# Uniform convergence from arbitrary initial states

The [model](model.md) has an exact pure stationary state $`\rho_\alpha`$. The argument below proves that this state attracts every input and gives an explicit convergence time. The [cleanup estimate](cleanup.md) first controls population outside the monotone sector. Within that sector, a bound on no-jump survival ensures repeated transfer of population into the dark state.

## Theorem and preparation guarantee

Let $`N=2m\ge4`$ be even and choose a stationary GHZ infidelity $`0<\epsilon\le1/8`$. Set

```math
\alpha^2=\frac{2\epsilon}{(m-1)(1-\epsilon)},
\qquad
Z_\alpha=2+(m-1)\alpha^2,
\qquad
\eta=4,
\qquad
\gamma=\frac{4\alpha}{\sqrt N},
```

and use the Hamiltonian and jump operators in [the model definition](model.md#generator). For every $`0<\delta<1`$, define

```math
T(\delta)=
\frac{N-1}{2}\log\!\left(\frac{2N(N-1)}{\delta^2}\right)
+\frac{4\sqrt N}{\alpha}
\left\lceil
\frac{4Z_\alpha}{\alpha^2}\log\!\left(\frac2\delta\right)
\right\rceil.
```

Then $`\rho_\alpha`$ is the unique stationary density operator. For every initial density operator $`\rho_0`$ on $`(\mathbb C^2)^{\otimes N}`$ and every $`t\ge T(\delta)`$,

```math
D\!\left(e^{t\mathcal L}(\rho_0),\rho_\alpha\right)\le\delta,
\qquad
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

The bound is uniform over the initial state. In the stated parameter range,

```math
T(\delta)
=O\!\left(
N\log\!\frac N\delta+
N^2\epsilon^{-3/2}\log\!\frac2\delta
\right),
```

with constants independent of $`N`$, $`\epsilon`$, and $`\delta`$. The factor $`\log(2/\delta)`$ keeps this expression valid throughout $`0<\delta<1`$, including accuracies close to one.

The stationary GHZ fidelity is $`1-\epsilon`$. Since the GHZ projector is an effect bounded between zero and the identity, trace distance controls the finite-time fidelity directly:

```math
\left|
F_{\mathrm{GHZ}}\!\left(e^{t\mathcal L}(\rho_0)\right)
-(1-\epsilon)
\right|
\le\delta
\qquad(t\ge T(\delta)).
```

In particular, $`F_{\mathrm{GHZ}}(e^{t\mathcal L}(\rho_0))\ge1-\epsilon-\delta`$. The two errors have distinct meanings: $`\epsilon`$ specifies the designed stationary state, while $`\delta`$ accounts for finite preparation time.

## Coupling between even and odd path vertices

Inside $`\mathcal M`$, let

```math
\mathcal E=\mathrm{span}\{|0\rangle,|2\rangle,\ldots,|2m\rangle\},
\qquad
\mathcal O=\mathrm{span}\{|1\rangle,|3\rangle,\ldots,|2m-1\rangle\}.
```

Write $`P_{\mathcal O}`$ for the projector onto the odd vertices. In the decomposition $`\mathcal M=\mathcal E\oplus\mathcal O`$, the restricted Hamiltonian has the block form

```math
H\big|_{\mathcal M}
=\begin{pmatrix}0&B^\dagger\\B&0\end{pmatrix}.
```

Rows of $`B`$ are indexed by $`r=1,\ldots,m`$, and columns by $`k=0,\ldots,m`$. Its only nonzero entries are

```math
B_{r,r-1}=\Omega_{2r-1},
\qquad
B_{r,r}=\Omega_{2r}.
```

Every hopping amplitude is nonzero for $`\alpha>0`$. The equation $`Bu=0`$ therefore determines all even-vertex coefficients from the first one, through the recurrence used to construct $`|d_\alpha\rangle`$. Thus $`B`$ has row rank $`m`$, and its kernel is the one-dimensional span of the even coefficients of $`|d_\alpha\rangle`$.

After conjugating $`BB^\dagger`$ by a diagonal matrix of alternating signs, it becomes

```math
L_{\mathrm{path},m}
+\alpha^2(e_1e_1^\dagger+e_me_m^\dagger),
```

where $`e_r`$ are the standard basis vectors of $`\mathbb C^m`$ and $`L_{\mathrm{path},m}`$ is the ordinary graph Laplacian of a path on $`m`$ vertices. Its quadratic form is

```math
\sum_{r=1}^{m-1}|x_{r+1}-x_r|^2
+\alpha^2(|x_1|^2+|x_m|^2).
```

Writing each $`x_r`$ as $`x_1`$ plus its successive differences and applying Cauchy–Schwarz gives

```math
\|x\|^2
\le2m|x_1|^2+
2m^2\sum_{r=1}^{m-1}|x_{r+1}-x_r|^2.
```

Whenever $`\alpha^2m\le1`$, multiplication by $`\alpha^2/(2m)`$ bounds the right-hand side by the preceding quadratic form. The smallest singular value of $`B`$ therefore satisfies

```math
s_{\min}(B)^2\ge\frac{\alpha^2}{2m}=\frac{\alpha^2}{N}.
```

The assumed infidelity range supplies the required condition:

```math
\alpha^2m
=\frac{2m\epsilon}{(m-1)(1-\epsilon)}
\le\frac{4\epsilon}{1-\epsilon}
\le\frac47<1.
```

## No-jump survival on the orthogonal complement of the dark state

On $`\mathcal M`$, the cleanup jumps vanish and

```math
\sum_{r=1}^{m}J_{2r-1}^\dagger J_{2r-1}
=\gamma P_{\mathcal O}.
```

The no-jump propagator is consequently

```math
K_t=\exp\!\left[t\left(-iH\big|_{\mathcal M}
-\frac\gamma2P_{\mathcal O}\right)\right].
```

Both the generator in this exponential and its adjoint annihilate $`|d_\alpha\rangle`$. Hence $`K_t`$ acts as the identity on the dark state and preserves its orthogonal complement in $`\mathcal M`$. Call this complement the bright subspace.

A singular-value decomposition of $`B`$ splits the bright evolution into $`m`$ two-dimensional blocks. For each singular value $`s>0`$, the block generator is

```math
F_s=\begin{pmatrix}0&-is\\-is&-\gamma/2\end{pmatrix}.
```

Consider the Hermitian matrix

```math
P_s=
\begin{pmatrix}
2/\gamma+\gamma/(4s^2)&-i/(2s)\\
i/(2s)&2/\gamma
\end{pmatrix}.
```

Direct multiplication gives

```math
F_s^\dagger P_s+P_sF_s=-I.
```

The matrix is positive; more precisely, $`P_s\ge I/\gamma`$. Its norm is bounded by its trace,

```math
\|P_s\|\le\mathrm{Tr}P_s
=\frac4\gamma+\frac{\gamma}{4s^2}.
```

For $`u_t=e^{tF_s}u_0`$, the Lyapunov identity gives

```math
\frac{d}{dt}(u_t^\dagger P_su_t)=-\|u_t\|^2.
```

Integration and positivity of $`P_s`$ imply the survival bound

```math
\int_0^\infty\|u_t\|^2\,dt
\le\left(\frac4\gamma+
\frac{\gamma}{4s_{\min}(B)^2}\right)\|u_0\|^2.
```

For the chosen $`\gamma=4\alpha/\sqrt N`$ and the singular-value estimate above,

```math
\frac4\gamma+
\frac{\gamma}{4s_{\min}(B)^2}
\le\frac{2\sqrt N}{\alpha}.
```

The squared survival norm is nonincreasing, since

```math
\frac{d}{dt}\|u_t\|^2
=-\gamma|(u_t)_{\mathcal O}|^2\le0.
```

For any nonincreasing nonnegative function, its value at time $`\tau`$ is at most its integral from zero to $`\tau`$, divided by $`\tau`$. Applying this observation to every block and summing them shows that at

```math
\tau_\alpha=\frac{4\sqrt N}{\alpha},
```

every bright initial vector has no-jump survival probability at most one half:

```math
\|K_{\tau_\alpha}u\|^2\le\frac12\|u\|^2,
\qquad
u\in\mathcal M,\quad
\langle d_\alpha|u\rangle=0.
```

This bound controls the full survival dynamics rather than only the eigenvalues of the Lindblad generator.

## Gain of dark-state population

Let $`\rho_t`$ be supported on $`\mathcal M`$, and set

```math
p(t)=\mathrm{Tr}(\rho_\alpha\rho_t).
```

The Hamiltonian and anticommutator terms make no contribution to its derivative because the target is dark. The jump terms give exactly

```math
p'(t)=\gamma\sum_{r=1}^{m}
|\langle d_\alpha|2r-2\rangle|^2
\langle2r-1|\rho_t|2r-1\rangle.
```

Every summand is nonnegative. Moreover, every jump output has target population at least

```math
f_\alpha=\frac{\alpha^2}{Z_\alpha},
```

because $`\alpha\le1`$ and $`m\ge2`$. The first jump output is the left endpoint and has overlap squared $`1/Z_\alpha`$; all remaining outputs have overlap squared $`\alpha^2/Z_\alpha`$.

In the quantum-jump representation of the same Lindblad evolution, the total jump intensity is $`\gamma\mathrm{Tr}(P_{\mathcal O}\rho_t)`$. Integrating the equation for $`p'(t)`$ therefore bounds the gain in $`p`$ below by $`f_\alpha`$ times the expected number of jumps. The expected number is at least the probability of one or more jumps. This representation is an analytical tool and does not require monitoring or feedback in the preparation.

For an arbitrary initial density operator $`\rho`$ supported on $`\mathcal M`$, let $`p=\mathrm{Tr}(\rho_\alpha\rho)`$. Its probability of no jump during $`\tau_\alpha`$ is

```math
\mathrm{Tr}(K_{\tau_\alpha}\rho K_{\tau_\alpha}^\dagger)
\le p+\frac12(1-p).
```

The dark component survives with probability one, and the bright component with probability at most one half. Cross terms between these orthogonal subspaces have zero trace because $`K_t`$ preserves both subspaces. Thus the probability of at least one jump is at least $`(1-p)/2`$, giving

```math
1-p(t+\tau_\alpha)
\le\left(1-\frac{f_\alpha}{2}\right)[1-p(t)].
```

Iteration yields

```math
1-p(k\tau_\alpha)
\le e^{-k f_\alpha/2},
\qquad k=0,1,2,\ldots.
```

Trace distance to a pure state obeys $`D(\rho_t,\rho_\alpha)\le\sqrt{1-p(t)}`$. Therefore, for $`0<\xi<1`$, a sufficient convergence time within $`\mathcal M`$ is

```math
t_{\mathcal M}(\xi)
=\frac{4\sqrt N}{\alpha}
\left\lceil\frac{4Z_\alpha}{\alpha^2}\log\!\left(\frac1\xi\right)\right\rceil.
```

Every state initially supported on $`\mathcal M`$ is within trace distance $`\xi`$ of $`\rho_\alpha`$ at this time and at all later times. The latter assertion follows from trace-distance contractivity and stationarity of $`\rho_\alpha`$.

## Return to the full Hilbert space

For a general initial state, the [cleanup estimate](cleanup.md#uniform-decay-outside-the-monotone-sector) gives, at

```math
t_0(\delta)
=\frac{N-1}{2}\log\!\left(\frac{2N(N-1)}{\delta^2}\right),
```

the bound

```math
q=\mathrm{Tr}\!\left[(I-\Pi_{\mathcal M})\rho_{t_0}\right]
\le\frac{\delta^2}{4}.
```

Define the normalized comparison state

```math
\sigma_0
=\frac{\Pi_{\mathcal M}\rho_{t_0}\Pi_{\mathcal M}}{1-q}.
```

It is supported on $`\mathcal M`$ and satisfies

```math
D(\rho_{t_0},\sigma_0)\le\sqrt q\le\frac\delta2.
```

To see the first inequality with its stated constant, purify $`\rho_{t_0}`$ and apply $`\Pi_{\mathcal M}`$ to the system part of that purification. After normalization, its overlap with the original purification is $`\sqrt{1-q}`$. The two pure states are therefore at trace distance $`\sqrt q`$, and tracing out the purifying system cannot increase that distance.

Evolve both $`\rho_{t_0}`$ and $`\sigma_0`$ for an additional time $`t_{\mathcal M}(\delta/2)`$. Contractivity keeps their distance at most $`\delta/2`$. Since $`\sigma_0`$ is supported on $`\mathcal M`$, the path estimate also places its evolved state within $`\delta/2`$ of $`\rho_\alpha`$. The triangle inequality gives

```math
D\!\left(
e^{[t_0(\delta)+t_{\mathcal M}(\delta/2)]\mathcal L}(\rho_0),
\rho_\alpha
\right)\le\delta.
```

The sum of these two times is precisely $`T(\delta)`$ in the theorem. Stationarity of the target and contractivity extend the bound to every later time. If another stationary density operator existed, applying the same bound to that state for arbitrarily small $`\delta`$ would force it to equal $`\rho_\alpha`$. This proves uniqueness and global attraction.

Finally, $`Z_\alpha=2/(1-\epsilon)`$ is uniformly bounded in the stated range, and

```math
\alpha^{-2}=\frac{(N-2)(1-\epsilon)}{4\epsilon}.
```

Substitution into the explicit formula for $`T(\delta)`$ gives the stated polynomial bound. All time estimates use the bounded local strengths specified in the model. The argument is a sufficient convergence estimate; it does not establish an optimal mixing exponent.
