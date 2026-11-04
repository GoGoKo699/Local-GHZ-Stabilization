# Local GHZ Stabilization

**Autonomous approximate GHZ preparation on a chain of physical qubits using nearest-neighbor two-body dynamics.**

The system consists of an even number $N\geq4$ of qubits with fixed local Hamiltonian terms and engineered dissipative jumps. From every initial density operator, the evolution converges to a unique pure state with tunable GHZ-plus fidelity. Intermediate domain-wall configurations of the data qubits provide the coherent preparation path, so the model requires no retained clock register or additional on-site level.

## Principal result

Let $N=2m$ and choose $0<\epsilon\leq1/8$. The explicit stationary state has fidelity

$$
F_{\rm GHZ}=\frac{2}{2+(m-1)\alpha^2}=1-\epsilon,
\qquad
\alpha^2=\frac{2\epsilon}{(m-1)(1-\epsilon)}.
$$

With bounded local strengths, a sufficient worst-input time to trace distance $\delta$ from that stationary state is

$$
t_{\rm mix}(\delta)
=O\!\left(
N\log\frac{N}{\delta}
+N^2\epsilon^{-3/2}\log\frac{2}{\delta}
\right),
\qquad 0<\delta<1.
$$

Here trace distance means one half of the trace norm. At that time the GHZ fidelity is at least $1-\epsilon-\delta$. The [convergence proof](science/convergence.md) gives the full constants and establishes convergence for arbitrary initial coherences. The sum of local strengths is $O(N)$; the [resource account](science/resources.md) gives the conversion for a fixed total strength budget and a conservative perturbation guarantee.

## Read the result

| Goal | Route |
|---|---|
| Understand the mechanism | [Scientific overview](science/README.md) and [explicit model](science/model.md) |
| Check the proof | [Full-space cleanup](science/cleanup.md), then [path convergence](science/convergence.md) |
| Assess physical assumptions | [Accuracy, resources and perturbations](science/resources.md) |
| Compare prior constructions | [Related work](references/related-work.md) and [bibliography](references/references.bib) |
| Reproduce finite-size checks | [Verification instructions](verification/README.md) |

## Scope

The theorem concerns even chains and a specified Markovian generator whose controls act on at most two neighboring qubits. Preparation is unconditional and time independent. The reservoir model is assumed; a microscopic implementation must supply the corresponding dissipation and coherent controls. The polynomial mixing estimate is conservative. The perturbation guarantee requires errors that decrease with system size and does not establish protection at a fixed nonzero local noise rate.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
