# Preparation accuracy, physical resources and perturbations

The construction acts on exactly the qubits that form the output state. Its cost is paid through local Hamiltonian control, engineered dissipative rates and convergence time. This page states those costs in the normalization of the [model](model.md), then explains what the uniform [mixing theorem](convergence.md) implies under small generator perturbations.

## Accuracy and preparation time

Let $`N=2m\geq4`$, and let $`\rho_\alpha`$ be the designed pure stationary state. For a specified stationary GHZ infidelity $`0<\epsilon\leq1/8`$, set

```math
\alpha^2=\frac{2\epsilon}{(m-1)(1-\epsilon)},
\qquad
\gamma=\frac{4\alpha}{\sqrt N},
\qquad \eta=4.
```

The target satisfies $`\langle\mathrm{GHZ}_N^+|\rho_\alpha|\mathrm{GHZ}_N^+\rangle=1-\epsilon`$. Write $`D(\rho,\sigma)=\frac12\lVert\rho-\sigma\rVert_1`$. Write $`T_\epsilon(\delta)=T(\delta)`$ for the explicit time in the convergence theorem, displaying its dependence on the chosen stationary infidelity. Every initial state then obeys

```math
D(e^{t\mathcal L}\rho,\rho_\alpha)\leq\delta
\quad\text{for all }t\geq T_\epsilon(\delta).
```

These two accuracy parameters have different roles. The parameter $`\epsilon`$ sets the generator and its stationary state. The parameter $`\delta`$ specifies how long to run that generator. Since the expectation of a projector changes by at most trace distance,

```math
\langle\mathrm{GHZ}_N^+|e^{t\mathcal L}(\rho)|\mathrm{GHZ}_N^+\rangle
\geq1-\epsilon-\delta.
```

The corresponding trace-distance bound to the ideal GHZ state is

```math
D(e^{t\mathcal L}\rho,|\mathrm{GHZ}_N^+\rangle\langle\mathrm{GHZ}_N^+|)
\leq\delta+\sqrt\epsilon.
```

For a total requested GHZ infidelity $`0<\chi\leq1/4`$, choosing $`\epsilon=\delta=\chi/2`$ therefore gives an unconditional preparation time

```math
O\!\left(
N\log\frac{N}{\chi}
+N^2\chi^{-3/2}\log\frac{1}{\chi}
\right).
```

There is no success flag or discarded branch. The dissipative evolution runs from an arbitrary input state to the specified accuracy.

## Locality and strength accounting

The physical system is an open chain of $`N`$ two-level systems. Its generator contains $`N-1`$ cleanup jumps and $`N/2`$ alternating loss jumps. The Hamiltonian can be written as $`N-1`$ nearest-neighbor terms and two boundary fields:

```math
H=\frac{\Omega_1X_1+\Omega_NX_N}{2}
+\frac12\sum_{j=1}^{N-1}
\left(\Omega_jX_jZ_{j+1}-\Omega_{j+1}Z_jX_{j+1}\right).
```

The virtual $`Z_0`$ and $`Z_{N+1}`$ values in the compact model definition are scalars that produce these fields. They do not add boundary qubits. Individual pair terms need not preserve the monotone domain-wall subspace; their coherent sum does. The cancellation is part of the specified static Hamiltonian.

In the present units, every bond Hamiltonian has norm at most one, every boundary field has norm at most $`1/2`$, the cleanup jumps have squared norm four, and the alternating jumps have squared norm $`\gamma\leq2`$. Thus local strengths are bounded independently of system size. The sum of local strengths is extensive. For example, the budget

```math
B=\sum_{\text{Hamiltonian terms }a}\lVert h_a\rVert_\infty
+\sum_{\text{jumps }b}\lVert L_b\rVert_\infty^2
```

satisfies $`B\leq6N`$ in the stated parameter range. This budget is one explicit convention; the headline time bound assumes bounded strength per local term, with $`O(N)`$ terms available simultaneously.

An overall physical rate $`g>0`$ restores units through $`H_{\rm phys}=gH`$ and $`L_{b,\rm phys}=\sqrt g\,L_b`$. The physical time is $`T_\epsilon(\delta)/g`$. If the sum budget is instead fixed to $`\Lambda`$, rescale the whole generator by $`\Lambda/B`$. The same construction then takes $`(B/\Lambda)T_\epsilon(\delta)`$, at most an additional factor of order $`N/\Lambda`$ in the normalized expression.

The weak parameters scale as

```math
\alpha=\Theta\!\left(\sqrt{\epsilon/N}\right),
\qquad
\gamma=\Theta\!\left(\sqrt\epsilon/N\right).
```

The system has no retained controller register, extra on-site level, feedback record or switching schedule. Engineered reservoirs are assumed by the Lindblad description. A microscopic realization must account for the apparatus that produces those reservoirs and Hamiltonian terms.

## A uniform perturbation guarantee

Let $`T=T_\epsilon(1/8)`$, and write $`\Phi=e^{T\mathcal L}`$. The mixing theorem implies

```math
\lVert\Phi(X)\rVert_1\leq\frac14\lVert X\rVert_1
```

