# Project understanding map: 30 milestones

This map organizes the scientific story of universal entanglement readout into exactly **30 milestones**. It is defined by the project and is common to every reader, including an LLM. Its targets and order do not depend on a particular reader's prior knowledge.

The allocation is **12 background/preliminaries milestones** and **18 narrative/innovation milestones**. The background connects quantum states and measurements to the analytic, algebraic, and statistical tools that the project needs. The narrative has more room because the physical corner, outcome constructions, binary rigidity, repetition bound, and promise-gap alternative must each become understandable before they can be joined into one resource account.

The single educational anchor is John Watrous's *The Theory of Quantum Information*. The [Watrous bridge](WATROUS_BRIDGE.md) owns the source version, section mapping, notation translation, and locally supplied steps. It provides a targeted route into the work. The scientific pages linked below remain authoritative for exact statements and complete proofs.

Each milestone gives a central question, an understanding target, earlier prerequisites, a conceptual connection and direct source pointers. The connections identify interpretations and distinctions that make the target useful in the scientific argument. Together the milestones support global understanding of the project, while specialist calculations remain in the proof files.

## Route through the project

| Phase | Milestones | Connection established |
|---|---|---|
| Background/preliminaries | [M01](#m01-states-and-independent-copies)–[M04](#m04-marginal-rank-and-physical-support) | Physical states, separability, partial transpose, and rank promises |
| Background/preliminaries | [M05](#m05-a-fixed-povm-and-its-complete-record)–[M08](#m08-distance-and-witness-certificates) | Retained data, collective observables, and distance from separability |
| Background/preliminaries | [M09](#m09-analytic-geometry-of-a-scalar-image)–[M12](#m12-the-complete-operational-question) | Local geometry, polynomial identities, and statistical evidence within the complete model |
| Narrative/innovation | [M13](#m13-a-physical-corner-with-two-entangling-directions)–[M20](#m20-the-attained-outcome-hierarchy) | Physical obstructions and explicit measurements establish R1 |
| Narrative/innovation | [M21](#m21-a-constant-probability-on-the-two-qubit-boundary)–[M23](#m23-a-feasible-and-normalized-binary-detector) | Boundary geometry establishes R2 and its four-copy realization |
| Narrative/innovation | [M24](#m24-weak-entanglement-and-fourth-order-sensitivity)–[M26](#m26-the-sharp-statistical-law-and-its-comparison) | Sensitivity and information establish R3 |
| Narrative/innovation | [M27](#m27-the-block-size-cost-of-a-promise-gap)–[M28](#m28-a-binary-filter-attaining-the-logarithmic-block-size) | A relaxed task gives the supporting block-size law S1 |
| Narrative/innovation | [M29](#m29-attribution-and-the-strength-of-the-evidence)–[M30](#m30-the-complete-scientific-story) | Attribution, verification, and resource distinctions support the full scientific account |

## Phase I: background/preliminaries

### M01 States and independent copies

**Central question.** What physical input does one run of the apparatus receive?

**Understanding target.** Interpret a positive trace-one operator as the unknown bipartite state and $`\rho^{\otimes k}`$ as $`k`$ independent preparations of that same state. Distinguish the local tensor factors $`A,B`$ from the tensor factors indexing repeated copies. This fixes the objects on which every later measurement acts.

**Prerequisites.** None within this map.

**Conceptual connection.** Recognize when correlations between nominal copies would invalidate the tensor-power probability formula, and distinguish increasing a local dimension from increasing the number of copies.

**Canonical sources.** [States and partial transpose](../science/model.md#states-partial-transpose-and-distance); [one fixed collective apparatus](../science/model.md#one-fixed-collective-apparatus).

### M02 Separable states as a convex set

**Central question.** How can the physical definition of separability constrain a measured scalar?

**Understanding target.** Interpret separable states as mixtures of product states. Connect convexity, compactness, and connectedness of this set to the fact that a continuous scalar has an interval as its separable image. Distinguish a mixture of product states from a product state itself.

**Prerequisites.** [M01](#m01-states-and-independent-copies).

**Conceptual connection.** Infer why a scalar classifier must keep every entangled value outside the entire separable interval, even if the classical classifier is allowed an arbitrary decision rule.

**Canonical sources.** [State domain](../science/model.md#states-partial-transpose-and-distance); [the image of the separable set](../science/binary_rigidity.md#31-the-image-of-the-separable-set).

### M03 Partial transpose and the dimension boundary

**Central question.** When does a spectral test decide separability?

**Understanding target.** Define partial transpose on one local subsystem and interpret its negative eigenvalues as entanglement certificates. Know the precise imported equivalence between positive partial transpose and separability in $`2\times2`$ and $`2\times3`$. Relate this dimensional restriction to the project's use of matrix spectra.

**Prerequisites.** [M01](#m01-states-and-independent-copies), [M02](#m02-separable-states-as-a-convex-set).

**Conceptual connection.** Identify which direction of the PPT implication survives in larger dimensions and why a formula involving $`\rho^\Gamma`$ does not instruct an experiment to apply partial transpose physically.

**Canonical sources.** [States, partial transpose, and distance](../science/model.md#states-partial-transpose-and-distance); [PPT source attribution](../references/RELATED_WORK.md#peres1996-and-ppt1996); [fixed linear maps](../science/collective_measurements.md#tensor-factors-and-fixed-linear-maps).

### M04 Marginal rank and physical support

**Central question.** What changes when the qutrit marginal loses rank?

**Understanding target.** Distinguish global rank, partial-transpose rank, and marginal rank. Understand why $`B=\mathrm{Tr}_A\rho\gt0`$ is weaker than full rank of $`\rho`$, and why positivity confines $`\rho`$ to $`A\otimes\mathrm{supp}B`$ when $`B`$ is singular. This identifies a physically meaningful boundary of the state domain.

**Prerequisites.** [M01](#m01-states-and-independent-copies), [M03](#m03-partial-transpose-and-the-dimension-boundary).

**Conceptual connection.** Recognize that a rank-two qutrit marginal leaves a two-qubit support, whereas a rank-one marginal forces a product state; avoid replacing an invertible-marginal promise with a global full-rank promise.

**Canonical sources.** [Rank promises in the model](../science/model.md#states-partial-transpose-and-distance); [singular qutrit marginal](../science/outcome_minima.md#singular-qutrit-marginal).

### M05 A fixed POVM and its complete record

**Central question.** What information is actually retained from the apparatus?

**Understanding target.** Interpret $`p_j(\rho)=\mathrm{Tr}(E_j\rho^{\otimes k})`$ for one fixed state-independent POVM. A run emits one of $`m`$ labels; its complete probability vector is determined by $`m-1`$ coordinates. Absorb fixed ancillas and internal operations into the effects while counting every retained setting, intermediate record, or postselection label.

**Prerequisites.** [M01](#m01-states-and-independent-copies), [M02](#m02-separable-states-as-a-convex-set).

**Conceptual connection.** Detect when a claimed binary protocol actually retains additional information, and distinguish one observed bit from its exactly known probability.

**Canonical sources.** [One fixed collective apparatus](../science/model.md#one-fixed-collective-apparatus); [resource accounting](../science/model.md#what-each-resource-measures).

### M06 Polynomial degree and collective realization

**Central question.** Why can copy count be studied through polynomial functions?

**Understanding target.** Connect tensor-product factorization to a real probability polynomial of degree at most $`k`$ on trace-one Hermitian coordinates. Understand the converse construction: represent each monomial by a Hermitian tensor observable, pad lower degrees with identities, then use a certified norm bound to shift and rescale observables into POVM effects.

**Prerequisites.** [M01](#m01-states-and-independent-copies), [M05](#m05-a-fixed-povm-and-its-complete-record).

**Conceptual connection.** Distinguish a polynomial statistic, its implementing observable, and a valid probability. Explain why finite-degree realization establishes existence without a useful sample margin or efficient circuit.

**Canonical sources.** [Polynomial form of a fixed detector](../science/outcome_minima.md#polynomial-form-of-a-fixed-detector); [general polynomial-to-observable lemma](../science/collective_measurements.md#general-polynomial-to-observable-lemma); [representation attribution](../references/RELATED_WORK.md#brun2004-and-leifer2004).

### M07 Spectral coefficients and antisymmetric observables

**Central question.** How do eigenvalue conditions become fixed collective observables?

**Understanding target.** Relate elementary symmetric coefficients $`e_r(X)`$ to the spectrum of a Hermitian matrix and to $`\mathrm{Tr}(A_rX^{\otimes r})`$, where $`A_r`$ is the normalized antisymmetric projector. Connect determinant degree, characteristic coefficients, and the derivative of a determinant to their copy requirements. Keep observable norm bounds distinct from bounds on selected expectations.

**Prerequisites.** [M01](#m01-states-and-independent-copies), [M03](#m03-partial-transpose-and-the-dimension-boundary), [M06](#m06-polynomial-degree-and-collective-realization).

**Conceptual connection.** Infer why a degree-four statistic can share a six-copy block through identity padding, and why differentiating a six-factor determinant contraction produces six contributions.

**Canonical sources.** [Antisymmetric projectors and normalization](../science/collective_measurements.md#antisymmetric-projectors-and-normalization); [explicit six-copy observables](../science/collective_measurements.md#explicit-six-copy-observables); [characteristic coefficients](../science/promise_gap.md#3-a-characteristic-coefficient-gap).

### M08 Distance and witness certificates

**Central question.** How is a quantitative entanglement promise certified?

**Understanding target.** Use the half-trace distance $`\Delta(\rho)=\inf_{\sigma\in\mathrm{SEP}}\Vert\rho-\sigma\Vert_1/2`$. A concrete separable approximation gives an upper bound; an entanglement witness with a controlled operator norm gives a lower bound through trace-norm duality. Equality requires matching both arguments.

**Prerequisites.** [M02](#m02-separable-states-as-a-convex-set), [M03](#m03-partial-transpose-and-the-dimension-boundary).

**Conceptual connection.** Distinguish a negative partial-transpose eigenvalue from the claimed distance value, and recognize why a statistical comparator need not be the closest separable state.

**Canonical sources.** [Distance convention](../science/model.md#states-partial-transpose-and-distance); [direct trace-distance comparison](../science/sampling_cost.md#21-a-direct-comparison-with-trace-distance); [a family with exact distance](../science/sampling_cost.md#22-a-family-attaining-the-fourth-power).

### M09 Analytic geometry of a scalar image

**Central question.** How can local boundary geometry defeat arbitrary scalar postprocessing?

**Understanding target.** Combine a connected scalar image with continuity near a class boundary. Understand why boundary values can be forced to an interval endpoint, why connectedness then forces constancy, and why real analyticity extends constancy along a line. Interpret the implicit function theorem as a way to hold a statistic fixed using a nonzero tangent derivative.

**Prerequisites.** [M02](#m02-separable-states-as-a-convex-set), [M06](#m06-polynomial-degree-and-collective-realization).

**Conceptual connection.** Separate assumptions on the continuous analytic statistic from assumptions on the unrestricted decision map, and identify which step would fail if only continuity were available.

**Canonical sources.** [Scalar quadrant lemma](../science/outcome_minima.md#lemma-1-no-analytic-scalar-classifies-a-quadrant); [tangent constancy argument](../science/outcome_minima.md#lemma-2-constancy-on-the-physical-rank-four-stratum).

### M10 Polynomial identities beyond a physical patch

**Central question.** When can a local identity constrain distant states?

**Understanding target.** Distinguish two continuation mechanisms used in the project. A rank factorization and trace homogenization turn vanishing on an open physical patch into a polynomial identity on an entire rank locus. A smooth real patch of an irreducible determinant hypersurface instead yields divisibility by the determinant. Understand the roles of complexification, full degree on the trace-one space, and irreducibility in those arguments.

**Prerequisites.** [M06](#m06-polynomial-degree-and-collective-realization), [M09](#m09-analytic-geometry-of-a-scalar-image).

**Conceptual connection.** Recognize why a finite list of zero evaluations is insufficient, and why irreducibility cannot simply be presumed after an arbitrary affine restriction.

**Canonical sources.** [Rank-four polynomial continuation](../science/outcome_minima.md#lemma-3-polynomial-continuation-to-all-matrices-of-rank-at-most-four); [irreducibility on the trace-one space](../science/binary_rigidity.md#4-irreducibility-and-continuation-on-the-trace-one-space).

### M11 Probability gaps and statistical evidence

**Central question.** How does a small probability separation turn into many repetitions?

**Understanding target.** Interpret an empirical frequency as an estimate of a binary probability. Connect a threshold separated from both hypotheses to a concentration upper bound. Connect the relative entropy between two outcome laws, its addition over independent runs, and data processing at the final decision to a lower bound with a confidence factor.

**Prerequisites.** [M05](#m05-a-fixed-povm-and-its-complete-record), [M08](#m08-distance-and-witness-certificates).

**Conceptual connection.** Recognize the different roles of a worst-case hard pair and a test valid on entire promised classes. Explain why changing the rare-outcome probability requires controlling the divergence denominator as well as the probability difference.

**Canonical sources.** [Statistical model](../science/sampling_cost.md#1-statistical-model-and-minimax-statement); [information-theoretic lower bound](../science/sampling_cost.md#4-information-theoretic-lower-bound); [frequency-threshold upper bound](../science/sampling_cost.md#5-matching-four-copy-upper-bound).

### M12 The complete operational question

**Central question.** Which experiment and which resource does each theorem describe?

**Understanding target.** Assemble the background into the full model: unknown iid mixed states, one fixed collective apparatus, complete retained outcomes, and an exact decision map. Separate outcomes $`m`$, block size $`k`$, repetitions $`n`$, probability precision, and implementation complexity. Locate the different quantifiers of exact universality, universal apparatuses used for a promised statistical task, and apparatuses designed only for that promise.

**Prerequisites.** [M04](#m04-marginal-rank-and-physical-support), [M07](#m07-spectral-coefficients-and-antisymmetric-observables), [M10](#m10-polynomial-identities-beyond-a-physical-patch), [M11](#m11-probability-gaps-and-statistical-evidence).

**Conceptual connection.** Assign a proposed protocol to the correct task and identify which model assumption is changed by a purity promise, a growing block, a retained setting label, or a marginal estimated before selecting a detector.

**Canonical sources.** [Model and exact claims](../science/model.md); [what each resource measures](../science/model.md#what-each-resource-measures).

## Phase II: narrative/innovation

### M13 A physical corner with two entangling directions

**Central question.** Can a two-coordinate corner be realized by physical density operators?

**Understanding target.** Follow the construction of a full-rank separable seed whose partial transpose is positive of rank four. Perturb its two kernel directions while preserving positivity of the original state. On the resulting physical square, the two selected partial-transpose eigenvalues are $`s,t`$, so separability is exactly $`s,t\ge0`$.

**Prerequisites.** [M03](#m03-partial-transpose-and-the-dimension-boundary), [M04](#m04-marginal-rank-and-physical-support), [M07](#m07-spectral-coefficients-and-antisymmetric-observables), [M12](#m12-the-complete-operational-question).

**Conceptual connection.** Explain why a rank-deficient partial transpose is compatible with a full-rank physical state and why the construction already lies inside the invertible-marginal domain.

**Canonical sources.** [Full-rank physical seed](../science/outcome_minima.md#a-full-rank-physical-seed); [physical quadrant](../science/outcome_minima.md#a-physical-quadrant).

### M14 Why one scalar cannot classify the corner

**Central question.** Why does the physical corner exclude every fixed binary detector?

**Understanding target.** Apply the interval-endpoint argument to the positive quadrant. Follow connectedness along a positive boundary ray and analytic continuation to its negative extension, where a separable and an entangled input acquire the same value. Use only the disjointness required of probability images.

**Prerequisites.** [M09](#m09-analytic-geometry-of-a-scalar-image), [M13](#m13-a-physical-corner-with-two-entangling-directions).

**Conceptual connection.** Explain why extra finite copies or a discontinuous classical decision map cannot remove this scalar collision, and why the result excludes two outcomes even under the full-rank promise.

**Canonical sources.** [Scalar quadrant lemma](../science/outcome_minima.md#lemma-1-no-analytic-scalar-classifies-a-quadrant); [physical application](../science/outcome_minima.md#a-physical-quadrant).

### M15 Why two statistics must become locally constant

**Central question.** What prevents a second statistic from using tangent information to resolve the corner?

**Understanding target.** Use a Schur-complement chart around the physical rank-four partial-transpose stratum. A nonzero tangent derivative would let the implicit function theorem keep one statistic constant while leaving a two-dimensional diagonal normal slice with the quadrant criterion. The other statistic would then be an impossible scalar classifier.

**Prerequisites.** [M09](#m09-analytic-geometry-of-a-scalar-image), [M14](#m14-why-one-scalar-cannot-classify-the-corner).

**Conceptual connection.** Identify the contradiction that forces both statistics to be constant on a connected open stratum patch. Distinguish the two-dimensional slice used in the proof from the full normal space of the rank-four stratum.

**Canonical sources.** [Constancy on the physical rank-four stratum](../science/outcome_minima.md#lemma-2-constancy-on-the-physical-rank-four-stratum).

### M16 The singular state reached by continuation

**Central question.** How does local constancy rule out two coordinates on the whole state space?

**Understanding target.** Follow trace homogenization, the factorization $`X=YY^\dagger`$, and complexification to independent factors $`YZ^T`$. The identity extends to trace-one Hermitian matrices of rank at most four in partial-transpose coordinates. An embedded Bell state therefore receives the same pair as a separable patch.

**Prerequisites.** [M10](#m10-polynomial-identities-beyond-a-physical-patch), [M15](#m15-why-two-statistics-must-become-locally-constant).

**Conceptual connection.** Explain why the Bell state's singular qutrit marginal matters: it completes the unrestricted lower bound while remaining outside the invertible-marginal promise. Translate the two-coordinate obstruction into a requirement of at least four outcomes.

**Canonical sources.** [Polynomial continuation](../science/outcome_minima.md#lemma-3-polynomial-continuation-to-all-matrices-of-rank-at-most-four); [completion of the lower bound](../science/outcome_minima.md#completion-of-the-lower-bound).

### M17 Two statistics under an invertible marginal

**Central question.** Which fixed polynomials suffice when the qutrit marginal is invertible?

**Understanding target.** Relate $`H=I_2\otimes B-\rho`$ to the partial transpose. Introduce $`f=\det H`$ and $`g=\mathrm{Tr}[D\mathrm{adj}(H)]`$, with $`D=I_2\otimes B`$. In the proof, whitening gives $`K\le I`$ and $`\mathrm{Tr}K=3`$; these restrictions on inertia make $`f`$ and the weighted coefficient $`g=(\det B)^2e_5(K)`$ sufficient.

**Prerequisites.** [M04](#m04-marginal-rank-and-physical-support), [M07](#m07-spectral-coefficients-and-antisymmetric-observables), [M12](#m12-the-complete-operational-question).

**Conceptual connection.** Interpret the sign branches, including an entangled state with $`f\gt0,g=0`$, and explain why whitening is a proof operation that supplies no hidden state estimate to the apparatus.

**Canonical sources.** [Three explicit statistics](../science/outcome_minima.md#three-explicit-statistics-give-a-complete-criterion); [invertible qutrit marginal](../science/outcome_minima.md#invertible-qutrit-marginal); [equality cases](../science/outcome_minima.md#equality-cases-and-verification).

### M18 The third statistic on the marginal boundary

**Central question.** How is the criterion completed when the rank promise is removed?

**Understanding target.** Use support reduction for a singular qutrit marginal. At rank two, $`f=g=0`$ while $`h=e_4(H)`$ becomes the determinant on the supported two-qubit block; at rank one the state is product. Integrate these cases with the invertible-marginal rule, preserving every strict and non-strict sign in the complete criterion.

**Prerequisites.** [M04](#m04-marginal-rank-and-physical-support), [M16](#m16-the-singular-state-reached-by-continuation), [M17](#m17-two-statistics-under-an-invertible-marginal).

**Conceptual connection.** Explain how $`h`$ resolves a collision that $`f,g`$ cannot resolve, and why a rule checked only at generic full rank would miss a load-bearing part of the theorem.

**Canonical sources.** [Singular qutrit marginal](../science/outcome_minima.md#singular-qutrit-marginal); [equality cases](../science/outcome_minima.md#equality-cases-and-verification); [complete criterion](../science/outcome_minima.md#three-explicit-statistics-give-a-complete-criterion).

### M19 One fixed six-copy measurement

**Central question.** How are the three quantities retained by one physical POVM?

**Understanding target.** Transfer the reduction maps to antisymmetric projectors to obtain fixed $`W_f,W_g,W_h`$ with the required expectations. Track the six derivative terms for $`g`$ and the identity padding for $`h`$. Use operator-norm certificates on the complete Hilbert space to make all four effects positive and recover the statistics by affine transformations.

**Prerequisites.** [M06](#m06-polynomial-degree-and-collective-realization), [M07](#m07-spectral-coefficients-and-antisymmetric-observables), [M18](#m18-the-third-statistic-on-the-marginal-boundary).

**Conceptual connection.** Explain why the construction needs neither a physical partial transpose nor prior knowledge of $`B`$, and why omitting $`h`$ permits a three-outcome POVM under the rank promise. Distinguish a positivity proof from checks on selected input states.

**Canonical sources.** [Explicit observables](../science/collective_measurements.md#explicit-six-copy-observables); [norm certificates](../science/collective_measurements.md#certified-operator-norm-bounds); [concrete POVMs](../science/collective_measurements.md#a-concrete-four-outcome-povm).

### M20 The attained outcome hierarchy

**Central question.** How do the converses and constructions fit into one exact minimum?

**Understanding target.** Assemble the minimum outcome counts: two for all two-qubit states, three for qubit–qutrit states with $`B\gt0`$, and four for all qubit–qutrit states. Place the established two-qubit determinant construction beside the new outcome argument. Understand restriction to a local $`2\times3`$ subspace as a lower-bound transfer to larger dimensions.

**Prerequisites.** [M14](#m14-why-one-scalar-cannot-classify-the-corner), [M16](#m16-the-singular-state-reached-by-continuation), [M19](#m19-one-fixed-six-copy-measurement).

**Conceptual connection.** State the matching lower and upper sides with their domains: lower bounds allow every finite block; six copies suffice for the qubit–qutrit constructions; four-outcome sufficiency is established only in $`2\times3`$ and its exchanged version.

**Canonical sources.** [R1 in the model](../science/model.md#r1-minimum-outcome-counts); [attainment and dimensional consequences](../science/outcome_minima.md#attainment-and-dimensional-consequences); [two-qubit determinant criterion](../science/binary_rigidity.md#2-the-two-qubit-determinant-criterion); [original determinant construction](../references/RELATED_WORK.md#augusiak2008).

### M21 A constant probability on the two-qubit boundary

**Central question.** What does exact scalar universality force in the exceptional two-qubit case?

**Understanding target.** Use the full-rank separable boundary state $`\tau=I_4/6+|\Phi^+\rangle\langle\Phi^+|/3`$, whose partial transpose has rank three. The local determinant hypersurface separates physical PPT and NPT states. The separable interval and connectedness force every universal scalar to take a constant endpoint value $`c`$ on a smooth open boundary patch.

**Prerequisites.** [M09](#m09-analytic-geometry-of-a-scalar-image), [M20](#m20-the-attained-outcome-hierarchy).

**Conceptual connection.** Explain why the detector's universality on all mixed states constrains its values near a full-rank boundary, even when the later hard statistical inputs are pure.

**Canonical sources.** [Separable scalar image](../science/binary_rigidity.md#31-the-image-of-the-separable-set); [explicit smooth boundary point](../science/binary_rigidity.md#32-an-explicit-smooth-boundary-point).

### M22 Determinant divisibility and four-copy necessity

**Central question.** Why must every universal binary probability contain the determinant?

**Understanding target.** Combine boundary constancy with absolute irreducibility of the partial-transpose determinant on trace-one coordinates. Obtain $`p_E=c+\det(\rho^\Gamma)q`$ with $`\deg q\le k-4`$. Deduce four-copy necessity and affine uniqueness of the probability at four copies, while retaining the distinction between a probability function and its microscopic implementation.

**Prerequisites.** [M10](#m10-polynomial-identities-beyond-a-physical-patch), [M21](#m21-a-constant-probability-on-the-two-qubit-boundary).

**Conceptual connection.** Explain why all determinant-zero states share $`c`$, why $`0\lt c\lt1`$ follows from a nontrivial effect and a full-rank state, and why an arbitrary higher-degree quotient need not yield a universal detector.

**Canonical sources.** [R2 statement](../science/binary_rigidity.md#r2-rigidity-and-minimum-block-size); [irreducibility and divisibility](../science/binary_rigidity.md#4-irreducibility-and-continuation-on-the-trace-one-space); [scope of the quotient condition](../science/binary_rigidity.md#8-scope).

### M23 A feasible and normalized binary detector

**Central question.** Which affine determinant probabilities can a four-copy effect realize?

**Understanding target.** Follow the four-copy antisymmetric construction and its Schmidt certificate to the spectrum of $`W`$. Understand why $`E_*=I/2+W`$ is valid and measures $`1/2+\det(\rho^\Gamma)`$. Permutation averaging and polarization identify the symmetric effect, giving the exact feasibility condition $`|\alpha|\le2\min(c,1-c)`$ for $`c+\alpha\det(\rho^\Gamma)`$.

**Prerequisites.** [M07](#m07-spectral-coefficients-and-antisymmetric-observables), [M22](#m22-determinant-divisibility-and-four-copy-necessity).

**Conceptual connection.** Distinguish uniqueness after copy-permutation averaging from uniqueness of all implementations. Interpret the optimal affine scale as a local sensitivity statement and four-copy sufficiency, without inferring a global finite-sample optimum.

**Canonical sources.** [Four-copy observable](../science/binary_rigidity.md#5-a-concrete-four-copy-observable); [spectrum and normalization](../science/binary_rigidity.md#6-spectrum-and-binary-normalization); [feasible probabilities](../science/binary_rigidity.md#7-which-four-copy-probabilities-are-physically-feasible).

### M24 Weak entanglement and fourth-order sensitivity

**Central question.** How does binary rigidity suppress sensitivity near a product state?

**Understanding target.** Use the Schmidt family $`\cos\theta|00\rangle+\sin\theta|11\rangle`$ with $`0\le\theta\le\pi/4`$. Match dephasing and witness bounds to obtain $`\Delta=\sin\theta\cos\theta`$, and connect its partial-transpose spectrum to determinant $`-\Delta^4`$. Rigidity makes every allowed probability variation vanish through third order along this family.

**Prerequisites.** [M08](#m08-distance-and-witness-certificates), [M22](#m22-determinant-divisibility-and-four-copy-necessity), [M23](#m23-a-feasible-and-normalized-binary-detector).

**Conceptual connection.** Explain why this pure family is a valid hard instance for a detector required to work on all mixed states. Distinguish forced vanishing through third order from a claim that every effect has exactly fourth-order variation.

**Canonical sources.** [Hard family and exact distance](../science/sampling_cost.md#22-a-family-attaining-the-fourth-power); [fourth-order flatness](../science/sampling_cost.md#32-fourth-order-flatness-along-the-family-in-8).

### M25 A uniform repetition lower bound

**Central question.** Why can neither gap-dependent tuning nor a rare output evade the exponent?

**Understanding target.** Use $`\tau\ge I/6`$ to control both $`E`$ and $`I-E`$ by their boundary probabilities. Along the hard family, combine that scale control with a fourth-derivative estimate to bound $`|p-c|`$ by $`B_k\min(c,1-c)\delta^4`$. The Bernoulli divergence is then uniformly $`O_k(\delta^8)`$, and data processing for the final decision forces the repetition lower bound.

**Prerequisites.** [M11](#m11-probability-gaps-and-statistical-evidence), [M21](#m21-a-constant-probability-on-the-two-qubit-boundary), [M24](#m24-weak-entanglement-and-fourth-order-sensitivity).

**Conceptual connection.** Identify why an effect-dependent bound on $`q`$ alone would be insufficient for minimax optimization. Explain why an effect chosen using $`\delta,\eta`$ remains covered when it is globally universal and $`k`$ is fixed.

**Canonical sources.** [Uniform probability bound](../science/sampling_cost.md#3-a-probability-bound-uniform-over-all-universal-effects); [information lower bound](../science/sampling_cost.md#4-information-theoretic-lower-bound); [explicit uniform constants](../science/sampling_cost.md#r3-uniform-repetition-bounds).

### M26 The sharp statistical law and its comparison

**Central question.** What makes the repetition exponent sharp, and what restriction causes it?

**Understanding target.** Combine the imported determinant–concurrence bound with the local trace-distance comparison to obtain $`|\det(\rho^\Gamma)|\ge\Delta^4`$. The normalized detector and a frequency threshold attain $`O(\delta^{-8}\log(1/\eta))`$ repetitions. Join this upper bound to M25 as R3 for fixed $`k\ge4`$, $`0\lt\delta\le1/2`$, and $`0\lt\eta\le1/4`$. Compare it with the $`\Theta(\delta^{-2}\log(1/\eta))`$ total-copy law for unrestricted two-qubit measurements.

**Prerequisites.** [M08](#m08-distance-and-witness-certificates), [M23](#m23-a-feasible-and-normalized-binary-detector), [M25](#m25-a-uniform-repetition-lower-bound).

**Conceptual connection.** Explain the architectural cost of exact universal binary readout at fixed $`k`$, with total copies $`kn`$. Distinguish the best rate in this class from the behavior of every effect and from an optimal tradeoff when $`k`$ grows with the gap.

**Canonical sources.** [Determinant and distance](../science/sampling_cost.md#2-determinant-and-distance-to-separability); [matching upper bound](../science/sampling_cost.md#5-matching-four-copy-upper-bound); [unrestricted comparison](../science/sampling_cost.md#6-comparison-with-unrestricted-measurements); [theorem boundaries](../science/sampling_cost.md#7-boundaries-of-the-theorem).

### M27 The block-size cost of a promise gap

**Central question.** How does the qubit–qutrit obstruction change if a detector may ignore weak entanglement?

**Understanding target.** Formulate S1 with no required decision on $`0\lt\Delta\lt\delta`$ and an exactly known binary probability. Use witnesses to certify the gap on the physical corner. Embed two independent Boolean majorities, convert arbitrary scalar postprocessing to a strict polynomial sign representation, and identify the imported threshold-degree theorem that yields an $`\Omega(\log(1/\delta))`$ block-size lower bound.

**Prerequisites.** [M06](#m06-polynomial-degree-and-collective-realization), [M08](#m08-distance-and-witness-certificates), [M14](#m14-why-one-scalar-cannot-classify-the-corner), [M26](#m26-the-sharp-statistical-law-and-its-comparison).

**Conceptual connection.** Explain why this task can admit a binary effect without contradicting R1. Distinguish the finite Boolean sign reduction from an assumed threshold classifier on the full continuum of states.

**Canonical sources.** [S1 and its task](../science/model.md#s1-binary-blocks-under-a-distance-promise); [physical distance certificate](../science/promise_gap.md#1-a-physical-quadrant-with-a-certified-distance); [two-majority lower bound](../science/promise_gap.md#2-lower-bound-from-two-majority-functions); [threshold-degree attribution](../references/RELATED_WORK.md#sherstov2013).

### M28 A binary filter attaining the logarithmic block size

**Central question.** How can a single probability combine the promised spectral signs?

**Understanding target.** Convert a trace-distance gap into a negative gap in at least one of $`e_3,e_4,e_5,e_6`$. Use a bounded rational sign filter so that one negative coordinate cannot be overwhelmed by the others. Clear strictly positive denominators, control the polynomial degree by $`O(\log(1/\delta))`$, and realize that polynomial as a fixed binary effect.

**Prerequisites.** [M06](#m06-polynomial-degree-and-collective-realization), [M07](#m07-spectral-coefficients-and-antisymmetric-observables), [M27](#m27-the-block-size-cost-of-a-promise-gap).

**Conceptual connection.** Join the construction and lower bound into S1. Explain why positive denominators preserve signs, why boundedness inside the transition interval matters, and why logarithmic block size supplies no logarithmic repetition or total-copy guarantee.

**Canonical sources.** [Characteristic-coefficient gap](../science/promise_gap.md#3-a-characteristic-coefficient-gap); [bounded rational filter](../science/promise_gap.md#4-an-explicit-bounded-rational-sign-filter); [polynomial realization](../science/promise_gap.md#5-clearing-denominators-and-realizing-one-binary-probability); [interpretation](../science/promise_gap.md#interpretation-and-exact-checks).

### M29 Attribution and the strength of the evidence

**Central question.** Which parts of the scientific account rest on which kind of evidence?

**Understanding target.** Locate imported PPT completeness, determinant measurement and concurrence bounds, polynomial realization, and threshold degree beside the arguments developed in this repository. Distinguish a complete criterion from a minimum retained record, a single-copy obstruction from an all-finite-copy converse, and exact finite checks from universal analytical proofs.

**Prerequisites.** [M20](#m20-the-attained-outcome-hierarchy), [M23](#m23-a-feasible-and-normalized-binary-detector), [M26](#m26-the-sharp-statistical-law-and-its-comparison), [M28](#m28-a-binary-filter-attaining-the-logarithmic-block-size).

**Conceptual connection.** Match a claim to its proof or imported source, state what the five verification modules actually establish, and avoid inferring universal correctness, experimental validation, external peer review, or exhaustive priority from finite checks and a focused literature comparison.

**Canonical sources.** [Related work and attribution](../references/RELATED_WORK.md); [what is checked](../verification/README.md#what-is-checked); [what requires proofs or external sources](../verification/README.md#what-requires-proofs-or-external-sources); [scope of the novelty review](../references/RELATED_WORK.md#scope-of-the-novelty-review).

### M30 The complete scientific story

**Central question.** What does universal entanglement readout teach about the information an apparatus keeps?

**Understanding target.** Connect the physical state-space corner to the attained outcome hierarchy, the two-qubit determinant boundary to binary rigidity, and rigidity to the sharp fixed-block statistical penalty. Place the gap-only alternative beside those results with its own resource and domain. Give one coherent account of what is possible, what is necessary, and which assumptions make each statement true.

**Prerequisites.** [M12](#m12-the-complete-operational-question), [M29](#m29-attribution-and-the-strength-of-the-evidence).

**Conceptual connection.** Interpret a changed experimental assumption and identify which result still applies. Explain R1, R2, R3, and S1 together while keeping outcomes, coordinates, block size, repetitions, probability precision, rank promises, and attribution distinct.

**Canonical sources.** [Model and exact claims](../science/model.md); [connected scientific reading route](../science/model.md#reading-and-verification); [readout resources and interpretation](../science/interpretation.md).
