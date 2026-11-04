# Scientific account

An open chain of qubits can carry both a target GHZ superposition and the intermediate configurations needed to prepare it. The construction studied here uses a coherent path through monotone domain-wall states, with weak endpoint couplings and loss on alternating intermediate states. Two-qubit cleanup jumps remove configurations outside this path. Every control term is time independent and acts on at most two neighboring qubits.

For every even chain length $`N\geq4`$, the generator has a unique pure stationary state with a specified GHZ infidelity $`\epsilon`$. A direct convergence proof gives a worst-input time polynomial in $`N`$ and $`1/\epsilon`$. This conclusion includes arbitrary initial quantum coherences and uses no retained auxiliary system, feedback or postselection. Engineered Markovian reservoirs remain part of the physical model.

## Reading route

| Page | Question answered |
|---|---|
| [Model and stationary state](model.md) | Which two-body terms are applied, and why is their dark state close to GHZ plus? |
| [Removal of reverse domain walls](cleanup.md) | Why does every initial state approach the monotone subspace? |
| [Convergence along the coherent path](convergence.md) | How do no-jump survival and jump-induced population transfer give a global mixing bound? |
| [Accuracy, resources and perturbations](resources.md) | What is charged, how long does a requested GHZ accuracy take, and what calibration errors are tolerated? |
| [Related work](../references/related-work.md) | Which ingredients are inherited, and which combination is established here? |
| [Numerical verification](../verification/README.md) | How can the finite-size identities and stationary-state checks be reproduced? |

## Proof structure

The target is annihilated by every jump, and its amplitudes cancel all Hamiltonian transitions into odd path vertices. Stationarity follows directly. Global attraction requires two further arguments.

First, a weighted count of reverse domain walls decreases under the full quantum evolution. Its zero eigenspace is exactly the monotone path subspace. This operator inequality bounds leakage for arbitrary density operators, including states with coherences between legal and illegal configurations.

Second, the path Hamiltonian has a unique zero mode on its even vertices. A pinned-path singular-value bound controls all remaining modes. An explicit two-dimensional Lyapunov equation bounds their no-jump survival, while every jump deposits a quantified amount of population in the dark state. Combining these bounds gives exponential contraction over intervals of polynomial duration. Projection and trace-distance contractivity join the two parts into a uniform full-space mixing theorem.

The perturbation estimates use that uniform mixing statement, rather than a dissipative spectral gap alone. The numerical checks reproduce finite instances of the operator identities; the analytical argument supplies the arbitrary-size guarantee.
