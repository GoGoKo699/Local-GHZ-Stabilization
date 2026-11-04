# Two-body generator and stationary state

An open chain of physical qubits can prepare an approximate Greenberger–Horne–Zeilinger (GHZ) state by using its domain-wall configurations as a coherent transport path. The two ferromagnetic configurations form the endpoints of this path. Weak endpoint couplings concentrate a dark state on these configurations, while local dissipation removes reverse domain walls and transfers population into the dark state.

This page defines the generator and its exact stationary state. [Removal of reverse domain walls](cleanup.md) controls arbitrary initial states, including coherences outside the transport sector. [Uniform convergence](convergence.md) then proves uniqueness and gives an explicit preparation time.

## Chain, units, and distance

The system consists of an even number $`N=2m\ge4`$ of qubits with open boundaries and Hilbert space

```math
\mathcal H=(\mathbb C^2)^{\otimes N}.
```

The local basis is $`|0\rangle,|1\rangle`$. Write

```math
P_{0,j}=|0\rangle\langle0|_j,
\qquad
P_{1,j}=|1\rangle\langle1|_j,
\qquad
s_j=|0\rangle\langle1|_j,
```

```math
X_j=s_j+s_j^\dagger,
\qquad
Y_j=-i s_j+i s_j^\dagger,
\qquad
Z_j=P_{0,j}-P_{1,j}.
```

Operators on different sites are tensored with the identity on the remaining qubits. Set $`\hbar=1`$ and measure time in units for which the bulk coherent hopping amplitude is one. The construction uses this qubit Hilbert space throughout; reservoir degrees of freedom are implicit in its Markovian description.

For a jump operator $`L`$, the dissipator convention is

```math
\mathcal D[L](\rho)
=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\}.
```

Trace distance means half the trace norm,

