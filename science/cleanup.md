# Removal of reverse domain walls

The [generator](model.md) preserves the monotone sector $\mathcal M$, but preparation must also succeed when the initial state has support outside it. A reverse domain wall, the substring $01$, identifies a nonmonotone basis configuration. A weighted count of these walls gives an operator inequality that controls their removal in the presence of the Hamiltonian.

The cleanup operator $P_{0,j}s_{j+1}$ also appears in the dissipative unary-clock construction of [VWC09], Appendix I. The argument below bounds its action together with the coherent terms and the odd-bond jumps. Attribution and the comparison of models are given in [related work](../references/related-work.md).

## A weighted wall observable

Let $\Pi_{\mathcal M}$ be the orthogonal projector onto $\mathcal M$, and define

$$
q_j=P_{0,j}P_{1,j+1},
\qquad
Q=\sum_{j=1}^{N-1}q_j,
\qquad
W=\sum_{j=1}^{N-1}(N-j)q_j.
$$

The operator $Q$ counts reverse walls. In $W$, a wall carries a weight equal to its distance from the right boundary. Moving a wall one site to the right therefore reduces $W$ by one, even when the number of walls does not change.

These observables are diagonal in the computational basis. Their common zero eigenspace is exactly $\mathcal M$, since a bit string with no $01$ substring consists of ones followed by zeros. Every nonzero eigenvalue of $W$ is at least one, and every wall weight is at most $N-1$. Thus

$$
I-\Pi_{\mathcal M}\le W\le(N-1)Q,
\qquad
W\le\frac{N(N-1)}2 I.
$$

All inequalities on this page are operator inequalities. They can therefore be evaluated in an arbitrary density operator, including one with coherences between different bit strings.

## Dissipative drift

For an observable $A$, the adjoint dissipator is

$$
\mathcal D[L]^\dagger(A)
=L^\dagger A L-\frac12\{L^\dagger L,A\}.
$$

The cleanup jump $C_j$ replaces $01$ on sites $j,j+1$ by $00$. If the following bit is one, the reverse wall moves from bond $j$ to bond $j+1$. If the following bit is zero, that wall disappears. Since $W$ is diagonal, these changes give the exact identity

$$
\mathcal D[C_j]^\dagger(W)
=-4q_j\left[1+(N-j-1)P_{0,j+2}\right]
\le-4q_j.
$$

For $j=N-1$, the term containing the virtual site $N+1$ has zero coefficient. It can be read with $P_{0,N+1}=I$.

The odd-bond jump $J_j$ replaces $10$ by $00$. This does not create a reverse wall. Its only possible change in $W$ is to remove a reverse wall immediately to its left. With the convention $q_0=0$, its adjoint action is

$$
\mathcal D[J_j]^\dagger(W)
=-\gamma(N-j+1)q_{j-1}P_{0,j+1}
\le0,
\qquad j=1,3,\ldots,N-1.
$$

The formula also gives zero at $j=1$, where there is no preceding bond. Summing the dissipative contributions therefore yields

$$
\sum_{j=1}^{N-1}\mathcal D[C_j]^\dagger(W)
+\sum_{r=1}^{m}\mathcal D[J_{2r-1}]^\dagger(W)
\le-4Q.
$$

## Hamiltonian drift

The Hamiltonian flips site $j$ only when its neighbors differ. In the local sector with neighboring bits $1,0$, the flip moves a monotone wall and leaves $W$ unchanged. In the sector with neighboring bits $0,1$, it interchanges $001$ and $011$. Their weights differ by one.

Define the projector onto the latter neighboring configuration by

$$
R_j=P_{0,j-1}P_{1,j+1}.
$$

The boundary conventions of the model give $P_{0,0}=0$ and $P_{1,N+1}=0$, so $R_1=R_N=0$. A direct commutator calculation gives

$$
i[H,W]=\sum_{j=1}^{N}\Omega_j R_jY_j.
$$

The projector $R_j$ commutes with $Y_j$. Hence $\Omega_jR_jY_j\le|\Omega_j|R_j$. With $q_N=0$ as well as $q_0=0$,

$$
R_j\le q_{j-1}+q_j.
$$

Indeed, when the neighbors are $0,1$, either value of the middle bit places a reverse wall on one of the two adjacent bonds. Since $|\Omega_j|\le1$, summing these bounds gives

$$
i[H,W]\le\sum_{j=1}^{N}R_j\le2Q.
$$

The Hamiltonian can therefore increase the weighted wall observable at a rate bounded by $2Q$, while cleanup removes it at a rate of at least $4Q$.

## Uniform decay outside the monotone sector

Combining the two drift estimates gives

$$
\mathcal L^\dagger(W)
\le-2Q
\le-\frac{2}{N-1}W.
$$

Let $\rho_t=e^{t\mathcal L}(\rho_0)$ for any initial density operator $\rho_0$. Taking expectations and integrating the differential inequality yields

$$
\operatorname{Tr}(W\rho_t)
\le e^{-2t/(N-1)}\operatorname{Tr}(W\rho_0).
$$

The population outside $\mathcal M$ therefore obeys

$$
\operatorname{Tr}\!\left[(I-\Pi_{\mathcal M})\rho_t\right]
\le\frac{N(N-1)}2e^{-2t/(N-1)}.
$$

This estimate holds uniformly over all initial states. It does not require the initial density operator to be diagonal or the evolution to follow a classical sequence of wall moves.

For a desired mixing accuracy $0<\delta<1$, define

$$
t_0(\delta)
=\frac{N-1}{2}
\log\!\left(\frac{2N(N-1)}{\delta^2}\right).
$$

At every $t\ge t_0(\delta)$, the population outside $\mathcal M$ is at most $\delta^2/4$. The [convergence proof](convergence.md#return-to-the-full-hilbert-space) converts this population bound into trace distance at most $\delta/2$ from a comparison state supported on $\mathcal M$. That projection is used only in the proof; the physical preparation is the continuous evolution generated by $\mathcal L$.
