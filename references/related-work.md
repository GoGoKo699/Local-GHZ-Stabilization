# Relation to earlier stabilization results

The [model](../science/model.md) uses a time-independent Lindblad generator on an even qubit chain, with one-site and adjacent-pair terms. Its unique pure stationary state approaches a specified GHZ phase, with [polynomial convergence](../science/convergence.md) from every initial state. The [resource assumptions](../science/resources.md) exclude additional system registers, extra local levels, measurement feedback, postselection, and control sequences. Engineered reservoirs remain part of the model. This combination is the relevant comparison; the bibliography is in [references.bib](references.bib).

## Hamiltonian assistance and the limits of generic preparation

Ticozzi and Viola [TV14] give the Hamiltonian-assisted stabilization framework. Corollary 2 relates purely dissipative stabilization to a unique frustration-free parent state; Proposition 3 describes Hamiltonian selection within a larger dark subspace. Their randomized synthesis theorem assumes a stabilizing choice exists, without supplying scalable existence or mixing bounds. Their GHZ results distinguish conditional attraction in a symmetry subspace from global attraction. See Sections II, III, and VI.2 of [arXiv:1304.4270v1](https://arxiv.org/html/1304.4270v1).

Here the common jump kernel contains all even domain-wall positions, a space of dimension $N/2+1$. The Hamiltonian selects one coherent superposition. The explicit selection mechanism and quantitative convergence proof develop this established principle.

Kraus and collaborators [Kraus08] construct Markov processes preparing pure entangled states and give criteria for uniqueness. Conjugating independent damping operators by a preparation unitary gives a general construction, but the resulting jumps need not preserve physical locality. Their matrix-product-state construction inherits the neighborhoods of a suitable frustration-free parent Hamiltonian. The nearest-neighbor AKLT example uses spin-one sites. Neither arbitrary invertible similarity transformations nor a small matrix-product bond dimension alone guarantee two-qubit jump support and polynomial mixing. See Theorems 1–2 and Sections IV and V.3 of [arXiv:0803.1463v3](https://arxiv.org/html/0803.1463v3). These results provide preparation methods and criteria, but do not directly implement the Hamiltonian selection required by this chain.

## The inherited unary cleanup and the change in propagation

Verstraete, Wolf, and Cirac [VWC09] develop dissipative computation and state engineering. Their unary-clock construction includes the adjacent-pair operator

```math
|0\rangle\langle 0|_j\otimes |0\rangle\langle 1|_{j+1}.
```

This is exactly the cleanup jump used here, up to its rate and site labels: it removes a forbidden `01` pattern. The cleanup operator is an inherited ingredient.

The remaining mechanisms differ. Their computational construction has a separate time register and obtains a computational output by reading the clock of a stationary history mixture. Its unary propagation uses three clock sites; its one-dimensional nearest-neighbor universality construction uses twelve-level sites. Here the data qubits themselves support the domain-wall path. Cancellation between adjacent-pair Hamiltonian terms implements coherent propagation, and weak endpoint couplings produce a pure dark state with dominant GHZ endpoints. No clock readout is required.

Their direct matrix-product-state construction assumes an injective state with a suitable unique parent Hamiltonian; grouping sites into larger particles changes physical locality. Its stated convergence bound is $O(N^{\log_2 N})$. See the main text and Appendices I and III of [arXiv:0803.1447v2](https://arxiv.org/html/0803.1447v2). The bibliography uses the published title, which differs from this preprint's longer title.

## Approximate GHZ stabilization

Martin and Sarlette [MS24] are the closest direct comparison. Their constructions stabilize approximate GHZ states using either data qubits accompanied by an ancillary clock chain, or additional levels in the data systems. Remark 1 of their [2023 author preprint, arXiv:2306.05070v1](https://arxiv.org/html/2306.05070v1), explicitly identifies efficient approximate stabilization within the data-qubit Hilbert space alone as an open problem. The present even-chain construction addresses this resource restriction with a pure stationary state and an explicit convergence guarantee.

The version distinction matters: the open-problem attribution is to that author preprint. The [2024 publication](https://doi.org/10.1088/1751-8121/ad52d7) has been bibliographically verified, and its published abstract retains the auxiliary-clock and additional-level architectures. The final article body was not available for this comparison, so no claim is made about its final Remark 1 wording.

Johnson, Ticozzi, and Viola [JTV16] give an earlier approximate-GHZ example within their general theory of frustration-free quantum semigroups. Section 5.4.3 of [arXiv:1506.07756v2](https://arxiv.org/html/1506.07756v2) considers a mixed-state family on four qubits with three-site neighborhoods. It can approach GHZ arbitrarily closely; Remark 8 discusses the closing relaxation gap. This establishes an important approximation precedent, with different system size, interaction support, and rate guarantees.

## Other scalable preparation mechanisms

| Work | Relevant result and resources | Distinction for the present task |
|---|---|---|
| Reiter, Reeb, and Sørensen [RRS16] | Scalable autonomous many-body entanglement preparation, including GHZ, using four-level atoms coupled to two common oscillator modes. | Polynomial autonomous GHZ preparation is established in this enlarged, collective-interaction architecture. The present model restricts the system to a chain of qubits with adjacent-pair terms. |
| Zhou, Choi, and Lukin [ZCL21] | Dissipative matrix-product-state preparation using symmetry, with accelerated segment fusion through quantum feedback. | The GHZ discussion retains both GHZ phases in the dark subspace. The fusion protocol uses the jump record and feedback to track or correct the phase, rather than selecting one phase unconditionally from every initial state. |

For the first comparison, see Eqs. (2)–(5) of [arXiv:1501.06611v2](https://arxiv.org/html/1501.06611v2). For the second, see the noninjective-state discussion in Section V of the [accepted manuscript](https://link.aps.org/accepted/10.1103/PhysRevA.104.032418).

## Scope of the comparison

The contribution is the combination of propagation on data qubits, pair-local Hamiltonian selection, an endpoint-dominated pure state, and polynomial global convergence. The [cleanup proof](../science/cleanup.md) uses the inherited unary cleanup operator. The results concern an ideal generator, without establishing optimal rates, a fixed-noise threshold, a reservoir implementation, or odd-chain preparation. The cited versions bound the comparison; no exhaustive priority claim is made.

## Bibliographic keys

| Label | BibTeX key |
|---|---|
| TV14 | `TicozziViola2014` |
| VWC09 | `VerstraeteWolfCirac2009` |
| Kraus08 | `KrausEtAl2008` |
| MS24 | `MartinSarlette2024` |
| JTV16 | `JohnsonTicozziViola2016` |
| RRS16 | `ReiterReebSorensen2016` |
| ZCL21 | `ZhouChoiLukin2021` |
