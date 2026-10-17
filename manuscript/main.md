# Minimum Outcomes and Statistical Cost of Universal Entanglement Readout

## Abstract

How much of a collective measurement's output distribution must be retained to detect every entangled mixed state? For a fixed apparatus acting on any finite number of independent copies, the exact minimum is two outcomes for two qubits, three for a qubit–qutrit state with an invertible qutrit marginal, and four for an arbitrary qubit–qutrit state. The lower bounds allow arbitrary classical processing of exactly known probabilities. An explicit six-copy measurement attains both qubit–qutrit minima. The binary two-qubit exception also has a statistical constraint: every universal probability polynomial is constant on the partial-transpose determinant boundary and is divisible by that determinant after subtracting the constant. This makes four copies necessary and imposes a sharp worst-case repetition cost proportional to the inverse eighth power of the trace-distance gap at any fixed block size. The known four-copy determinant measurement attains that exponent. These results distinguish retained outcomes, collective block size, and finite-sample cost within one operational model.

## 1. The question concerns the retained distribution

A collective apparatus can measure a nonlinear function of a density operator by acting on several copies [Brun2004](../references/RELATED_WORK.md#brun2004-and-leifer2004). For two qubits, the sign of the partial-transpose determinant completely decides entanglement, and a four-copy collective measurement accesses that determinant [Augusiak2008](../references/RELATED_WORK.md#augusiak2008). Rescaling its observable gives one binary probability. This raises a more restrictive question than whether a suitable witness can be selected for a particular state: can one fixed binary apparatus distinguish every separable mixed state from every entangled one?

The distinction between an entanglement criterion and its experimental data requirement is essential. A single setting can have many retained outcomes. A detector selected after estimating the input state uses information outside its final output. Even when one exactly known scalar is sufficient, estimating it near the separable boundary can be expensive. Earlier work already separates criterion count from statistical efficiency [Leifer2004](../references/RELATED_WORK.md#brun2004-and-leifer2004), [LiuWei2025](../references/RELATED_WORK.md#liuwei2025). The results below give attained outcome minima and a sharp distance exponent for a precise class of fixed universal apparatuses.

Let $`\rho`$ be an unknown bipartite density operator. Each run consumes $`k`$ fresh independent copies and applies the same state-independent POVM $`\{E_j\}_{j=1}^m`$. The probabilities are

```math
p_j(\rho)=\mathrm{Tr}(E_j\rho^{\otimes k}),\qquad
\sum_{j=1}^m p_j(\rho)=1.
```

Ancillas and global processing inside the block are unrestricted. The complete retained distribution has $`m-1`$ coordinates, each a polynomial of degree at most $`k`$. Exact universality means that some decision map of this distribution classifies every state in the stated domain. The decision map may be discontinuous. The lower bounds consequently apply beyond a prescribed collection of polynomial sign inequalities.

For statistical tests, define

```math
\Delta(\rho)=\inf_{\sigma\in\mathrm{SEP}}\frac12\Vert\rho-\sigma\Vert_1.
```

The independent-copy assumption, rank promises, and exact versus statistical tasks are specified in [Model and exact claims](../science/model.md). Probability resolution and internal circuit complexity are separate resources.

## 2. An attained outcome hierarchy

**Result R1.** Minimizing over every finite block size and every exact decision map gives the following outcome counts.

| Input domain | Minimum outcomes | Sufficient copies per run |
|---|---:|---:|
| Arbitrary two-qubit states | 2 | 4 |
| Qubit–qutrit states with invertible qutrit marginal | 3 | 6 |
| Arbitrary qubit–qutrit states | 4 | 6 |

The four-copy two-qubit construction is inherited from [Augusiak2008](../references/RELATED_WORK.md#augusiak2008). Four-copy necessity for an arbitrary exactly universal binary apparatus follows from R2 below. The six-copy constructions are sufficient; R1 does not assert their copy optimality. The qubit–qutrit lower bound also embeds into all other nontrivial bipartite dimensions except $`2\times2`$, where at least four outcomes are therefore necessary. Sufficiency of four outcomes is proved here for $`2\times3`$.

### Why one scalar fails beyond two qubits

The positive partial transpose criterion is equivalent to separability in $`2\times3`$ [PPT1996](../references/RELATED_WORK.md#peres1996-and-ppt1996). There is an explicit full-rank family $`\rho(s,t)`$ on a square around the origin for which $`\rho(s,t)^\Gamma`$ has two distinguished eigenvalues $`s,t`$ and four positive eigenvalues. Consequently,

```math
\rho(s,t)\in\mathrm{SEP}\quad\Longleftrightarrow\quad s\ge0\text{ and }t\ge0.
```

No real analytic scalar can classify this quadrant through arbitrary exact postprocessing. The scalar image of the closed positive quadrant is an interval. Every point on one positive boundary ray is approached from the complement, so its image must be an endpoint of that interval. Connectedness makes the scalar constant on that ray. Analytic continuation then assigns the same value to the negative ray, which consists of entangled states. The explicit physical family shows that this obstruction holds even when all input states and marginals are full rank.

### Why two scalars still fail without a rank promise

The stronger converse uses the rank-four positive partial-transpose stratum. Near every point where the original state is full rank and its partial transpose is positive of rank four, a Schur-complement chart gives a two-dimensional normal slice with the same quadrant criterion. If either of two proposed statistics varied tangentially along this stratum, the analytic implicit function theorem would hold that statistic fixed while the other classified the quadrant. The scalar obstruction rules this out.

Both statistics must therefore be constant on a nonempty open patch of the rank-four stratum. A polynomial identity then extends this constant value to every trace-one Hermitian matrix of rank at most four in partial-transpose coordinates. The continuation can be made explicit: homogenize the polynomial with the trace, substitute $`X=YY^\dagger`$ for a complex $`6\times4`$ matrix, and use vanishing on an open real set. Complexification makes the two factors independent, giving the identity on all products $`YZ^T`$, which cover the rank-at-most-four matrices.

An embedded Bell state has partial-transpose spectrum

```math
-\frac12,\quad\frac12,\quad\frac12,\quad\frac12,\quad0,\quad0.
```

It would receive the same two statistics as a separable state in the open patch, contradicting universality. This final state has a singular qutrit marginal. Its role explains why the stronger lower bound is compatible with a three-outcome apparatus under the invertible-marginal promise.

### Three explicit quantities achieve the unrestricted minimum

Define

```math
B=\mathrm{Tr}_A\rho,\qquad D=I_2\otimes B,\qquad H=D-\rho,
```

and retain

```math
f=\det H,\qquad
g=\mathrm{Tr}[D\mathrm{adj}(H)],\qquad
h=e_4(H).
```

Here $`e_4`$ is the fourth elementary symmetric coefficient. These are polynomials of degrees six, six, and four. The qubit reduction identity makes $`H`$ unitarily equivalent to $`\rho^\Gamma`$. The exact decision rule is

```math
\rho\in\mathrm{SEP}\quad\Longleftrightarrow\quad
(f>0\ \text{and}\ g>0)
\quad\text{or}\quad
\bigl(f=0\ \text{and}\ [g>0\ \text{or}\ (g=0\ \text{and}\ h\ge0)]\bigr).
```

When $`B>0`$, only $`f,g`$ are needed: the second branch reduces to $`f=0,g\ge0`$. To see why these two quantities work under the promise, set $`K=D^{-1/2}HD^{-1/2}`$. Then $`K\le I`$ and $`\mathrm{Tr}K=3`$. If $`K`$ has any negative eigenvalue, it must have at least four positive eigenvalues. The determinant distinguishes one negative eigenvalue at full rank. The identity

```math
g=(\det B)^2e_5(K)
```

resolves the two-negative case and the rank-five boundary. With two negatives $`-a,-b`$ and four positives $`c_i`$, the trace constraint implies $`c_i\ge a+b`$, giving

```math
e_5(K)=\left(\prod_i c_i\right)
\left[ab\sum_i\frac1{c_i}-(a+b)\right]\le0.
```

If $`B`$ is singular, positivity confines $`\rho`$ to a local two-qubit support or a product support. In the former case $`f=g=0`$, while $`h`$ is the determinant criterion on that two-qubit block. This is the reason to retain the third quantity for unrestricted inputs.

The strict sign of $`g`$ in the branch $`f>0`$ matters. An exact entangled example has

```math
(f,g,h)=\left(\frac1{4096},0,-\frac1{64}\right).
```

Replacing $`g>0`$ by $`g\ge0`$ would misclassify it. The full proof, physical seed, and equality example are given in [Outcome minima](../science/outcome_minima.md).

The three quantities can be measured by one state-independent POVM on six copies. Antisymmetrizers represent the elementary coefficients, and the self-adjoint qubit reduction map transfers $`H`$ and $`D`$ to observable operators. The resulting observables $`W_f,W_g,W_h`$ have certified bounds $`1,12,\sqrt{15}`$ on their operator norms. In particular,

```math
E_i=\frac I4+\frac{W_i}{80}\quad(i=f,g,h),\qquad
E_4=\frac I4-\frac{W_f+W_g+W_h}{80}
```

are strictly positive and sum to identity. Their probabilities recover $`f,g,h`$ by known affine transformations. [Collective measurements](../science/collective_measurements.md) gives the explicit permutation formulas and a three-outcome version for $`B>0`$. Whitening is used only in the proof; it is not a state-dependent operation in this apparatus.

## 3. The binary exception is rigid

**Result R2.** Let $`p_E(\rho)=\mathrm{Tr}(E\rho^{\otimes k})`$ be exactly universal for all two-qubit mixed states. Then

```math
p_E(\rho)=c+\det(\rho^\Gamma)q(\rho),\qquad\deg q\le k-4.
```

Thus $`k\ge4`$. At four copies, the probability is an affine rescaling of the determinant. This does not assert that all microscopic implementations of that probability are identical.

The rigidity comes from a physical boundary patch and a polynomial continuation. The separable set has an interval as its scalar image. A smooth full-rank point with partial-transpose rank three lies on the boundary between separable and entangled states. A connected open patch of this boundary must map to a single endpoint $`c`$ of the interval. Hence $`p_E-c`$ vanishes on that patch.

The determinant of a generic matrix is irreducible. The property remains true on the trace-one affine Hermitian coordinates after complexification and partial transpose. The real smooth physical patch is Zariski dense in the determinant hypersurface. Therefore the determinant divides $`p_E-c`$. The full argument, including the trace-one restriction and the distinction between the probability polynomial and the effect, is in [Binary rigidity](../science/binary_rigidity.md). Smooth boundary geometry itself is prior work [Djokovic2006](../references/RELATED_WORK.md#djokovic2006); the divisibility statement constrains every fixed finite-copy scalar classifier.

## 4. Exact universality costs repetitions

**Result R3.** Fix a finite $`k\ge4`$, a gap $`0<\delta\le1/2`$, and an error target $`0<\eta\le1/4`$. Among binary effects that remain exactly universal on all two-qubit mixed states, the minimum fixed number of independent repetitions required to distinguish $`\mathrm{SEP}`$ from $`\Delta(\rho)\ge\delta`$ is

```math
n_{\mathrm{univ},k}(\delta,\eta)
=\Theta_k\!\left(\delta^{-8}\log\frac1\eta\right).
```

The constants are uniform over the chosen effects at fixed $`k`$. An effect may be chosen using knowledge of the gap, provided it remains exactly universal outside the promised task as well.

### A weakly entangled pure state determines the exponent

Consider

```math
|\psi_\theta\rangle=\cos\theta|00\rangle+\sin\theta|11\rangle,
\qquad 0<\theta\le\frac\pi4.
```

Its exact distance to the separable set is $`\delta=\sin\theta\cos\theta`$, and

```math
\det(\rho_\theta^\Gamma)=-\delta^4.
```

R2 forces the probability variation away from the product limit to vanish through third order; some effects can vanish to higher order. A full-rank separable boundary state has the same probability $`c`$, which forces $`0<c<1`$ for a nontrivial effect. Positivity and a fourth-derivative bound give, uniformly over the universal effects,

```math
|p_E(\rho_\theta)-c|
\le B_k\min(c,1-c)\delta^4,
```

with an explicit finite constant $`B_k`$. Consequently the one-run Bernoulli relative entropy against the product input is at most $`B_k^2\delta^8`$. Additivity and data processing for any classical test of the bit string yield the lower bound, including the logarithmic confidence factor. The effect cannot evade it by choosing a very rare output because the same positivity argument scales the probability difference with $`\min(c,1-c)`$.

### The determinant apparatus attains the exponent

Let $`P`$ be the rank-one projector onto the totally antisymmetric state of four four-level copies, and put $`W=P^{\Gamma_{A_1}\cdots\Gamma_{A_4}}`$. The nonzero eigenvalues of $`W`$ are $`1/2`$ with multiplicity three and $`-1/2`$ with multiplicity one. Thus

```math
E_*=\frac I2+W,\qquad p_*(\rho)=\frac12+\det(\rho^\Gamma)
```

defines a valid binary effect.

The established determinant–concurrence inequality [Augusiak2008](../references/RELATED_WORK.md#augusiak2008), [Demianowicz2011](../references/RELATED_WORK.md#wootters1998-and-demianowicz2011), together with a direct convex-roof comparison between concurrence and distance to separability, gives

```math
|\det(\rho^\Gamma)|\ge\Delta(\rho)^4
\quad\text{for entangled two-qubit states}.
```

Separable states have $`p_*\ge1/2`$, while promised entangled states have $`p_*\le1/2-\delta^4`$. A frequency threshold at $`1/2-\delta^4/2`$ and Hoeffding's inequality achieve

```math
n\le\left\lceil2\delta^{-8}\log\frac1\eta\right\rceil.
```

The construction uses $`4n`$ copies, or $`kn`$ copies if padded to a larger fixed block. [Sampling cost](../science/sampling_cost.md) gives the constants, the distance proof, and the exact normalization. This is a lower bound for exact binary universality, not a general lower bound on entanglement testing. Allowing a larger retained distribution or designing an apparatus only for a fixed gap changes the problem.

## 5. What changes under a gap-only requirement

For qubit–qutrit states, exact binary universality is impossible for every finite block. If a detector may ignore all states with $`0<\Delta(\rho)<\delta`$, a finite binary block becomes possible. The supporting [Result S1](../science/promise_gap.md) gives

```math
k_{\mathrm{gap}}(\delta)=\Theta\!\left(\log\frac1\delta\right)
\qquad(\delta\downarrow0)
```

when its probability is known exactly. The lower bound embeds the conjunction of two majority functions into the physical quadrant and imports their threshold-degree bound [Sherstov2013](../references/RELATED_WORK.md#sherstov2013). The upper bound turns four characteristic-coefficient signs into a bounded rational conjunction, clears positive denominators, and realizes the resulting polynomial as a binary effect [Brun2004](../references/RELATED_WORK.md#brun2004-and-leifer2004).

S1 concerns the block-size price of approaching exact universality. Its construction can have a very small probability margin, so it gives no corresponding logarithmic bound on repetitions or total copies. This is why the statistical law R3 and the block-size law S1 are stated separately.

## 6. Interpretation and attribution

The outcome hierarchy and sampling law answer two parts of the same fixed-apparatus question. Beyond two qubits, a universal detector must retain more than one scalar; on all qubit–qutrit states it needs three coordinates. For the exceptional binary case, the determinant boundary bounds the weak-entanglement sensitivity and gives an eighth-power repetition lower bound at fixed block size. The normalized determinant apparatus attains that exponent.

The rank promise is material. The local scalar obstruction uses full-rank states, but the second coordinate obstruction reaches a singular marginal through polynomial continuation. Admitting that boundary changes the exact minimum outcome count. Exact universality is also material. It imposes correctness arbitrarily close to every separable boundary point even when the subsequent sampling task has a nonzero promise.

The closest located sources supply the two-qubit determinant apparatus [Augusiak2008](../references/RELATED_WORK.md#augusiak2008), single-copy tomography obstructions [Carmeli2016](../references/RELATED_WORK.md#carmeli2016), [Lu2016](../references/RELATED_WORK.md#lu2016), complete qubit–qutrit coefficient tests [ZhangXie2026](../references/RELATED_WORK.md#zhangxie2026), and earlier separations between criteria and sample efficiency [Leifer2004](../references/RELATED_WORK.md#brun2004-and-leifer2004), [LiuWei2025](../references/RELATED_WORK.md#liuwei2025). The [attribution account](../references/RELATED_WORK.md) distinguishes those ingredients from the all-finite-degree output converse, the universal divisibility statement, and the fixed-block statistical exponent. A focused literature comparison supports these distinctions; it does not establish exhaustive priority.

## Proofs and reproducibility

| Component | Complete supporting account |
|---|---|
| Operational definitions and exact quantifiers | [Model](../science/model.md) |
| Physical quadrant, outcome lower bounds, and rank-sensitive criterion | [Outcome minima](../science/outcome_minima.md) |
| Fixed observables and POVM positivity | [Collective measurements](../science/collective_measurements.md) |
| Boundary continuation and four-copy necessity | [Binary rigidity](../science/binary_rigidity.md) |
| Uniform information lower bound and matching detector | [Sampling cost](../science/sampling_cost.md) |
| Gap-dependent binary block size | [Promise-gap theorem](../science/promise_gap.md) |
| Primary-source roles and bibliography | [Related work](../references/RELATED_WORK.md) |
| Exact examples and implementation checks | [Verification](../verification/README.md) |

The finite calculations check the explicit physical seed, rank and equality cases, antisymmetric Schmidt certificate, rational filter, and collective-observable contractions. The general converses, asymptotic statements, and originality assessment rely on their written proofs or cited primary sources, not on extrapolation from those checks.
