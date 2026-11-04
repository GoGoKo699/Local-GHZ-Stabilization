# Thirty milestones for local GHZ stabilization

This map follows the complete scientific argument: local controls create a coherent domain-wall path, dissipation selects a state close to GHZ, and two complementary convergence estimates establish preparation from every initial state. The stable identifiers are **M01–M30**.

There are **12 background/preliminary milestones** and **18 narrative/innovation milestones**. The background moves from individual states and operators to channels, stability, error measures, and the complete preparation task. The narrative has more milestones because stationarity is only the first part of the result: removal of unwanted configurations, convergence within the path, their combination, and physical error accounting each require a distinct connection. Its final milestones integrate the theorem, evidence, resources, and scope.

The single educational anchor is Ángel Rivas and Susana F. Huelga, *Open Quantum Systems: An Introduction*, [arXiv:1104.5242v2, 9 February 2012][RH]. Every **RH section number refers to that author version**. The [source bridge](RIVAS_HUELGA_BRIDGE.md) translates notation and supplies the connections to this project. Anchor pointers identify supporting tools; the linked scientific pages supply the construction and its proofs. This map organizes the understanding targets without reproducing every calculation.

| Phase | Route | Integrating question |
|---|---|---|
| Background and preliminaries | [M01](#m01)–[M12](#m12) | What must a local autonomous generator accomplish, and what would establish that it succeeds? |
| Narrative and innovation | [M13](#m13)–[M30](#m30) | How do the explicit terms produce the target, attract every input, and determine the cost and limitations? |

## Phase I: Background and preliminaries

### M01

**States and observable probabilities**

**Central question.** What information does a density operator retain beyond computational-basis probabilities?

**Understanding target.** Interpret a one-qubit density operator, a projector, and its expectation value. Distinguish a coherent superposition from a mixture with identical basis populations, preparing the distinction between GHZ coherence and ferromagnetic populations.

**Dependencies and story role.** None. Establish the state and observable language used by every later claim.

**Conceptual connection.** Preparation must control the full density operator; a population-only description can miss the target's phase coherence.

**Sources.** [RH §§3 and 4.3][RH]; [model: chain, units, and distance](../science/model.md#chain-units-and-distance); [model: exact stationary state](../science/model.md#exact-stationary-state).

### M02

**Physical support and tensor products**

**Central question.** How is the locality of a control term determined on an entire qubit chain?

**Understanding target.** Identify the sites on which a tensor-product operator acts nontrivially. Distinguish one-site and adjacent-pair support from the spatial extent of the state being prepared, and distinguish physical qubits from scalar boundary conventions.

**Dependencies and story role.** [M01](#m01). Extend individual observables to the physical architecture before examining its dynamics.

**Conceptual connection.** Locality constrains generator terms; it does not require the eventual state or channel to factor across sites.

**Sources.** [RH §§2.1 and 4.2][RH]; [model: generator](../science/model.md#generator); [resources: locality and strength accounting](../science/resources.md#locality-and-strength-accounting).

### M03

**Unconditional quantum channels**

**Central question.** What makes an evolution rule valid for every input state?

**Understanding target.** Explain trace preservation and complete positivity, including the role of an untouched reference system. Distinguish the unconditional state map from a normalized state conditioned on a particular measurement outcome.

**Dependencies and story role.** [M01](#m01), [M02](#m02). Establish the operational meaning of a preparation guarantee that applies to arbitrary density operators.

**Conceptual connection.** The final theorem concerns one deterministic channel at each time, even when a conditional trajectory representation is used to analyze it.

**Sources.** [RH §§4.1–4.2][RH]; [model: chain, units, and distance](../science/model.md#chain-units-and-distance); [convergence: theorem and preparation guarantee](../science/convergence.md#theorem-and-preparation-guarantee).

### M04

**Coherent motion and dissipative transitions**

**Central question.** What do the Hamiltonian and jump operators contribute to a Lindblad generator?

**Understanding target.** Read the commutator, recycling term, and anticommutator in the stated dissipator convention. Explain why a jump amplitude proportional to the square root of a rate produces a dissipative strength proportional to that rate.

**Dependencies and story role.** [M02](#m02), [M03](#m03). Identify the two kinds of local control that the construction combines.

**Conceptual connection.** Hamiltonian interference controls amplitudes, while the jump terms transfer population and preserve the normalization of the unconditional evolution.

**Sources.** [RH §5.2, Theorem 5.1 and Eq. (46)][RH]; [model: generator](../science/model.md#generator).

### M05

**One fixed generator over all times**

**Central question.** What does autonomy mean for the preparation protocol?

**Understanding target.** Interpret the semigroup $`e^{t\mathcal L}`$ and its composition law. Explain why fixed controls can produce evolving states, and why dividing a proof into time intervals does not introduce a physical switching schedule.

**Dependencies and story role.** [M03](#m03), [M04](#m04). Assemble local infinitesimal dynamics into a complete time evolution.

**Conceptual connection.** The same generator performs cleanup and target preparation simultaneously; the proof can analyze successive intervals of that evolution.

**Sources.** [RH §§2.2–2.3 and 4.5][RH]; [model: generator](../science/model.md#generator); [convergence: return to the full Hilbert space](../science/convergence.md#return-to-the-full-hilbert-space).

### M06

**Observables as certificates for all states**

**Central question.** How can an observable inequality control an evolution without knowing its initial state?

**Understanding target.** Interpret the adjoint generator through the derivative of an expectation value. Explain why an operator inequality can be evaluated in every density operator, including states with off-diagonal coherences.

**Dependencies and story role.** [M01](#m01), [M04](#m04), [M05](#m05). Introduce the proof language that will lift local defect removal to the full Hilbert space.

**Conceptual connection.** A quantum Lyapunov observable turns a local dynamical calculation into a uniform bound on unwanted population.

**Sources.** [RH §§2.1 and 5.2][RH] provide operator and generator background; [cleanup: weighted wall observable](../science/cleanup.md#a-weighted-wall-observable) and [dissipative drift](../science/cleanup.md#dissipative-drift) supply the adjoint calculation.

### M07

**Two errors and two distance measures**

**Central question.** How does closeness to the stationary state translate into a useful GHZ preparation guarantee?

**Understanding target.** Distinguish stationary GHZ infidelity $`\epsilon`$ from mixing error $`\delta`$, with trace distance defined as half the trace norm. Explain the different conclusions $`F_{\rm GHZ}\ge1-\epsilon-\delta`$ and distance to ideal GHZ at most $`\sqrt\epsilon+\delta`$.

**Dependencies and story role.** [M01](#m01), [M03](#m03). Define the operational output before discussing stability or rates.

**Conceptual connection.** Designing the limiting state and deciding how long to evolve are separate choices that enter the final accuracy together.

**Sources.** [RH §§2.1 and 4.3][RH]; [resources: accuracy and preparation time](../science/resources.md#accuracy-and-preparation-time).

### M08

**Stationarity, attraction, and preparation time**

**Central question.** What has been established when a candidate state is annihilated by the generator?

**Understanding target.** Distinguish a stationary-state identity, uniqueness, attraction from every input, and a quantitative convergence bound. Recognize that checking a dark vector alone leaves the behavior of other states unresolved.

**Dependencies and story role.** [M04](#m04), [M05](#m05), [M07](#m07). Separate the logical obligations in a stabilization theorem.

**Conceptual connection.** The explicit target is the starting point for the proof; unwanted invariant states and slowly decaying modes must also be controlled.

**Sources.** [RH §5.4, Definition 5.3, Eq. (63), and Theorem 5.4][RH]; [scientific overview: proof structure](../science/README.md#proof-structure).

### M09

**Invariant subspaces and restricted guarantees**

**Central question.** When can a reduced state space faithfully describe part of a larger open-system evolution?

**Understanding target.** Explain the invariance conditions for a subspace under the Hamiltonian, jumps, and dissipator terms. Distinguish a theorem for inputs already in that subspace from a theorem for arbitrary full-system inputs.

**Dependencies and story role.** [M02](#m02), [M04](#m04), [M08](#m08). Prepare the separation between motion along the domain-wall path and attraction toward that path.

**Conceptual connection.** A small invariant sector makes the problem tractable only when a separate argument controls states initially outside it.

**Sources.** [RH §§5.2 and 5.4][RH]; [model: monotone domain-wall sector](../science/model.md#monotone-domain-wall-sector); [convergence: return to the full Hilbert space](../science/convergence.md#return-to-the-full-hilbert-space).

### M10

**Spectral information and norm bounds**

**Central question.** Why does a useful worst-input convergence estimate need more than a list of decay eigenvalues?

**Understanding target.** Distinguish an eigenvalue condition for relaxation from a bound with controlled size-dependent prefactors. Identify the different roles of the Hamiltonian coupling matrix, no-jump propagator, and Lindblad generator.

**Dependencies and story role.** [M05](#m05), [M07](#m07), [M08](#m08). Establish the quantitative standard that the path proof must meet.

**Conceptual connection.** Singular values and a Lyapunov matrix will control actual survival norms, avoiding an inference of the claimed mixing time from a spectral gap alone.

**Sources.** [RH §§2.1–2.2 and 5.4, including its Jordan-block discussion][RH]; [convergence: no-jump survival](../science/convergence.md#no-jump-survival-on-the-orthogonal-complement-of-the-dark-state).

### M11

**Trajectories as an analysis of unconditional dynamics**

**Central question.** How can jumps and no-jump motion describe a preparation that does not monitor a reservoir?

**Understanding target.** Interpret an unnormalized no-jump state and its squared norm as a survival probability. Explain how recycling terms restore the unconditional evolution and why the analysis does not require a recorded outcome or feedback.

**Dependencies and story role.** [M03](#m03), [M04](#m04), [M05](#m05). Connect the channel description to the probability estimates used later.

**Conceptual connection.** A lower bound on the occurrence of a jump can imply progress toward a dark state without selecting a successful trajectory.

**Sources.** [RH §5.2, Eqs. (49)–(50)][RH]; [convergence: no-jump survival](../science/convergence.md#no-jump-survival-on-the-orthogonal-complement-of-the-dark-state) and [gain of dark-state population](../science/convergence.md#gain-of-dark-state-population).

### M12

**The complete stabilization task**

**Central question.** Which simultaneous requirements define the result to be understood?

**Understanding target.** State the task for even $`N\ge4`$, $`0<\epsilon\le1/8`$, and every initial density operator. Combine a specified GHZ phase, pair-local static controls, a unique pure approximate target, polynomial convergence, and the assumption of engineered Markovian reservoirs.

**Dependencies and story role.** [M02](#m02), [M05](#m05), [M07](#m07)–[M11](#m11). Integrate the background into a complete scientific specification.

**Conceptual connection.** Removing a retained controller does not remove the environment or control apparatus; a valid ideal generator and its microscopic realization are different levels of description.

**Sources.** [RH §§5.2–5.4 and 6.2.3, 6.2.6][RH]; [convergence: theorem](../science/convergence.md#theorem-and-preparation-guarantee); [resources: locality and strength accounting](../science/resources.md#locality-and-strength-accounting).

## Phase II: Narrative and innovation

### M13

**Conditional motion from adjacent-pair terms**

**Central question.** How can a spin flip depend on both neighbors while every Hamiltonian term remains two-body?

**Understanding target.** Explain cancellation between the two pair terms involving a given spin. Recover the one-site boundary fields from scalar boundary values, and distinguish locality of the summands from invariance under their coherent sum.

**Dependencies and story role.** [M02](#m02), [M04](#m04), [M12](#m12). Begin the construction with its elementary physical mechanism.

**Conceptual connection.** Interference between allowed terms implements domain-wall motion without introducing a three-site product or an auxiliary boundary qubit.

**Sources.** [RH §§3 and 5.2][RH]; [model: generator](../science/model.md#generator); [resources: locality and strength accounting](../science/resources.md#locality-and-strength-accounting).

### M14

**A preparation path inside the data qubits**

**Central question.** Which configurations turn the many-qubit generator into a simple path problem?

**Understanding target.** Identify the $`N+1`$ monotone configurations with a block of ones followed by zeros. Explain their invariant span, the vanishing of cleanup jumps there, and the reduction of each odd-bond jump to a transition from an odd vertex to the preceding even vertex.

**Dependencies and story role.** [M09](#m09), [M13](#m13). Assemble the local rules into the reduced dynamical system.

**Conceptual connection.** The same physical qubits carry both the target endpoints and the intermediate preparation configurations.

**Sources.** [RH §§5.2 and 5.4][RH]; [model: monotone domain-wall sector](../science/model.md#monotone-domain-wall-sector).

### M15

**Destructive interference selects the target amplitudes**

**Central question.** Why does the stated superposition have no coherent or dissipative escape?

**Understanding target.** Use cancellation into every odd vertex to determine the alternating even-vertex amplitudes. Explain why the final hopping sign $`(-1)^m`$ produces GHZ plus for every even chain length, and why all jumps annihilate the resulting vector.

**Dependencies and story role.** [M04](#m04), [M08](#m08), [M14](#m14). Establish the exact stationary vector before proving attraction.

**Conceptual connection.** A large dissipative dark subspace is reduced by Hamiltonian interference to the desired coherent candidate; the phase is part of the design.

**Sources.** [RH §§5.2 and 5.4, Eq. (63)][RH]; [model: exact stationary state](../science/model.md#exact-stationary-state).

### M16

**Approximation through weak endpoint couplings**

**Central question.** How does the construction approach GHZ without uniquely stabilizing exact GHZ at the endpoint?

**Understanding target.** Relate normalization to $`F_{\rm GHZ}=2/[2+(m-1)\alpha^2]`$ and the chosen positive infidelity. Explain why reducing the interior weight improves the target while $`\alpha=0`$ disconnects the endpoints and admits additional stationary states.

**Dependencies and story role.** [M07](#m07), [M08](#m08), [M15](#m15). Establish both the accuracy mechanism and its singular limit.

**Conceptual connection.** Each positive-error instance is a separate generator; an increasingly accurate family does not imply a uniquely selected exact limit.

**Sources.** [RH §5.4][RH]; [model: exact stationary state](../science/model.md#exact-stationary-state); [resources: scope](../science/resources.md#scope-of-the-construction).

### M17

**A reverse wall carries a distance to the boundary**

**Central question.** What quantity detects progress when cleanup moves a defect without removing it immediately?

**Understanding target.** Interpret $`W=\sum_j(N-j)P_{0,j}P_{1,j+1}`$ as a weighted reverse-wall observable. Explain why its kernel is exactly the monotone sector and why its weights capture progress that an unweighted count can miss.

**Dependencies and story role.** [M06](#m06), [M14](#m14). Introduce the observable that controls the configurations omitted from the path description.

**Conceptual connection.** A local geometric weight converts transport of a defect toward the boundary into a decrease of a global observable.

**Sources.** [RH §§2.1 and 5.1][RH] supply operator and classical-process background; [cleanup: weighted wall observable](../science/cleanup.md#a-weighted-wall-observable) supplies this construction.

### M18

**Cleanup dominates coherent defect motion**

**Central question.** Why does the weighted observable decrease under the full quantum generator?

**Understanding target.** Combine cleanup drift at most $`-4Q`$, nonpositive odd-jump drift, and Hamiltonian drift at most $`2Q`$. Explain why these are operator bounds and therefore survive arbitrary quantum coherences.

**Dependencies and story role.** [M06](#m06), [M13](#m13), [M17](#m17). Turn local transition rules into the decisive full-space differential inequality.

**Conceptual connection.** The proof controls competing coherent and dissipative effects together; classical cleanup trajectories alone would leave part of the dynamics unaccounted for.

**Sources.** [RH §5.2][RH]; [cleanup: dissipative drift](../science/cleanup.md#dissipative-drift), [Hamiltonian drift](../science/cleanup.md#hamiltonian-drift), and [uniform decay](../science/cleanup.md#uniform-decay-outside-the-monotone-sector).

### M19

**Uniform approach to the monotone sector**

**Central question.** What does decreasing defect weight imply for every initial state after a specified time?

**Understanding target.** Connect $`I-\Pi_{\mathcal M}\le W`$ to the exponential leakage bound and the cleanup time $`t_0(\delta)`$. Distinguish a bound on outside population from the trace-distance estimate still needed to control coherences across the sector boundary.

**Dependencies and story role.** [M07](#m07), [M09](#m09), [M18](#m18). Complete the first component of the global proof while identifying its interface with the path argument.

**Conceptual connection.** An observable bound makes a reduced description quantitatively useful without assuming that the initial state lies in it.

**Sources.** [RH §§2.3 and 4.3][RH]; [cleanup: uniform decay](../science/cleanup.md#uniform-decay-outside-the-monotone-sector).

### M20

**One dark mode and coupled bright modes**

**Central question.** Why can no additional even-path superposition avoid coupling to the lossy vertices?

**Understanding target.** Interpret the rectangular even-to-odd coupling matrix $`B`$. Explain how its full row rank leaves one kernel vector and how its singular-value decomposition organizes the remaining motion into paired bright modes.

**Dependencies and story role.** [M10](#m10), [M14](#m14), [M15](#m15). Begin quantitative path convergence by identifying all modes outside the candidate state.

**Conceptual connection.** The recurrence that constructs the target also identifies the unique coherent zero mode; the remaining singular values govern access to dissipation.

**Sources.** [RH §§2.1 and 5.4][RH]; [convergence: coupling between even and odd vertices](../science/convergence.md#coupling-between-even-and-odd-path-vertices).

### M21

**Boundary pinning controls the slowest coupling**

**Central question.** Why can the slowest bright mode be bounded uniformly as the chain grows?

**Understanding target.** Relate $`BB^\dagger`$ to a path Laplacian with endpoint penalties. Explain the bound $`s_{\min}(B)^2\ge\alpha^2/N`$ and the role of the hypothesis $`\alpha^2m\le1`$, supplied by the stated infidelity range.

**Dependencies and story role.** [M16](#m16), [M20](#m20). Convert the geometry of the path into a quantitative scale for every bright mode.

**Conceptual connection.** Small endpoint couplings both concentrate the stationary state and weaken the spectral control available for convergence.

**Sources.** [RH §2.1][RH] supplies operator-norm background; [convergence: coupling between even and odd vertices](../science/convergence.md#coupling-between-even-and-odd-path-vertices) supplies the quadratic-form proof.

### M22

**A survival bound from a two-dimensional Lyapunov equation**

**Central question.** How long can a bright component evolve without a jump?

**Understanding target.** Explain how the positive matrix solving the block Lyapunov equation bounds integrated survival. Relate the two contributions $`4/\gamma`$ and $`\gamma/(4s_{\min}^2)`$ to the choice $`\gamma=4\alpha/\sqrt N`$ and the half-survival interval $`\tau_\alpha=4\sqrt N/\alpha`$.

**Dependencies and story role.** [M10](#m10), [M11](#m11), [M20](#m20), [M21](#m21). Obtain a norm estimate on actual bright dynamics with controlled constants.

**Conceptual connection.** Balancing coherent transfer and loss yields a useful waiting-time bound; increasing the loss rate without regard to coherent motion does not improve this bound indefinitely.

**Sources.** [RH §§2.2 and 5.2, Eqs. (49)–(50)][RH]; [convergence: no-jump survival](../science/convergence.md#no-jump-survival-on-the-orthogonal-complement-of-the-dark-state).

### M23

**Every jump supplies a quantified target overlap**

**Central question.** Why does a jump make progress toward the dark state rather than merely move probability around the path?

**Understanding target.** Interpret the derivative of the dark-state population and its nonnegative terms. Explain the minimum squared overlap $`f_\alpha=\alpha^2/Z_\alpha`$ of any jump output with the target, including the larger overlap at the left endpoint.

**Dependencies and story role.** [M11](#m11), [M15](#m15), [M16](#m16). Supply the capture estimate that complements the survival bound.

**Conceptual connection.** Darkness prevents loss of target population, while the recycling terms replenish it from lossy configurations.

**Sources.** [RH §5.2, Eqs. (46), (49)–(50)][RH]; [convergence: gain of dark-state population](../science/convergence.md#gain-of-dark-state-population).

### M24

**Repeated intervals give convergence on the path**

**Central question.** How do a jump probability and a minimum capture fraction yield a uniform convergence law?

**Understanding target.** Combine half-survival of the bright component with gain per jump to obtain contraction of the population outside the dark state by $`1-f_\alpha/2`$ per interval. Explain why the argument includes mixed inputs and dark–bright coherences, then convert population convergence into trace distance.

**Dependencies and story role.** [M05](#m05), [M07](#m07), [M22](#m22), [M23](#m23). Assemble the complete reduced-sector convergence estimate.

**Conceptual connection.** The semigroup law turns a uniform one-interval progress estimate into a bound for arbitrarily high preparation accuracy.

**Sources.** [RH §§2.3, 4.3, and 5.2][RH]; [convergence: gain of dark-state population](../science/convergence.md#gain-of-dark-state-population).

### M25

**From two estimates to every initial density operator**

**Central question.** How do cleanup and path convergence establish the full theorem without postselection?

**Understanding target.** Explain the normalized projected comparison state, the distance bound $`D\le\sqrt q`$ from leakage population $`q`$, and contractive evolution of both comparison states. Combine the two half-error budgets and infer uniqueness from convergence of every input.

**Dependencies and story role.** [M03](#m03), [M07](#m07), [M08](#m08), [M19](#m19), [M24](#m24). Complete the central global proof.

**Conceptual connection.** Projection and the division into intervals are proof devices; the physical evolution remains continuous under one fixed generator.

**Sources.** [RH §4.3, Theorem 4.4, and §5.4][RH]; [convergence: return to the full Hilbert space](../science/convergence.md#return-to-the-full-hilbert-space).

### M26

**Accuracy, time, and strength budgets**

**Central question.** What physical preparation cost follows when an accuracy and a strength convention are specified?

**Understanding target.** Read the explicit $`T_\epsilon(\delta)`$ and its polynomial scaling, including cleanup and path contributions. Translate to total GHZ infidelity, distinguish bounded local strengths from a fixed total budget, and explain the time rescaling by $`B/\Lambda`$ when the sum budget is fixed.

**Dependencies and story role.** [M07](#m07), [M12](#m12), [M16](#m16), [M25](#m25). Turn the mathematical convergence result into an operational resource statement.

**Conceptual connection.** Simultaneously available local terms and increasingly weak endpoint parameters are part of the cost model behind the time estimate.

**Sources.** [RH §§2.2–2.3][RH]; [convergence: theorem](../science/convergence.md#theorem-and-preparation-guarantee); [resources: accuracy](../science/resources.md#accuracy-and-preparation-time) and [strength accounting](../science/resources.md#locality-and-strength-accounting).

### M27

**Uniform mixing controls perturbations**

**Central question.** What survives when the implemented generator differs slightly from the designed one?

**Understanding target.** Explain how the ideal mixing time at accuracy $`1/8`$ gives a contraction factor $`1/4`$ on Hermitian trace-zero operators. Use the full-system perturbation norm $`\nu`$ and Duhamel comparison to distinguish the stationary-state error bound from the stronger condition $`1/4+\nu T<1`$ ensuring unique perturbed convergence.

**Dependencies and story role.** [M03](#m03), [M07](#m07), [M10](#m10), [M25](#m25). Extend the ideal theorem to a controlled implementation error without assuming the perturbed target remains pure.

**Conceptual connection.** A uniform channel bound supplies quantitative stability information that a gap value alone would not supply here.

**Sources.** [RH §§2.1–2.3 and 4.3][RH]; [resources: uniform perturbation guarantee](../science/resources.md#a-uniform-perturbation-guarantee).

### M28

**Local calibration errors accumulate with system size**

**Central question.** Which local error assumptions actually imply the full-system perturbation bound?

**Understanding target.** Distinguish norms of embedded local errors from a bare local induced norm that need not remain unchanged with spectator systems. Explain the coefficient estimates, accumulation over $`O(N)`$ terms, and sufficient precision scale $`O(\epsilon^{5/2}/N^3)`$ for the stated convention.

**Dependencies and story role.** [M02](#m02), [M03](#m03), [M26](#m26), [M27](#m27). Translate abstract stability into the construction's calibration requirements.

**Conceptual connection.** A sufficient tolerance that shrinks with size and target error establishes controlled finite-instance approximation, without establishing a nonzero noise threshold as the chain grows.

**Sources.** [RH §§2.1 and 4.2–4.3][RH]; [resources: coefficient errors](../science/resources.md#from-coefficient-errors-to-generator-errors) and [scope](../science/resources.md#scope-of-the-construction).

### M29

**Evidence for the complete argument**

**Central question.** How do analytical proofs and finite numerical checks support different parts of the same claim?

**Understanding target.** Connect the independent full-space and path implementations to checks of support, phases, stationary identities, drift inequalities, and contraction. Distinguish matrix inequalities at checked sizes from sampled trajectories, numerical nullity, and the proof for arbitrary even size.

**Dependencies and story role.** [M10](#m10), [M18](#m18), [M21](#m21), [M24](#m24), [M25](#m25). Audit the assembled result through its distinct kinds of evidence.

**Conceptual connection.** Reproducible small instances can expose a wrong boundary sign or normalization, while the symbolic inequalities carry the uniform theorem.

**Sources.** [RH §5.4][RH] provides the spectral background; [verification: what is checked](../verification/README.md#what-is-checked), [parameters and limits](../verification/README.md#parameters-and-limits), and [scientific proof structure](../science/README.md#proof-structure) define the evidence scope.

### M30

**The mechanism, contribution, and limits as one account**

**Central question.** What can this construction establish as a whole, and which stronger conclusions remain outside it?

**Understanding target.** Explain how pair-term interference, an endpoint-weighted dark state, full-space cleanup, and jump-assisted capture combine into unconditional preparation. Relate that combination to the inherited unary cleanup and Hamiltonian-assisted framework. Preserve the even-chain, positive-error, reservoir, strength-budget, and size-dependent perturbation assumptions.

**Dependencies and story role.** [M12](#m12), [M16](#m16), [M25](#m25), [M26](#m26), [M28](#m28), [M29](#m29). Integrate the narrative from its elementary controls to its global scientific meaning.

**Conceptual connection.** The result is a controlled family of pure approximate GHZ steady states with a polynomial worst-input guarantee. Optimal rates, odd-chain extensions, fixed-noise protection, and microscopic reservoir synthesis require additional results.

**Sources.** [RH §§5.4 and 6.2.3, 6.2.6][RH]; [scientific overview](../science/README.md); [resources: scope](../science/resources.md#scope-of-the-construction); [related work](../references/related-work.md).

[RH]: https://arxiv.org/html/1104.5242v2
