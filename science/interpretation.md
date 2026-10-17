# Readout resources and interpretation

The outcome hierarchy and sampling law answer two parts of the same fixed-apparatus question. Beyond two qubits, a universal detector must retain more than one scalar; on all qubit–qutrit states it needs three coordinates. For the exceptional binary case, the determinant boundary bounds the weak-entanglement sensitivity and gives an eighth-power repetition lower bound at fixed block size. The normalized determinant apparatus attains that exponent.

The exact domains and quantifiers are collected in [Model and exact claims](model.md). This page connects the proof mechanisms and their physical meaning; the linked scientific pages give the complete proofs.

## Boundary geometry constrains the retained record

A probability obtained from a fixed finite block is polynomial in the density operator. Arbitrary classical postprocessing does not remove a collision between a separable state and an entangled state with the same probability. The [physical quadrant](outcome_minima.md#a-physical-quadrant) realizes two independent directions across the separable boundary while keeping the input density operator positive definite. Its two distinguished partial-transpose eigenvalues are the coordinates of a quadrant. The analytic scalar obstruction therefore rules out every finite-block binary classifier, not just a chosen witness or a prescribed threshold rule.

The rank promise is material. The local scalar obstruction uses full-rank states, but the second coordinate obstruction reaches a singular marginal through polynomial continuation. Admitting that boundary changes the exact minimum outcome count. The [two-coordinate converse](outcome_minima.md#two-polynomial-coordinates-are-insufficient-on-all-states) uses a two-dimensional diagonal slice of the normal directions to a rank-four stratum, not an assertion that the entire normal space has dimension two. It forces both coordinates to be constant on a physical patch. The resulting polynomial identity then reaches an embedded Bell state.

The [attaining criterion](outcome_minima.md#three-explicit-statistics-give-a-complete-criterion) reflects the same distinction. Its determinant and weighted-adjugate statistics suffice for an invertible qutrit marginal. A third statistic distinguishes the supported two-qubit states at a singular marginal. This is why the rank promise changes the number of retained coordinates even though the same six-copy construction can implement both measurements.

The [collective measurement construction](collective_measurements.md) turns these polynomials into one fixed positive POVM. Partial transpose and marginal whitening enter the analysis, not an uncounted preliminary state estimate or a physical operation applied to the unknown input. Its six-copy block establishes sufficiency, while the outcome converse permits every finite block size. The two resource statements are different.

## A universal scalar can still have poor sensitivity

Exact universality is also material. It imposes correctness arbitrarily close to every separable boundary point even when the subsequent sampling task has a nonzero promise. In the two-qubit exception, a connected smooth boundary patch fixes a universal scalar's value to one endpoint of its separable image. Irreducibility of the partial-transpose determinant turns this constancy into the [determinant factorization](binary_rigidity.md#4-irreducibility-and-continuation-on-the-trace-one-space). The four-copy minimum and affine rigidity follow from its degree.

Along the weakly entangled Schmidt family, the determinant is minus the fourth power of the half-trace distance to separability. For the normalized determinant detector, a probability change of order four suggests a repetition cost of order eight because empirical-frequency fluctuations scale as the inverse square root of the number of runs. That observation explains the exponent for one apparatus; it does not establish the optimum over all apparatuses.

The [uniform probability bound](sampling_cost.md#3-a-probability-bound-uniform-over-all-universal-effects) supplies the additional step. A full-rank separable boundary state controls both an effect and its complement through their boundary probabilities. This prevents a gap-dependent choice of an extremely rare output from evading the information bound. Combined with data processing and the matching determinant detector, it gives the best fixed-block repetition rate over the entire globally universal binary class.

The hard statistical inputs can be pure even though the required universality includes every mixed state. A purity promise would change the apparatus class and remove the premise behind this rigidity argument. Likewise, the constants in the repetition lower bound depend on the fixed block size; the result does not give an optimal joint tradeoff when that size grows as the distance gap shrinks.

## A distance promise changes the apparatus requirement

For qubit–qutrit inputs, the [gap-only task](promise_gap.md) permits arbitrary behavior on entangled states closer than the specified distance to the separable set. A rational filter can combine the characteristic-coefficient signs across this unconstrained region, and clearing positive denominators produces one polynomial scalar. This makes a finite binary apparatus possible without contradicting the exact-universality obstruction.

The supporting logarithmic law counts copies within one block and allows arbitrarily precise knowledge of its outcome probability. It does not control the asymptotic probability margin after normalization. It consequently gives no logarithmic repetition or total-copy bound. By contrast, the two-qubit sampling theorem retains global exact universality even while its statistical decision is tested under a distance promise.

The [unrestricted two-qubit comparison](sampling_cost.md#6-comparison-with-unrestricted-measurements) permits a richer measurement record and gives a quadratic inverse-distance total-copy law, with the same logarithmic confidence dependence. This locates the eighth-power penalty in the fixed-block, exactly universal binary architecture rather than in entanglement detection as a whole. A binary final answer is not the same restriction as one retained binary probability.

## Attribution and strength of evidence

The closest located sources supply the two-qubit determinant apparatus [Augusiak2008](../references/RELATED_WORK.md#augusiak2008), single-copy tomography obstructions [Carmeli2016](../references/RELATED_WORK.md#carmeli2016), [Lu2016](../references/RELATED_WORK.md#lu2016), complete qubit–qutrit coefficient tests [ZhangXie2026](../references/RELATED_WORK.md#zhangxie2026), and earlier separations between criteria and sample efficiency [Leifer2004](../references/RELATED_WORK.md#brun2004-and-leifer2004), [LiuWei2025](../references/RELATED_WORK.md#liuwei2025). The [attribution account](../references/RELATED_WORK.md) distinguishes those ingredients from the all-finite-degree output converse, the universal divisibility statement, and the fixed-block statistical exponent. A focused literature comparison supports these distinctions; it does not establish exhaustive priority.

The [exact checks](../verification/README.md) reproduce finite constructions and identities. Universal claims depend on the complete analytical arguments and their imported theorem ingredients. Together, the scientific pages establish a bounded contribution: attained limits on the record retained by a fixed universal detector and, for its binary exception, the statistical price of that universality.
