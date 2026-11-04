# Numerical verification

The verifier assembles the Hamiltonian and jumps from explicit local Kronecker
products on the full qubit Hilbert space. It also assembles the monotone clock
path independently. Agreement between these two constructions checks the site
ordering, boundary signs, jump directions, and restriction used in the proofs.

The recorded run covers even sizes $`N=4,6,8`$. Full operator inequalities are
checked at each size. The full Liouvillian spectrum and sample evolutions are
computed for $`N=4`$; path evolutions are computed for $`N=4,6`$. The
[scientific account](../science/) supplies the proofs for arbitrary even $`N`$.
These floating-point calculations do not establish that general result.

## Reproduce the recorded run

Run these commands from the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_construction.py --nmax 8 --alpha 0.2 --output verification/results.json
```

The dependencies used for the recorded run are Python 3.12.14, NumPy 2.3.5,
and SciPy 1.17.0. The requirements file pins the two numerical packages.
The script exits with status zero when all checks pass and status one when
any numerical check fails. An invalid parameter choice exits through the
command-line parser.

The expected summary for this parameter choice is:

```text
PASSED: 134 finite-size checks; N = [4, 6, 8]
N=4: GHZ fidelity=0.980392157, smin^2=0.04 >= 0.01
N=6: GHZ fidelity=0.961538462, smin^2=0.0265476238 >= 0.00666666667
N=8: GHZ fidelity=0.943396226, smin^2=0.01980002 >= 0.005
N=4 full Liouvillian: numerical nullity=1, observed gap=0.0452363012
Report: verification/results.json
```

Rounding in the last digits can depend on the numerical backend. The recorded
run completed in approximately 1.2 seconds of script runtime. Runtime is an
observation for this environment, not a complexity guarantee.

| File | Content |
|---|---|
| [check_construction.py](check_construction.py) | Model builders, numerical checks, and report generation. |
| [requirements.txt](requirements.txt) | Exact NumPy and SciPy versions used. |
| [results.json](results.json) | Parameters, tolerances, source hash, versions, residuals, spectra, and sampled trajectories from the recorded run. |
| [results_epsilon.json](results_epsilon.json) | Additional $`N=4`$ run at the allowed infidelity endpoint $`\epsilon=1/8`$. |

The report includes the SHA-256 hash of the script used to generate it. Its
timestamp and runtime will change on a new run. Parameter values and residuals
should be compared alongside the reported pass status.

## Model conventions

Site 1 is the leftmost bit in the computational basis. The single-site
operators are $`Z=\mathrm{diag}(1,-1)`$ and
$`s=|0\rangle\langle1|`$. The dissipator convention is
$`D[L](\rho)=L\rho L^\dagger-\{L^\dagger L,\rho\}/2`$.

For $`N=2m`$, the endpoint hoppings are
$`\Omega_1=\alpha`$ and $`\Omega_N=(-1)^m\alpha`$, with unit bulk hoppings.
The final sign makes the endpoint superposition GHZ plus for every checked
size. The script uses $`\eta=4`$ and $`\gamma=4\alpha/\sqrt{N}`$.
The full Hamiltonian is built as two boundary fields and the adjacent pair
terms $`(\Omega_jX_jZ_{j+1}-\Omega_{j+1}Z_jX_{j+1})/2`$.

The clock basis is $`|j\rangle=|1\rangle^{\otimes j}|0\rangle^{\otimes(N-j)}`$.
Its isometry into the full space is constructed from computational-basis
indices. The path Hamiltonian and path jumps are specified directly, without
projecting the full operators to define them. Matrix vectorization uses column
order throughout the Liouvillian calculation.

## What is checked

| Check | Finite-size evidence |
|---|---|
| Dark state and stationarity | Hamiltonian annihilation, jump annihilation, generator residual, and the GHZ fidelity formula. |
| Clock reduction | Intertwining of the full and path Hamiltonians and jumps; cleanup annihilation of the entire clock subspace. |
| Cleanup drift | Hermiticity and largest eigenvalues for the separate Hamiltonian, cleanup, pump, and total drift inequalities; the leakage bound from the diagonal weight operator. |
| Path spectrum | The pinned-Laplacian identity and $`s_{\min}^2\ge\alpha^2/N`$. |
| No-jump estimate | The two-dimensional Lyapunov equation, positivity of its solution, and the bright-sector survival bound at the stated interval. |
| Jump gain | The path channel's one-interval contraction inequality is checked as a matrix inequality, covering all path inputs at each checked size. |
| Full-space stationary nullity | Eigenvalues and singular values of the complete $`N=4`$ Liouvillian each give one numerical null direction. |
| Sample evolution | Trace, Hermiticity, positivity, distance nonincrease, and observed decay for three deterministic inputs; dark population is also checked to increase on the path. |

The algebra tolerance is an absolute $`10^{-10}`$. Evolution and numerical
nullity use $`10^{-8}`$. Values slightly below zero at the scale of floating-point
roundoff are retained in the report rather than silently set to zero.

The three sample inputs are the maximally mixed state, a coherent state with
amplitudes proportional to $`\exp(i\sqrt{2}j)`$, and a basis state. The basis
state is $`|0101\rangle`$ in the full $`N=4`$ space and the odd clock state $`|1\rangle`$
on the path. Each evolution is sampled at times $`0,1,2,4,8`$ divided by that
finite model's observed spectral gap. This choice resolves the observed decay;
it is not the analytical worst-input mixing bound.

In the recorded run, the largest structural residual among the dark-state
and clock-intertwining checks was below $`4\times10^{-17}`$. All three full
$`N=4`$ sample inputs reached half trace distance below $`2.74\times10^{-4}`$
at the final sampled time. These are finite examples. The sampled trajectories
alone do not certify convergence for every input, and a finite spectral gap
alone does not establish the stated arbitrary-size mixing theorem.

## Parameters and limits

`--nmax` selects all even sizes from 4 through its value. The allowed values
are 4, 6, 8, and 10, with default 8. The cap keeps the full operator eigenvalue
calculations modest. Full Liouvillian diagonalization remains restricted to
$`N=4`$, regardless of this setting.

`--alpha` fixes the endpoint amplitude across sizes; its default is 0.2.
The verifier requires $`(N_{\max}/2)\alpha^2\le1`$, which is the hypothesis of
the singular-value bound used here. Alternatively, `--epsilon` fixes the GHZ
infidelity in $`(0,1/8]`$ and chooses the required amplitude separately at each
size. For example:

```bash
python verification/check_construction.py --nmax 4 --epsilon 0.125 --output verification/results_epsilon.json
```

This additional recorded run passed 58 checks, with GHZ fidelity 0.875 and one
numerical stationary null direction. It exercises the infidelity input and
the endpoint of the stated infidelity range.

The script and the checked theorem use even $`N\ge4`$. No odd-size, fixed-noise
threshold, optimality, experimental implementation, or large-system spectral
claim is inferred from this numerical suite. Very small amplitudes can become
ill-conditioned at the fixed floating-point tolerances; a failed numerical
nullity check in that regime requires numerical analysis before it can be
interpreted physically.