for every Hermitian trace-zero operator $`X`$. To see this, use its Jordan decomposition $`X=X_+-X_-`$, with $`\mathrm{Tr}X_+=\mathrm{Tr}X_-=\lVert X\rVert_1/2`$. Each normalized part evolves to within trace distance $`1/8`$ of $`\rho_\alpha`$. Their difference consequently has full trace norm at most $`1/2`$, yielding the coefficient $`1/4`$ above.

Consider another valid time-independent Lindblad generator

```math
\mathcal L'=\mathcal L+\mathcal E,
\qquad
\nu=\lVert\mathcal E\rVert_{1\to1,\mathrm{Herm}}
=\sup_{X=X^\dagger\ne0}
\frac{\lVert\mathcal E(X)\rVert_1}{\lVert X\rVert_1}.
```

Here the norm is taken on the full $`N`$-qubit system. Duhamel's identity and trace-norm contractivity of both completely positive trace-preserving semigroups give

```math
e^{t\mathcal L'}-e^{t\mathcal L}
=\int_0^t e^{(t-s)\mathcal L'}\mathcal E e^{s\mathcal L}\,ds,
\qquad
\lVert(e^{t\mathcal L'}-e^{t\mathcal L})X\rVert_1
\leq\nu t\lVert X\rVert_1
```

for Hermitian $`X`$. Every stationary state $`\rho'`$ of $`\mathcal L'`$ therefore satisfies

```math
\lVert\rho'-\rho_\alpha\rVert_1
\leq\nu T+\frac14\lVert\rho'-\rho_\alpha\rVert_1,
\qquad
\lVert\rho'-\rho_\alpha\rVert_1\leq\frac43\nu T.
```

In particular, its GHZ infidelity is at most

```math
1-\langle\mathrm{GHZ}_N^+|\rho'|\mathrm{GHZ}_N^+\rangle
\leq\epsilon+\frac23\nu T.
```

This stationary-state estimate holds for every valid perturbed generator, although it becomes uninformative when $`\nu T`$ is large. For small perturbations it also gives a convergence statement. If

```math
q'=\frac14+\nu T<1,
```

then $`e^{T\mathcal L'}`$ is a strict trace-distance contraction. It has a unique fixed density operator. Semigroup commutation makes that fixed state stationary under every $`e^{t\mathcal L'}`$, so it is the unique stationary state of $`\mathcal L'`$. Iteration and contractivity during the remaining fraction of the interval yield

```math
D(e^{t\mathcal L'}\rho,\rho')
\leq(q')^{\lfloor t/T\rfloor}
```

for every initial state. This argument does not assume that $`\rho'`$ remains pure.

## From coefficient errors to generator errors

The norm in the previous section includes all spectator qubits. A bare local induced trace norm must not be treated as automatically invariant under tensoring with an identity map. One convenient sufficient assumption is that each embedded local generator error has induced Hermitian trace norm at most $`\zeta`$; a local diamond-norm bound of $`\zeta`$ also suffices. With $`M=O(N)`$ such errors, the triangle inequality gives $`\nu\leq M\zeta`$.

Direct coefficient estimates avoid this tensor-extension issue. An embedded Hamiltonian error $`\Delta h`$ contributes at most $`2\lVert\Delta h\rVert_\infty`$ to $`\nu`$. For a jump $`L`$ changed to $`L+\Delta L`$,

```math
\lVert\mathcal D[L+\Delta L]-\mathcal D[L]\rVert_{1\to1,\mathrm{Herm}}
\leq4\lVert L\rVert_\infty\lVert\Delta L\rVert_\infty
+2\lVert\Delta L\rVert_\infty^2.
```

This follows by expanding the recycling and anticommutator terms and using $`\lVert AXB\rVert_1\leq\lVert A\rVert_\infty\lVert B\rVert_\infty\lVert X\rVert_1`$. A rate error $`\Delta r\,\mathcal D[A]`$ contributes at most $`2|\Delta r|\lVert A\rVert_\infty^2`$, provided the resulting total rates define a valid generator.

For $`O(N)`$ bounded local terms, these estimates show that inverse-polynomial coefficient precision is sufficient. A conservative scale for preserving an additional GHZ infidelity of order $`\epsilon`$ is

```math
\zeta=O\!\left(\frac{\epsilon}{N T_\epsilon(1/8)}\right)
=O\!\left(\frac{\epsilon^{5/2}}{N^3}\right),
```

with a sufficiently small constant and the norm convention stated above. This is a sufficient tolerance derived from a conservative mixing bound. It does not identify an optimal noise floor or establish a nonzero noise threshold as $`N`$ grows.

## Scope of the construction

The proved family has even chain length. Its resources, fidelity and mixing estimates are explicit at each finite $`N`$. As $`\epsilon`$ approaches zero, the chosen generator changes and the convergence guarantee slows. At the exact endpoint the limiting dynamics has additional invariant states, consistently with the established locality obstruction for exact GHZ stabilization on sufficiently long chains [TV14]. The result supplies a controlled approximation within the original qubit Hilbert space. The [related-work account](../references/related-work.md) separates that contribution from generic state-preparation methods and auxiliary-system schemes.
