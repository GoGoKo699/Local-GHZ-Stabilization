#!/usr/bin/env python3
"""Finite-size checks of the even-qubit local GHZ stabilization model.

The full model is assembled from local Kronecker products. A separately
assembled clock path checks its restriction. Floating-point calculations
support the stated finite cases; they do not prove the arbitrary-size theorem.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import sys
import time

import numpy as np
import scipy
from scipy import linalg, sparse
from scipy.sparse.linalg import expm_multiply


ALGEBRA_TOL = 1e-10
EVOLUTION_TOL = 1e-8
I2 = np.eye(2, dtype=complex)
X2 = np.array([[0, 1], [1, 0]], dtype=complex)
Z2 = np.diag([1, -1]).astype(complex)
P0 = np.diag([1, 0]).astype(complex)
P1 = np.diag([0, 1]).astype(complex)
LOWER = np.array([[0, 1], [0, 0]], dtype=complex)


@dataclass
class Checks:
    count: int = 0
    failures: list[str] = field(default_factory=list)

    def require(self, name: str, condition: bool) -> None:
        self.count += 1
        if not condition:
            self.failures.append(name)

    def small(self, name: str, value: float, tol: float = ALGEBRA_TOL) -> None:
        self.require(name, bool(np.isfinite(value) and value <= tol))


def embed(n: int, factors: dict[int, np.ndarray]) -> sparse.csr_matrix:
    """Site zero is the leftmost computational-basis bit."""
    out = sparse.csr_matrix([[1.0 + 0j]])
    for site in range(n):
        out = sparse.kron(out, factors.get(site, I2), format="csr")
    return out


def full_model(n: int, alpha: float) -> dict:
    """Build only explicit one-site and adjacent two-site terms."""
    m, dim, eta = n // 2, 2**n, 4.0
    gamma = 4 * alpha / np.sqrt(n)
    omega = np.ones(n)
    omega[0], omega[-1] = alpha, (-1)**m * alpha
    h = 0.5 * omega[0] * embed(n, {0: X2})
    h += 0.5 * omega[-1] * embed(n, {n-1: X2})
    cleanup, pump = [], []
    q = sparse.csr_matrix((dim, dim), dtype=complex)
    w = q.copy()
    for j in range(n-1):
        h += 0.5 * omega[j] * embed(n, {j: X2, j+1: Z2})
        h -= 0.5 * omega[j+1] * embed(n, {j: Z2, j+1: X2})
        cleanup.append(np.sqrt(eta) * embed(n, {j: P0, j+1: LOWER}))
        if j % 2 == 0:
            pump.append(np.sqrt(gamma) * embed(n, {j: LOWER, j+1: P0}))
        qj = embed(n, {j: P0, j+1: P1})
        q += qj
        w += (n-1-j) * qj
    return dict(n=n, alpha=alpha, eta=eta, gamma=gamma, omega=omega,
                h=h.tocsr(), cleanup=cleanup, pump=pump, q=q, w=w)


def clock_model(n: int, alpha: float, gamma: float) -> dict:
    """Independent path definition, not extracted from the full operators."""
    m, dim = n // 2, n+1
    h = np.zeros((dim, dim), dtype=complex)
    for j in range(1, n+1):
        edge = alpha if j == 1 else ((-1)**m * alpha if j == n else 1.0)
        h[j-1, j] = h[j, j-1] = edge
    jumps = []
    for j in range(1, n, 2):
        jump = np.zeros_like(h)
        jump[j-1, j] = np.sqrt(gamma)
        jumps.append(sparse.csr_matrix(jump))
    d = np.zeros(dim, dtype=complex)
    d[0] = d[-1] = 1
    for r in range(1, m):
        d[2*r] = (-1)**r * alpha
    z = 2 + (m-1)*alpha**2
    d /= np.sqrt(z)
    # The integer with j leading ones and n-j trailing zeros.
    indices = [((1 << j)-1) << (n-j) for j in range(n+1)]
    v = sparse.csr_matrix((np.ones(dim), (indices, range(dim))), shape=(2**n, dim))
    return dict(h=sparse.csr_matrix(h), jumps=jumps, d=d, z=z, v=v)


def norm(a) -> float:
    return float(sparse.linalg.norm(a) if sparse.issparse(a) else linalg.norm(a))


def dissipator_adjoint(j, a):
    jj = j.conj().T @ j
    return j.conj().T @ a @ j - (jj @ a + a @ jj)/2


def generator_action(h, jumps, rho):
    out = -1j*(h @ rho-rho @ h)
    for j in jumps:
        jj = j.conj().T @ j
        out += j @ rho @ j.conj().T - (jj @ rho+rho @ jj)/2
    return out


def liouvillian(h, jumps) -> sparse.csr_matrix:
    """Column vectorization: vec(A rho B) = (B.T tensor A) vec(rho)."""
    eye = sparse.eye(h.shape[0], dtype=complex, format="csr")
    out = -1j*(sparse.kron(eye, h)-sparse.kron(h.T, eye))
    for j in jumps:
        jj = j.conj().T @ j
        out += sparse.kron(j.conjugate(), j)
        out -= (sparse.kron(eye, jj)+sparse.kron(jj.T, eye))/2
    return out.tocsr()


def max_hermitian_eigenvalue(a, label: str, checks: Checks) -> float:
    dense = a.toarray() if sparse.issparse(a) else a
    checks.small(label+": Hermiticity", norm(dense-dense.conj().T))
    value = float(linalg.eigvalsh((dense+dense.conj().T)/2)[-1])
    checks.small(label, value)
    return value


def spectral_data(l, label: str, checks: Checks, singular_values=False) -> dict:
    dense = l.toarray()
    es = linalg.eigvals(dense)
    zero_count = int(np.count_nonzero(np.abs(es) <= EVOLUTION_TOL))
    checks.require(label+": one numerical zero eigenvalue", zero_count == 1)
    checks.small(label+": no positive real eigenvalues", float(es.real.max()), EVOLUTION_TOL)
    nonzero = es[np.abs(es) > EVOLUTION_TOL]
    gap = float(-nonzero.real.max())
    checks.require(label+": positive observed spectral gap", gap > EVOLUTION_TOL)
    result = dict(zero_eigenvalue_count=zero_count, observed_spectral_gap=gap,
                  largest_eigenvalue_real_part=float(es.real.max()))
    if singular_values:
        sv = linalg.svdvals(dense)
        nullity = int(np.count_nonzero(sv <= EVOLUTION_TOL))
        checks.require(label+": one numerical singular null direction", nullity == 1)
        result.update(singular_nullity=nullity, smallest_singular_value=float(sv[-1]),
                      second_smallest_singular_value=float(sv[-2]))
    return result


def trajectory_checks(l, d, gap: float, label: str, checks: Checks,
                      full_space: bool) -> dict:
    """Deterministic sample inputs, with no statistical or worst-case claim."""
    dim = len(d)
    basis = np.zeros(dim, dtype=complex)
    basis[5 if full_space else 1] = 1  # |0101> for N=4, |1> on the clock.
    coherent = np.exp(1j*np.sqrt(2)*np.arange(dim))/np.sqrt(dim)
    inputs = {
        "maximally_mixed": np.eye(dim, dtype=complex)/dim,
        "coherent_phase_state": np.outer(coherent, coherent.conjugate()),
        "alternating_basis" if full_space else "odd_clock_basis": np.outer(basis, basis),
    }
    pd = np.outer(d, d.conjugate())
    times = np.array([0.0, 1.0, 2.0, 4.0, 8.0])/gap
    vecs = np.column_stack([rho.reshape(-1, order="F") for rho in inputs.values()])
    trajectories = {name: dict(half_trace_distance=[], dark_population=[])
                    for name in inputs}
    trace_error = hermiticity_error = 0.0
    least_eigenvalue = 1.0
    for t in times:
        states = vecs if t == 0 else expm_multiply(l*t, vecs, traceA=t*l.diagonal().sum())
        for index, name in enumerate(inputs):
            rho = states[:, index].reshape((dim, dim), order="F")
            trace_error = max(trace_error, float(abs(np.trace(rho)-1)))
            hermiticity_error = max(hermiticity_error, norm(rho-rho.conj().T))
            rh = (rho+rho.conj().T)/2
            least_eigenvalue = min(least_eigenvalue, float(linalg.eigvalsh(rh)[0]))
            distance = float(np.abs(linalg.eigvalsh(rh-pd)).sum()/2)
            population = float(np.vdot(d, rh@d).real)
            trajectories[name]["half_trace_distance"].append(distance)
            trajectories[name]["dark_population"].append(population)
    checks.small(label+": trace preservation", trace_error, EVOLUTION_TOL)
    checks.small(label+": Hermiticity preservation", hermiticity_error, EVOLUTION_TOL)
    checks.small(label+": positivity", -least_eigenvalue, EVOLUTION_TOL)
    for name, trajectory in trajectories.items():
        distances = np.array(trajectory["half_trace_distance"])
        checks.small(label+" "+name+": distance nonincrease", float(np.diff(distances).max()), EVOLUTION_TOL)
        checks.require(label+" "+name+": observed decay", distances[-1] < distances[0])
        if not full_space:
            population = np.array(trajectory["dark_population"])
            checks.small(label+" "+name+": dark population nondecrease",
                         float((-np.diff(population)).max()), EVOLUTION_TOL)
    return dict(times=times.tolist(), time_unit="Hamiltonian bulk hopping = 1",
                max_trace_error=trace_error, max_hermiticity_error=hermiticity_error,
                minimum_density_eigenvalue=least_eigenvalue, inputs=trajectories)


def check_size(n: int, alpha: float, checks: Checks) -> dict:
    full = full_model(n, alpha)
    path = clock_model(n, alpha, full["gamma"])
    h, cs, js, q, w = (full[key] for key in ("h", "cleanup", "pump", "q", "w"))
    hp, jp, dp, v = (path[key] for key in ("h", "jumps", "d", "v"))
    d = np.asarray(v@dp).ravel()
    label = f"N={n}"
    pd = sparse.csr_matrix(np.outer(d, d.conjugate()))
    residuals = {
        "hamiltonian_hermiticity": norm(h-h.conj().T),
        "dark_hamiltonian": norm(h@d),
        "dark_jumps": max(norm(j@d) for j in cs+js),
        "stationary_generator": norm(generator_action(h, cs+js, pd)),
        "clock_hamiltonian_intertwining": norm(h@v-v@hp),
        "clock_cleanup_annihilation": max(norm(c@v) for c in cs),
        "clock_pump_intertwining": max(norm(j@v-v@p) for j, p in zip(js, jp)),
    }
    for name, value in residuals.items():
        checks.small(label+" "+name, value)
    ghz = np.zeros(2**n, dtype=complex)
    ghz[0] = ghz[-1] = 1/np.sqrt(2)
    fidelity = float(abs(np.vdot(ghz, d))**2)
    checks.small(label+": GHZ fidelity formula", abs(fidelity-2/path["z"]))
    wdiag, qdiag = w.diagonal().real, q.diagonal().real
    checks.require(label+": W kernel dimension", np.count_nonzero(wdiag == 0) == n+1)
    checks.small(label+": nonclock leakage below W", float(np.max((qdiag > 0)-wdiag)))
    checks.small(label+": W below (N-1)Q", float(np.max(wdiag-(n-1)*qdiag)))
    dc = sum((dissipator_adjoint(j, w) for j in cs), start=w*0)
    dj = sum((dissipator_adjoint(j, w) for j in js), start=w*0)
    dh = 1j*(h@w-w@h)
    drift_values = {}
    for name, matrix in {
        "hamiltonian_minus_2Q": dh-2*q,
        "cleanup_plus_etaQ": dc+full["eta"]*q,
        "pump": dj,
        "total_plus_2Q": dh+dc+dj+2*q,
        "total_plus_2W_over_N_minus_1": dh+dc+dj+2*w/(n-1),
    }.items():
        drift_values[name] = max_hermitian_eigenvalue(matrix, label+" "+name, checks)
    b = hp.toarray()[np.ix_(range(1, n, 2), range(0, n+1, 2))]
    singular = linalg.svdvals(b)
    smin2, lower = float(singular[-1]**2), alpha**2/n
    checks.small(label+": singular-value lower bound", lower-smin2)
    m = n//2
    gauge = np.diag((-1.0)**np.arange(m))
    laplacian = np.diag([1.0]+[2.0]*(m-2)+[1.0])
    laplacian += np.diag(-np.ones(m-1), 1)+np.diag(-np.ones(m-1), -1)
    laplacian[0, 0] += alpha**2
    laplacian[-1, -1] += alpha**2
    laplacian_residual = norm(gauge@(b@b.conj().T)@gauge-laplacian)
    checks.small(label+": pinned Laplacian identity", laplacian_residual)
    gamma = full["gamma"]
    lyapunov_residual = 0.0
    for s in singular:
        f = np.array([[0, -1j*s], [-1j*s, -gamma/2]])
        ps = np.array([[2/gamma+gamma/(4*s*s), -1j/(2*s)], [1j/(2*s), 2/gamma]])
        lyapunov_residual = max(lyapunov_residual, norm(f.conj().T@ps+ps@f+np.eye(2)))
        checks.require(label+": positive Lyapunov matrix", linalg.eigvalsh(ps)[0] > 0)
    checks.small(label+": Lyapunov identity", lyapunov_residual)
    pdp = np.outer(dp, dp.conjugate())
    bright = np.eye(n+1)-pdp
    odd_projector = np.diag([j % 2 for j in range(n+1)])
    tau = 4*np.sqrt(n)/alpha
    k = linalg.expm(tau*(-1j*hp.toarray()-gamma*odd_projector/2))
    survival = float(linalg.svdvals(k@bright)[0]**2)
    checks.small(label+": no-jump bright survival bound", survival-0.5, EVOLUTION_TOL)
    lp = liouvillian(hp, jp)
    channel = linalg.expm(tau*lp.toarray())
    q_heisenberg = (channel.conj().T@bright.reshape(-1, order="F")).reshape((n+1, n+1), order="F")
    fmin = alpha**2/path["z"]
    contraction_eigenvalue = max_hermitian_eigenvalue(
        q_heisenberg-(1-fmin/2)*bright, label+": path one-interval contraction", checks)
    result = dict(n=n, alpha=alpha, epsilon=1-fidelity, eta=full["eta"], gamma=gamma,
                  normalization=path["z"], ghz_fidelity=fidelity, residuals=residuals,
                  drift_max_eigenvalues=drift_values,
                  smin_squared=smin2, smin_squared_lower_bound=lower,
                  pinned_laplacian_residual=laplacian_residual,
                  lyapunov_residual=lyapunov_residual, interval_tau=tau,
                  bright_no_jump_survival_operator_norm_squared=survival,
                  path_contraction_residual_max_eigenvalue=contraction_eigenvalue)
    if n in (4, 6):
        sp = spectral_data(lp, label+" path", checks)
        result["path_spectrum"] = sp
        result["path_trajectories"] = trajectory_checks(
            lp, dp, sp["observed_spectral_gap"], label+" path", checks, False)
    if n == 4:
        lf = liouvillian(h, cs+js)
        checks.small("N=4 vectorized stationary residual", norm(lf@pd.toarray().reshape(-1, order="F")))
        sf = spectral_data(lf, "N=4 full Liouvillian", checks, singular_values=True)
        result["full_spectrum"] = sf
        result["full_trajectories"] = trajectory_checks(
            lf, d, sf["observed_spectral_gap"], "N=4 full", checks, True)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nmax", type=int, default=8, help="largest even N; default 8, allowed 4 to 10")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--alpha", type=float, help="fixed endpoint amplitude; default 0.2")
    group.add_argument("--epsilon", type=float, help="fixed GHZ infidelity in (0,1/8], with alpha chosen separately for each N")
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    if args.nmax not in (4, 6, 8, 10):
        parser.error("--nmax must be one of 4, 6, 8, 10; the full-operator checks use dense eigenvalue calculations")
    if args.epsilon is not None and not (0 < args.epsilon <= 1/8):
        parser.error("--epsilon must lie in (0,1/8]")
    alpha = 0.2 if args.alpha is None else args.alpha
    if args.epsilon is None and not (0 < alpha <= 1 and (args.nmax/2)*alpha**2 <= 1):
        parser.error("--alpha must be positive and satisfy (nmax/2)*alpha**2 <= 1 for the checked singular-value bound")
    start = time.perf_counter()
    checks = Checks()
    rows = []
    for n in range(4, args.nmax+1, 2):
        a = alpha if args.epsilon is None else np.sqrt(2*args.epsilon/((n//2-1)*(1-args.epsilon)))
        rows.append(check_size(n, float(a), checks))
    report = {
        "status": "passed" if not checks.failures else "failed",
        "scope": "Floating-point finite-size verification; no arbitrary-N or noise-threshold inference.",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "parameters": {"nmax": args.nmax, "alpha": alpha if args.epsilon is None else None,
                       "epsilon": args.epsilon, "eta": 4.0, "gamma": "4*alpha/sqrt(N)"},
        "tolerances": {"algebra_absolute": ALGEBRA_TOL, "evolution_and_numerical_nullity": EVOLUTION_TOL},
        "check_count": checks.count, "failures": checks.failures,
        "elapsed_seconds": time.perf_counter()-start, "sizes": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(f"{report['status'].upper()}: {checks.count} finite-size checks; N = {[row['n'] for row in rows]}")
    for row in rows:
        print(f"N={row['n']}: GHZ fidelity={row['ghz_fidelity']:.9f}, "
              f"smin^2={row['smin_squared']:.9g} >= {row['smin_squared_lower_bound']:.9g}")
    print(f"N=4 full Liouvillian: numerical nullity={rows[0]['full_spectrum']['singular_nullity']}, "
          f"observed gap={rows[0]['full_spectrum']['observed_spectral_gap']:.9g}")
    print(f"Report: {args.output}")
    for failure in checks.failures:
        print("FAILED: "+failure, file=sys.stderr)
    return int(bool(checks.failures))


if __name__ == "__main__":
    raise SystemExit(main())
