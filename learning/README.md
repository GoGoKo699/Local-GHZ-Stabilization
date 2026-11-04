# Learning the construction

The physical task is to prepare a coherent GHZ superposition on an open qubit chain using fixed local Hamiltonian terms and dissipation. The intermediate configurations needed for preparation are states of the same qubits that form the output. Understanding the construction requires both its interference mechanism and the argument that every initial state reaches the selected stationary state.

The educational anchor is Ángel Rivas and Susana F. Huelga, *Open Quantum Systems: An Introduction* (2012). All source locators in this learning route refer to the [author version arXiv:1104.5242v2](https://arxiv.org/html/1104.5242v2), dated 9 February 2012. The [bibliography](../references/references.bib) records the book and version under `RivasHuelga2012`.

## Reading routes

| Starting point | Route |
|---|---|
| See the mechanism in a small system | Read the [four-qubit example](RIVAS_HUELGA_BRIDGE.md#a-complete-four-qubit-example), including its exact stationary state and preparation bound. |
| Connect open-system foundations to the construction | Follow the [Rivas–Huelga bridge](RIVAS_HUELGA_BRIDGE.md), which maps notation and identifies the proof ingredients supplied by this project. |
| Follow the conceptual dependencies | Use the [30-milestone map](MILESTONES.md), from local prerequisites to the global preparation guarantee and its scope. |
| Read the exact scientific argument | Start from the [scientific account](../science/README.md), then follow the model, cleanup, convergence, and resource pages. |
| Check the numerical implementation | Use the [verification instructions](../verification/README.md), alongside the analytical statements that each finite check addresses. |

The bridge supplies a focused explanation of the construction; the milestone map organizes its understanding targets and dependencies. The canonical science pages contain the full statements and proofs. Primary research references in [related work](../references/related-work.md) provide attribution and model comparisons alongside the single educational anchor.

## The distinctions that organize the argument

The designed state is exactly stationary and only approximately GHZ. Its stationary infidelity $`\epsilon`$ determines the generator, while the mixing accuracy $`\delta`$ determines how long that generator runs. A state annihilated by every jump still requires a global-attraction proof. Locality refers to the physical qubits and the actual Hamiltonian and jump terms, while the smaller domain-wall path is a subspace used to analyze them.

The learning route retains these distinctions through the example, the proof, and the resource discussion. In particular, engineered reservoirs remain part of the effective physical model, and the perturbation guarantee requires errors small enough for the stated norm and time scale.
