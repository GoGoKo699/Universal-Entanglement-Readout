# Model and exact claims

A source prepares independent copies of one unknown bipartite density operator. The task is to decide whether that state is separable using the output distribution of one fixed collective apparatus. This page fixes the resources and quantifiers used throughout the repository.

## States, partial transpose, and distance

Let $`\mathcal H=\mathbb C^{d_A}\otimes\mathbb C^{d_B}`$, with $`d_A,d_B\ge2`$. Write $`\mathcal D(\mathcal H)`$ for the density operators and $`\mathrm{SEP}`$ for their convex subset of separable states. The partial transpose $`\Gamma`$ acts on subsystem $`A`$ in a fixed product basis. Positivity of $`\rho^\Gamma`$ is basis independent under local changes of basis.

For two qubits and for a qubit and a qutrit, the positive partial transpose criterion is complete:

```math
\rho\in\mathrm{SEP}\quad\Longleftrightarrow\quad \rho^\Gamma\ge0.
```

This is an imported theorem [PPT1996](../references/RELATED_WORK.md#peres1996-and-ppt1996); it is not valid as a sufficient criterion in arbitrary local dimensions. References and their roles are collected in [Related work](../references/RELATED_WORK.md).

The distance used in the statistical statements is

```math
\Delta(\rho)=\inf_{\sigma\in\mathrm{SEP}}\frac12\Vert\rho-\sigma\Vert_1.
```

The factor $`1/2`$ is part of the definition. For a qubit–qutrit state, write $`B=\mathrm{Tr}_A\rho`$ for its qutrit marginal. The promise $`B\gt0`$ means that this $`3\times3`$ matrix is invertible. A globally full-rank state satisfies this promise, but a singular global state can also satisfy it.

## One fixed collective apparatus

Choose a finite block size $`k`$ and one state-independent $`m`$-outcome POVM

```math
E_1,\ldots,E_m\ge0,\qquad \sum_{j=1}^{m}E_j=I_{\mathcal H^{\otimes k}}.
```

Every run consumes $`k`$ fresh copies of the same state and produces one label $`j`$. The retained probabilities are

```math
p_j(\rho)=\mathrm{Tr}(E_j\rho^{\otimes k}).
```

Because $`\sum_jp_j=1`$, the complete distribution is specified by $`m-1`$ real coordinates. This is a count of retained coordinates; no assertion of their algebraic independence is needed. A state-independent ancilla, joint unitary, internal measurement, or classical randomization can be absorbed into the POVM. The model permits arbitrary global processing within the block.

The apparatus is **exactly universal** on a state domain $`\mathcal S`$ if a decision map

```math
\mathcal A:\{p(\rho):\rho\in\mathcal S\}\longrightarrow\{\mathrm{separable},\mathrm{entangled}\}
```

classifies every state in that domain correctly when its probability vector is known exactly. The map may be discontinuous and may use arbitrary classical computation. Equivalently, the probability images of separable and entangled inputs are disjoint. The lower bounds do not restrict the decision map to thresholds or conjunctions of signs.

Each $`p_j`$ is a real polynomial of degree at most $`k`$ in real affine coordinates on the trace-one Hermitian matrices. Conversely, a finite collection of real polynomial statistics can be represented by Hermitian observables on a common finite number of copies, then shifted and rescaled into one finite-outcome POVM [Brun2004](../references/RELATED_WORK.md#brun2004-and-leifer2004). The [collective measurement construction](collective_measurements.md) gives this reduction and explicit observables for this project.

A setting label retained across randomized settings is an additional part of the output. So are intermediate measurement records used to estimate a marginal before selecting a detector. The results count the complete retained record. In particular, the whitening used in the qubit–qutrit proof is an algebraic argument; the implemented measurement never needs to know $`B`$.

## R1. Minimum outcome counts

The minimum is taken over every finite $`k`$, every fixed state-independent POVM, and every exact classical decision map.

| State domain | Minimum retained coordinates | Minimum outcomes | Explicit sufficient block size |
|---|---:|---:|---:|
| All two-qubit states | 1 | 2 | 4 copies |
| Qubit–qutrit states with $`B\gt0`$ | 2 | 3 | 6 copies |
| All qubit–qutrit states | 3 | 4 | 6 copies |

The positive four-copy two-qubit construction is established prior work [Augusiak2008](../references/RELATED_WORK.md#augusiak2008). Its copy optimality within the full class of exactly universal binary apparatuses follows from R2. The six-copy entries are constructive upper bounds; their copy optimality is not part of R1.

The scalar obstruction already holds on a neighborhood of full-rank qubit–qutrit states. The stronger lower bound for all qubit–qutrit inputs also embeds into every other nontrivial bipartite dimension except $`2\times2`$, so at least four outcomes are necessary there. Four-outcome sufficiency is proved for $`2\times3`$. The stronger lower bound uses a rank-deficient state after polynomial continuation, which explains the different minimum under the marginal-rank promise.

Full proofs: [Outcome minima](outcome_minima.md), [binary rigidity](binary_rigidity.md), and [explicit collective measurements](collective_measurements.md).

## R2. Rigidity of binary two-qubit readout

For every exactly universal two-qubit effect $`0\le E\le I`$ on a finite block of $`k`$ copies, there are a real constant $`c`$ and a real polynomial $`q`$ such that

```math
p_E(\rho)=c+\det(\rho^\Gamma)q(\rho),\qquad \deg q\le k-4.
```

In particular, $`k\ge4`$. At $`k=4`$, the probability is $`c+\alpha\det(\rho^\Gamma)`$ with $`\alpha\ne0`$. This is uniqueness of the probability polynomial up to an affine transformation. Effects whose nonsymmetric components have zero expectation on every $`\rho^{\otimes4}`$ can implement the same probability.

Full proof: [Binary rigidity](binary_rigidity.md).

## R3. Repetition cost of exact binary universality

Fix $`k\ge4`$. An experiment chooses an effect that is exactly universal on **all** two-qubit mixed states and repeats that same apparatus independently $`n`$ times. It must distinguish

```math
H_0:\rho\in\mathrm{SEP},\qquad H_1:\Delta(\rho)\ge\delta
```

with $`0\lt\delta\le1/2`$ and each worst-case error probability at most $`\eta`$, where $`0\lt\eta\le1/4`$. The effect and the classical test may depend on $`\delta`$ and $`\eta`$, provided the effect remains exactly universal on all mixed states. Let $`n_{\mathrm{univ},k}(\delta,\eta)`$ be the minimum possible fixed number of repetitions under these requirements. Then, as $`\delta\downarrow0`$,

```math
n_{\mathrm{univ},k}(\delta,\eta)
=\Theta_k\!\left(\delta^{-8}\log\frac1\eta\right).
```

The constants are uniform over the chosen effects at fixed $`k`$. The lower-bound constant can depend strongly on $`k`$; this is not a sharp joint tradeoff between block size and distance. The total number of input copies in this model is $`kn`$. A four-copy effect, padded with identities when $`k\gt4`$, achieves

```math
n\le\left\lceil2\delta^{-8}\log\frac1\eta\right\rceil.
```

Full proof and normalization: [Sampling cost](sampling_cost.md).

## S1. Binary blocks under a distance promise

A different task allows a qubit–qutrit apparatus that need only distinguish every separable state from every state with $`\Delta(\rho)\ge\delta`$. Its behavior on $`0\lt\Delta(\rho)\lt\delta`$ is unrestricted, and the effect may depend on $`\delta`$. When the binary probability can be known to arbitrary precision, the minimum block size obeys

```math
k_{\mathrm{gap}}(\delta)=\Theta\!\left(\log\frac1\delta\right).
```

This statement counts copies within a block. It does not bound repetitions, probability resolution, or implementation cost. The constructive bias can be very small. The lower bound imports the threshold degree of the conjunction of two majority functions [Sherstov2013](../references/RELATED_WORK.md#sherstov2013); the quantum reduction and a constructive upper bound are given in [Promise-gap block size](promise_gap.md).

## What each resource measures

| Resource | Meaning here | Where it is controlled |
|---|---|---|
| Outcomes $`m`$ | Labels retained from one run of a fixed apparatus | R1 gives attained minima |
| Block size $`k`$ | Fresh input copies processed collectively per run | R2 gives a binary two-qubit minimum; S1 gives a promised qubit–qutrit asymptotic law |
| Repetitions $`n`$ | Independent runs used to meet a specified statistical error | R3 gives a sharp fixed-$`k`$ law under exact universality |
| Probability precision | Accuracy with which the output distribution is known | Idealized in R1, R2, and S1; explicitly costed through repetitions in R3 |
| Internal gates and workspace | Implementation of the fixed POVM and classical processing | Unrestricted; no efficient circuit or QRAM assumption |

An exact classification theorem does not promise error-free classification from finitely many observations. The statistical penalty in R3 is specific to apparatuses required to remain exactly universal with binary output. It does not apply to arbitrary tomography, a larger output record, or devices designed only for a nonzero gap. The independent-copy and fixed-apparatus assumptions are part of each theorem, not claims about a general experimental source.

## Reading and verification

The [manuscript account](../manuscript/main.md) develops the physical question and proof mechanism in one narrative. The individual science pages contain the complete analytical arguments. [Verification](../verification/README.md) states what the exact scripts check and what is established by proofs or imported theorems instead.