```math
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

The parameter $`\epsilon`$ will denote the stationary GHZ infidelity. The separate parameter $`\delta`$ specifies convergence to the stationary state. All logarithms are natural.

## Generator

Choose $`0<\alpha\le1`$ and real hopping amplitudes

```math
\Omega_1=\alpha,
\qquad
\Omega_j=1\quad(2\le j\le N-1),
\qquad
\Omega_N=(-1)^m\alpha.
```

The final sign fixes the relative phase of the two GHZ components for every even $`N`$. Introduce the boundary scalars $`Z_0=-I`$ and $`Z_{N+1}=I`$, and define

```math
H=\frac12\sum_{j=1}^{N}
\Omega_j X_j(Z_{j+1}-Z_{j-1}).
```

The physical support of this Hamiltonian is explicit in its expansion:

```math
H=
\frac{\Omega_1}{2}X_1+
\frac{\Omega_N}{2}X_N+
\frac12\sum_{j=1}^{N-1}
\left(\Omega_j X_jZ_{j+1}
-\Omega_{j+1}Z_jX_{j+1}\right).
```

Each summand acts on one site or on one nearest-neighbor pair. The two terms involving a flip at site $`j`$ cancel when its neighboring spins agree. When they differ, they generate motion of a domain wall.

There are two families of two-qubit jump operators:

```math
C_j=\sqrt{\eta}\,P_{0,j}s_{j+1},
\qquad j=1,\ldots,N-1,
\qquad \eta=4,
```

```math
J_j=\sqrt{\gamma}\,s_jP_{0,j+1},
\qquad j=1,3,\ldots,N-1,
\qquad \gamma=\frac{4\alpha}{\sqrt N}.
```

On their active pair, $`C_j`$ replaces $`01`$ by $`00`$, while $`J_j`$ replaces $`10`$ by $`00`$. The latter family acts only on bonds with an odd left endpoint. The full time-independent generator is

```math
\mathcal L(\rho)
=-i[H,\rho]
+\sum_{j=1}^{N-1}\mathcal D[C_j](\rho)
+\sum_{r=1}^{m}\mathcal D[J_{2r-1}](\rho).
```

The Hamiltonian coefficients and local dissipative strengths are bounded uniformly in $`N`$ and $`\alpha`$ in the stated range. There are $`N-1`$ cleanup jumps and $`m`$ odd-bond jumps. This is a bounded-local-strength model with a number of terms proportional to $`N`$.

## Monotone domain-wall sector

Define the orthonormal configurations

```math
|j\rangle
=|1\rangle^{\otimes j}|0\rangle^{\otimes(N-j)},
\qquad j=0,\ldots,N,
```

and their span

```math
\mathcal M=\mathrm{span}\{|0\rangle,|1\rangle,\ldots,|N\rangle\}.
```

Here the label $`j`$ records the position of the domain wall. In particular, $`|0\rangle`$ and $`|N\rangle`$ in this notation are the full-chain states $`|0\rangle^{\otimes N}`$ and $`|1\rangle^{\otimes N}`$. Every basis string in $`\mathcal M`$ consists of a block of ones followed by a block of zeros, allowing either block to be empty.

The restriction of the Hamiltonian to this sector is a nearest-neighbor path:

```math
H\big|_{\mathcal M}
=\sum_{j=1}^{N}\Omega_j
\left(|j-1\rangle\langle j|+|j\rangle\langle j-1|\right).
```

The cleanup jumps annihilate the sector, and the odd-bond jumps restrict to

```math
C_j\big|_{\mathcal M}=0,
\qquad
J_{2r-1}\big|_{\mathcal M}
=\sqrt\gamma\,|2r-2\rangle\langle2r-1|,
\qquad r=1,\ldots,m.
```

The Hamiltonian preserves $`\mathcal M`$. Each jump and each operator $`L^\dagger L`$ occurring in the dissipator also preserves this sector. Thus a density operator initially supported on $`\mathcal M`$ remains supported there. The domain-wall encoding and the cleanup jump have precedents in dissipative unary-clock constructions [VWC09]; their role here is described in [related work](../references/related-work.md).

## Exact stationary state

Set

```math
Z_\alpha=2+(m-1)\alpha^2
```

and define

```math
|d_\alpha\rangle
=\frac{1}{\sqrt{Z_\alpha}}
\left(
|0\rangle+|N\rangle+
\alpha\sum_{r=1}^{m-1}(-1)^r|2r\rangle
\right),
\qquad
\rho_\alpha=|d_\alpha\rangle\langle d_\alpha|.
```

All cleanup jumps annihilate $`|d_\alpha\rangle`$ because it lies in $`\mathcal M`$. All odd-bond jumps annihilate it because it has no amplitude on an odd path vertex. The Hamiltonian only couples even and odd vertices. If $`u_{2r}`$ denotes the unnormalized coefficient of $`|2r\rangle`$, its amplitude into the odd vertex $`|2r-1\rangle`$ is

```math
\Omega_{2r-1}u_{2r-2}+\Omega_{2r}u_{2r}=0,
\qquad r=1,\ldots,m.
```

At the left endpoint this identity is $`\alpha-\alpha=0`$. In the interior it follows from the alternating coefficients. At the right endpoint it is

```math
(-1)^{m-1}\alpha+(-1)^m\alpha=0.
```

Consequently,

```math
H|d_\alpha\rangle=0,
\qquad
C_j|d_\alpha\rangle=0,
\qquad
J_{2r-1}|d_\alpha\rangle=0,
\qquad
\mathcal L(\rho_\alpha)=0.
```

The target is therefore an exact pure stationary state of the specified generator. Its approximation concerns the GHZ state, rather than stationarity.

For

```math
|\mathrm{GHZ}_N^+\rangle
=\frac{|0\rangle^{\otimes N}+|1\rangle^{\otimes N}}{\sqrt2},
```

the fidelity is exactly

```math
F_{\mathrm{GHZ}}(\rho_\alpha)
=\langle\mathrm{GHZ}_N^+|\rho_\alpha|\mathrm{GHZ}_N^+\rangle
=\frac{2}{Z_\alpha}.
```

To obtain stationary infidelity $`\epsilon`$, choose

```math
\alpha^2
=\frac{2\epsilon}{(m-1)(1-\epsilon)}
=\frac{4\epsilon}{(N-2)(1-\epsilon)}.
```

Then $`Z_\alpha=2/(1-\epsilon)`$ and $`F_{\mathrm{GHZ}}(\rho_\alpha)=1-\epsilon`$. The uniform convergence theorem uses $`0<\epsilon\le1/8`$, which ensures both $`\alpha\le1`$ and $`\alpha^2m\le1`$.

The endpoint couplings vanish at $`\alpha=0`$. At that value, every density operator supported on the span of the two ferromagnetic configurations is stationary, so the limiting exact GHZ state is not uniquely selected by this construction. This behavior is consistent with the locality obstructions for exact GHZ stabilization discussed in [TV14] and [related work](../references/related-work.md). For every positive $`\alpha`$ in the theorem's range, the [convergence proof](convergence.md) establishes a unique stationary state and attraction from every initial density operator.
