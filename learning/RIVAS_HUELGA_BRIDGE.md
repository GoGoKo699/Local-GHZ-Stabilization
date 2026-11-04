# From open-system dynamics to local GHZ stabilization

An open chain of qubits is driven continuously by a fixed Hamiltonian and fixed dissipative channels. The goal is a coherent superposition of all zeros and all ones, reached from any initial density operator. The construction prepares a pure stationary state close to this GHZ state and gives an explicit time for reaching it.

Rivas and Huelga provide the open-system framework for expressing this task. The project supplies the particular two-body generator, the dark-state interference, and the quantitative argument for global attraction. This bridge connects those ingredients through a complete four-qubit instance. The [30-milestone map](MILESTONES.md) organizes the wider conceptual route; the [scientific account](../science/README.md) contains the authoritative proofs.

## Selected source and reading route

The anchor is Ángel Rivas and Susana F. Huelga, *Open Quantum Systems: An Introduction*, SpringerBriefs in Physics (2012), DOI [10.1007/978-3-642-23354-8](https://doi.org/10.1007/978-3-642-23354-8). Section, theorem, and equation numbers below refer specifically to [arXiv:1104.5242v2](https://arxiv.org/html/1104.5242v2), dated 9 February 2012. Its bibliography key is `RivasHuelga2012`.

| Author-version locator | Foundation used here |
|---|---|
| Sections 2.1–2.3 | Norms, operator exponentials, and continuous semigroups. |
| Sections 4.2–4.3; Theorem 4.4 | Completely positive trace-preserving maps and trace-norm contraction. |
| Section 5.2; Theorem 5.1, Eq. (46) | Lindblad generators with nonnegative rates. |
| Section 5.2; Eqs. (49)–(50) | Separation into no-jump evolution and recycling terms. |
| Section 5.4; Definition 5.3, Eq. (63), Theorem 5.4 | Stationarity, relaxation, and spectral characterization. |
| Sections 6.2 and 6.4.1 | Microscopic weak-coupling assumptions and interacting subsystems. |

The first five entries supply the main mathematical background. The final entry supports the distinction between an assumed effective generator and a microscopic implementation of its reservoirs.

## Translate the notation

The source's master equation separates rates $`\gamma_k`$ from operators $`V_k`$. This project absorbs their square roots into its jump operators. The translation is

```math
L_k=\sqrt{\gamma_k}\,V_k,
\qquad
\mathcal D[L_k](\rho)
=L_k\rho L_k^\dagger-\frac12\{L_k^\dagger L_k,\rho\}.
```

Thus a cleanup jump $`C_j=2P_{0,j}s_{j+1}`$ has rate four, and a jump $`J_j=\sqrt\gamma\,s_jP_{0,j+1}`$ has rate $`\gamma`$. Applying another factor of the rate to $`\mathcal D[C_j]`$ or $`\mathcal D[J_j]`$ would change the specified generator.

| Source notation | Project notation and meaning |
|---|---|
| $`\mathcal E_{(t_2,t_1)}`$ | $`e^{(t_2-t_1)\mathcal L}`$, since the generator is time independent. |
| $`\mathcal L_t`$ | The fixed generator $`\mathcal L`$. |
| $`\gamma_k,V_k`$ | Rate-weighted jumps $`C_j,J_j`$. |
| $`\rho_{\mathrm{ss}}`$ | The designed state $`\rho_\alpha`$. |
| System dimension in the proof of Theorem 5.1 | $`2^N`$ for a chain of $`N`$ qubits. |
| Bath-coupling parameter $`\alpha`$ in Section 6.4.1 | The project's $`\alpha`$ instead sets endpoint hopping amplitudes. |
| Trace norm | The project distance is $`D(\rho,\sigma)=\tfrac12\lVert\rho-\sigma\rVert_1`$. |

A density operator $`\rho`$ contains the probabilities and coherences of the state. An observable $`A`$ has expectation $`\mathrm{Tr}(A\rho)`$. Complete positivity and trace preservation ensure that the evolution is a quantum channel, and the semigroup property gives

```math
e^{(t+s)\mathcal L}=e^{t\mathcal L}e^{s\mathcal L}.
```

Trace-distance contractivity means that evolving two states by the same channel cannot increase their distinguishability. Here it allows a state close to the monotone sector to be compared with a state entirely inside that sector.

There are three different questions about the target. The identity $`\mathcal L(\rho_\alpha)=0`$ establishes stationarity. Global attraction requires convergence to $`\rho_\alpha`$ from every initial state. A preparation guarantee additionally needs a time bound uniform over those inputs. The following example exhibits the stationary state explicitly; the subsequent proof route explains the other two requirements.

## The model and its preparation task

For even $`N=2m\ge4`$, define $`P_{0,j}=|0\rangle\langle0|_j`$, $`P_{1,j}=|1\rangle\langle1|_j`$, $`s_j=|0\rangle\langle1|_j`$, and the Pauli operators $`X_j=s_j+s_j^\dagger`$ and $`Z_j=P_{0,j}-P_{1,j}`$. Operators on one or two specified sites act as the identity on the remaining sites.

The full generator has the form

```math
\mathcal L(\rho)
=-i[H,\rho]
+\sum_{j=1}^{N-1}\mathcal D[C_j](\rho)
+\sum_{r=1}^{m}\mathcal D[J_{2r-1}](\rho),
```

with $`C_j=2P_{0,j}s_{j+1}`$ and $`J_j=\sqrt\gamma\,s_jP_{0,j+1}`$. The [model page](../science/model.md#generator) gives the explicit Hamiltonian as one-site boundary fields and nearest-neighbor two-qubit terms. Its coherent action preserves the monotone configurations

```math
|j\rangle=|1\rangle^{\otimes j}|0\rangle^{\otimes(N-j)},
\qquad j=0,\ldots,N.
```

The label $`j`$ specifies the position of a domain wall, and these vectors span $`\mathcal M`$. In this notation $`|0\rangle`$ and $`|N\rangle`$ denote full-chain states. The labels are coordinates within the original qubit Hilbert space; they do not introduce an additional register.

Within $`\mathcal M`$, the Hamiltonian is a hopping path. Its endpoint amplitudes have magnitude $`\alpha`$, its bulk amplitudes are one, and a final sign fixes the GHZ-plus phase. The $`J_j`$ jumps drain odd path vertices to their neighboring even vertices. Their common dark state is selected by destructive interference under $`H`$:

```math
\begin{aligned}
|d_\alpha\rangle
&=\frac{|0\rangle+|N\rangle+
\alpha\sum_{r=1}^{m-1}(-1)^r|2r\rangle}
{\sqrt{Z_\alpha}},\\
Z_\alpha&=2+(m-1)\alpha^2,\\
\rho_\alpha&=|d_\alpha\rangle\langle d_\alpha|.
\end{aligned}
```

For a requested stationary GHZ infidelity $`0<\epsilon\le1/8`$, the parameters are

```math
\alpha^2=\frac{2\epsilon}{(m-1)(1-\epsilon)},
\qquad
\gamma=\frac{4\alpha}{\sqrt N}.
```

They give $`\langle\mathrm{GHZ}_N^+|\rho_\alpha|\mathrm{GHZ}_N^+\rangle=1-\epsilon`$. The generator has an exact stationary state; $`\epsilon`$ measures how closely that state approximates GHZ.

## A complete four-qubit example

Take $`N=4`$ and $`\alpha=1/2`$. Then $`\gamma=1`$, the cleanup rate is four, and the endpoint sign is positive. The physical Hamiltonian is

```math
\begin{aligned}
H_4
&=\frac14X_1(Z_2+I)
+\frac12X_2(Z_3-Z_1)\\
&\quad+\frac12X_3(Z_4-Z_2)
+\frac14X_4(I-Z_3).
\end{aligned}
```

Expanding each parenthesis gives only one-qubit and nearest-neighbor two-qubit terms. The five jump operators are

```math
\begin{aligned}
&C_1=2P_{0,1}s_2,
\quad C_2=2P_{0,2}s_3,
\quad C_3=2P_{0,3}s_4,\\
&J_1=s_1P_{0,2},
\quad J_3=s_3P_{0,4}.
\end{aligned}
```

These operators, together with the dissipator convention above, specify the evolution on all sixteen dimensions of the four-qubit Hilbert space.

### Five configurations inside sixteen dimensions

The monotone sector has the ordered basis

```math
|0000\rangle,
\quad |1000\rangle,
\quad |1100\rangle,
\quad |1110\rangle,
\quad |1111\rangle.
```

In this basis, the Hamiltonian and the nonzero restricted jumps are

```math
H_4\big|_{\mathcal M}
=\begin{pmatrix}
0&1/2&0&0&0\\
1/2&0&1&0&0\\
0&1&0&1&0\\
0&0&1&0&1/2\\
0&0&0&1/2&0
\end{pmatrix},
```

```math
J_1\big|_{\mathcal M}=|0000\rangle\langle1000|,
\qquad
J_3\big|_{\mathcal M}=|1100\rangle\langle1110|.
```

The $`C_j`$ jumps vanish on these five configurations. They remain essential on the full Hilbert space because a general input need not begin in this sector.

### Dark-state cancellation and fidelity

The stationary vector is

```math
|d_{1/2}\rangle
=\frac{2|0000\rangle-|1100\rangle+2|1111\rangle}{3}.
```

Its norm is one because the squared coefficients sum to $`(4+1+4)/9=1`$. Both restricted jumps annihilate it. The Hamiltonian produces an amplitude into $`|1000\rangle`$ from the first two components, and an amplitude into $`|1110\rangle`$ from the last two. In the unnormalized numerator, these amplitudes are respectively

```math
2\left(\frac12\right)-1=0,
\qquad
-1+2\left(\frac12\right)=0.
```

Thus $`H_4|d_{1/2}\rangle=0`$, and the full generator leaves its projector stationary. For the GHZ-plus vector, the fidelity is

```math
\begin{aligned}
|\mathrm{GHZ}_4^+\rangle
&=\frac{|0000\rangle+|1111\rangle}{\sqrt2},\\
|\langle\mathrm{GHZ}_4^+|d_{1/2}\rangle|^2
&=\left(\frac{4}{3\sqrt2}\right)^2
=\frac89.
\end{aligned}
```

Equivalently, the stationary infidelity is $`\epsilon=1/9`$. The coherent endpoint amplitudes are essential: an equal classical mixture of $`|0000\rangle`$ and $`|1111\rangle`$ has GHZ fidelity only $`1/2`$.

### Cleanup and a finite-time guarantee

A reverse wall is a neighboring substring $`01`$. For four qubits its weighted count is

```math
W=3q_1+2q_2+q_3,
\qquad q_j=P_{0,j}P_{1,j+1}.
```

For example, the cleanup jumps allow the transitions

```math
|0011\rangle
\overset{C_2}{\rightarrow}|0001\rangle
\overset{C_3}{\rightarrow}|0000\rangle.
```

Their wall weights decrease from two to one to zero. This example describes individual jump actions. The rigorous [operator inequality](../science/cleanup.md#uniform-decay-outside-the-monotone-sector) includes the concurrent Hamiltonian evolution and every possible initial coherence:

```math
\mathcal L^\dagger(W)\le-\frac23W,
\qquad
\mathrm{Tr}[(I-\Pi_{\mathcal M})\rho_t]
\le6e^{-2t/3}.
```

Inside $`\mathcal M`$, the general proof uses intervals of length $`\tau_{1/2}=16`$. Every jump output has dark-state population at least $`1/9`$. Writing $`p(t)=\langle d_{1/2}|\rho_t|d_{1/2}\rangle`$, it gives

```math
1-p(t+16)\le\frac{17}{18}[1-p(t)].
```

Combining cleanup with this path estimate gives the explicit sufficient time

```math
\begin{aligned}
T_4(\delta)
&=\frac32\log\left(\frac{24}{\delta^2}\right)\\
&\quad+16\left\lceil36\log\left(\frac2\delta\right)\right\rceil,
\qquad 0<\delta<1.
\end{aligned}
```

For every four-qubit input and every $`t\ge T_4(\delta)`$,

```math
D(\rho_t,\rho_{1/2})\le\delta,
\qquad
F_{\mathrm{GHZ}}(\rho_t)\ge\frac89-\delta.
```

This is the general theorem evaluated at the example's parameters. It is a conservative analytical guarantee, not a fitted or optimal time for this small system.

## What completes the argument beyond the anchor

The open-system framework supplies the mathematical meaning of a generator and relaxation. The construction requires several additional arguments tied to its physical operators. Their dependencies are useful even when the detailed algebra is read separately.

**A two-body Hamiltonian selects the dark superposition.** The neighboring terms cancel for equal neighboring spins and combine into wall hopping for unequal ones. The endpoint weights and alternating even-vertex amplitudes then solve every odd-vertex cancellation equation. [Model and stationary state](../science/model.md) proves this directly on the original qubit chain. A generic Lindblad form does not choose those coefficients.

**A weighted wall inequality treats arbitrary initial states.** The observable $`W`$ vanishes exactly on $`\mathcal M`$. Cleanup contributes at most $`-4Q`$ to its drift, the Hamiltonian contributes at most $`2Q`$, and the odd-bond jumps contribute a nonpositive term. Therefore

```math
\mathcal L^\dagger(W)\le-2Q\le-\frac{2}{N-1}W.
```

Because this is an operator inequality, its expectation bound applies to coherent and mixed inputs alike. [Removal of reverse domain walls](../science/cleanup.md) gives the full calculation. The local cleanup operator is inherited from earlier dissipative constructions, as attributed in [related work](../references/related-work.md).

**A survival estimate supplies a quantitative time scale.** Within $`\mathcal M`$, the Hamiltonian couples even and odd vertices through a matrix $`B`$. A pinned-path estimate gives $`s_{\min}(B)^2\ge\alpha^2/N`$. On the orthogonal complement of the dark state, its no-jump evolution decomposes into two-dimensional blocks. An explicit positive matrix solving a Lyapunov equation bounds the integrated survival in every block. It follows that by time $`4\sqrt N/\alpha`$, each bright initial vector has no-jump probability at most one half. These estimates are proved in [the convergence argument](../science/convergence.md#no-jump-survival-on-the-orthogonal-complement-of-the-dark-state).

**Jumps convert that survival bound into attraction.** Every jump output has target population at least $`f_\alpha=\alpha^2/Z_\alpha`$. The probability of at least one jump therefore gives a guaranteed gain in dark-state population during each interval. Repeating the argument contracts the remaining population. The no-jump representation describes a decomposition of the unconditional evolution; the preparation does not monitor the reservoir or select a measurement outcome.

**Projection and contractivity join the two estimates.** If the population outside $`\mathcal M`$ is $`q`$, a normalized comparison state supported on $`\mathcal M`$ lies at trace distance at most $`\sqrt q`$. The proof follows from projecting a purification and then tracing out its purifying system. Both states subsequently evolve under the same channel, so their distance cannot increase. Applying the path bound to the comparison state completes the [uniform full-space theorem](../science/convergence.md#return-to-the-full-hilbert-space).

Together these steps give, for every even $`N\ge4`$, $`0<\epsilon\le1/8`$, and $`0<\delta<1`$,

```math
\begin{aligned}
T_\epsilon(\delta)
&=\frac{N-1}{2}\log\left(\frac{2N(N-1)}{\delta^2}\right)\\
&\quad+\frac{4\sqrt N}{\alpha}
\left\lceil
\frac{4Z_\alpha}{\alpha^2}\log\left(\frac2\delta\right)
\right\rceil.
\end{aligned}
```

Here $`T_\epsilon`$ denotes the theorem's $`T`$ with its dependence on the chosen generator displayed. At every later time, all inputs obey $`D(\rho_t,\rho_\alpha)\le\delta`$ and $`F_{\mathrm{GHZ}}(\rho_t)\ge1-\epsilon-\delta`$. The exact formula implies

```math
T_\epsilon(\delta)
=O\left(
N\log\frac N\delta+
N^2\epsilon^{-3/2}\log\frac2\delta
\right).
```

The survival and population-transfer estimates supply this uniform bound directly. The spectral discussion in the anchor is useful background, but the numerical value of a dissipative gap alone is not the time estimate established here.

## Accuracy, resources, and perturbations

The error parameters answer different questions. Reducing $`\epsilon`$ changes the endpoint coupling $`\alpha`$ and the loss rate $`\gamma`$ so that the stationary state becomes closer to GHZ. Reducing $`\delta`$ runs that chosen generator longer. In the exact endpoint limit $`\alpha=0`$, the two ferromagnetic states cease to be uniquely combined by the dynamics. The quantitative result therefore concerns positive approximation errors.

The physical system contains exactly $`N`$ output qubits. It uses a number of local control and dissipative terms proportional to $`N`$, with bounded strength per term. Engineered reservoirs remain part of the model. The microscopic chapters of the anchor explain the context for deriving Markovian equations; this project assumes the specified effective generator and does not provide a microscopic reservoir implementation.

An overall physical rate $`g>0`$ scales $`H`$ to $`gH`$ and every jump $`L`$ to $`\sqrt g\,L`$. It changes the preparation time to $`T_\epsilon(\delta)/g`$. Fixing the sum of all local strengths instead of the strength per local term changes the resource convention and can add a factor proportional to $`N`$. [Accuracy and physical resources](../science/resources.md#locality-and-strength-accounting) states the explicit budget.

For perturbations, consider another valid time-independent Lindblad generator $`\mathcal L'=\mathcal L+\mathcal E`$. Let $`\nu`$ be the induced trace norm of $`\mathcal E`$ on Hermitian operators of the full chain, and set $`T=T_\epsilon(1/8)`$. The [perturbation argument](../science/resources.md#a-uniform-perturbation-guarantee) gives, for every stationary state $`\rho'`$ of the perturbed generator,

```math
D(\rho',\rho_\alpha)\le\frac23\nu T,
\qquad
F_{\mathrm{GHZ}}(\rho')\ge1-\epsilon-\frac23\nu T.
```

The bound compares a generator error with the time over which it acts. When the condition

```math
q'=\frac14+\nu T<1
```

holds, the [same analysis](../science/resources.md#a-uniform-perturbation-guarantee) also proves that $`\rho'`$ is unique and attracts every initial state, with

```math
D(e^{t\mathcal L'}\rho,\rho')
\le(q')^{\lfloor t/T\rfloor},
\qquad t\ge0.
```

Inverse-polynomial control precision is sufficient for the stated preparation family. A local error bound must remain valid after including the spectator qubits; a bare local induced norm does not automatically provide that guarantee. The [coefficient-error estimates](../science/resources.md#from-coefficient-errors-to-generator-errors) give suitable sufficient assumptions. These statements do not establish a fixed nonzero noise threshold as the chain grows.

## Continue through the scientific account

The [milestone map](MILESTONES.md) connects the prerequisite concepts to the mechanism, the global proof, and the resource boundary. For a direct mathematical route, read [model](../science/model.md), [cleanup](../science/cleanup.md), [convergence](../science/convergence.md), and [resources](../science/resources.md) in that order. The [related-work account](../references/related-work.md) separates the textbook foundation, inherited research ingredients, and the combination established here. [Verification](../verification/README.md) explains which finite instances are checked and how those checks relate to the arbitrary-size analytical proof.
