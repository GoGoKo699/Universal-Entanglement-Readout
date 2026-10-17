# Related work and attribution

This document identifies the established results used in this project and distinguishes nearby measurement models. Citation keys in square brackets match [references.bib](references.bib). The literature review was last checked on 17 October 2026.

## Scope of the comparison

The resource studied here is the number of probability coordinates retained from one fixed POVM on a fixed finite number of identical copies. For a binary measurement, the complete retained information is

$$
p(\rho)=\operatorname{Tr}(E\rho^{\otimes k}),\qquad 0\le E\le I.
$$

Exact classification permits an arbitrary classical decision rule applied to these probabilities, and requires correctness for every state in the specified domain. Copy count, retained output count, and the number of repetitions are distinct resources. A single measurement setting can have many outcomes; a single named invariant can require several measured quantities; and a witness chosen after learning the state is not one fixed universal apparatus.

## Imported entanglement and measurement results

### Peres1996 and PPT1996

**Asher Peres, “Separability Criterion for Density Matrices,” Physical Review Letters 77, 1413–1415 (1996)** [Peres1996]. [Publisher](https://doi.org/10.1103/PhysRevLett.77.1413), [primary preprint](https://arxiv.org/abs/quant-ph/9604005).

**Michał Horodecki, Paweł Horodecki, and Ryszard Horodecki, “Separability of Mixed States: Necessary and Sufficient Conditions” (1996)** [PPT1996]. [Publisher](https://doi.org/10.1016/S0375-9601(96)00706-2), [primary preprint](https://arxiv.org/abs/quant-ph/9605038).

Peres supplies necessity of positivity under partial transposition. The Horodecki paper establishes sufficiency in $2\times2$ and $2\times3$. This project imports that equivalence. It does not assume PPT is sufficient in higher dimensions.

### Augusiak2008

**Remigiusz Augusiak, Maciej Demianowicz, and Paweł Horodecki, “Universal observable detecting all two-qubit entanglement and determinant based separability tests,” Physical Review A 77, 030301(R) (2008)** [Augusiak2008]. [Publisher](https://doi.org/10.1103/PhysRevA.77.030301), [primary preprint, v2](https://arxiv.org/abs/quant-ph/0604109v2).

This is the original universal four-copy determinant observable and the criterion

$$
\rho\text{ is entangled}\quad\Longleftrightarrow\quad\det(\rho^\Gamma)<0
$$

for two qubits. The paper also supplies the quantitative input used here: Eqs. (3) and (5) define $\pi_2(\rho)=2|\det(\rho^\Gamma)|^{1/4}$ on entangled states and prove $C(\rho)\le\pi_2(\rho)$, with continuity covering singular states. Its discussion asks about higher-dimensional universal collective observables.

The determinant construction, its sufficiency, and this concurrence bound are established results. The present project studies necessity, polynomial rigidity, retained output minima, and the statistical consequences of requiring exact universality.

### Wootters1998 and Demianowicz2011

**William K. Wootters, “Entanglement of Formation of an Arbitrary State of Two Qubits,” Physical Review Letters 80, 2245–2248 (1998)** [Wootters1998]. [Publisher](https://doi.org/10.1103/PhysRevLett.80.2245), [primary preprint](https://arxiv.org/abs/quant-ph/9709029).

The two-qubit concurrence and optimal pure-state decompositions are imported from this work. The trace-distance estimate used in this repository is derived explicitly by combining a pure-state bound with the convex-roof construction; it is not attributed to Wootters as a separate stated theorem.

**Maciej Demianowicz, “Reexamination of determinant-based separability test for two qubits,” Physical Review A 83, 034301 (2011)** [Demianowicz2011]. [Publisher](https://doi.org/10.1103/PhysRevA.83.034301), [primary preprint](https://arxiv.org/pdf/1010.0395).

This single-author paper further analyzes the determinant-based entanglement quantity and its relationship to concurrence. It is useful follow-up literature; the concurrence bound needed here is already present in [Augusiak2008].

### Brun2004 and Leifer2004

**Todd A. Brun, “Measuring polynomial functions of states,” Quantum Information and Computation 4(5), 401–408 (2004)** [Brun2004]. [Publisher](https://doi.org/10.26421/QIC4.5-6), [primary preprint](https://arxiv.org/abs/quant-ph/0401067).

Brun shows how degree-$k$ polynomial functions of density-matrix entries can be measured on $k$ copies. For a real polynomial, the corresponding observable can be chosen Hermitian. The polynomial-to-collective-observable correspondence is therefore established background. This project's conversion of several bounded Hermitian observables into one finite-outcome POVM is stated explicitly in its measurement model.

**M. S. Leifer, N. Linden, and A. Winter, “Measuring Polynomial Invariants of Multi-Party Quantum States,” Physical Review A 69, 052304 (2004)** [Leifer2004]. [Publisher](https://doi.org/10.1103/PhysRevA.69.052304), [primary preprint](https://arxiv.org/pdf/quant-ph/0308008).

This work constructs invariant-measurement networks. Section VII also analyzes their sampling efficiency: a binary circuit encoding an invariant through $p=(1+F)/2$ has variance $(1-F^2)/N$ for the inferred invariant after $N$ runs. Thus the distinction between few measured parameters and few samples is already explicit in the literature.

### Cerf1999

**N. J. Cerf, C. Adami, and R. M. Gingrich, “Reduction criterion for separability,” Physical Review A 60, 898–909 (1999)** [Cerf1999]. [Publisher](https://doi.org/10.1103/PhysRevA.60.898), [authors' institutional record and published PDF](https://authors.library.caltech.edu/records/67hpc-5y923).

When the transposed subsystem is a qubit, the reduction operator $I_2\otimes\rho_B-\rho$ is unitarily equivalent to the partial transpose. That identity and the resulting low-dimensional completeness of the reduction criterion are prior results. The weighted-adjugate statistic used in this repository is a further construction based on this identity.

## Imported algebraic geometry

### Djokovic2006

**Dragomir Z. Đoković, “Multigraded Poincaré series for mixed states of two qubits and the boundary of the set of separable states” (2006)** [Djokovic2006]. [Primary preprint, v2](https://arxiv.org/abs/quant-ph/0604190v2).

Section 3 describes the two-qubit separable boundary using the determinant hypersurfaces of $\rho$ and $\rho^\Gamma$. Proposition 3.1 identifies the singular determinant stratum, and Theorem 3.3 proves smoothness of the separable boundary inside the full-rank state space. This boundary geometry precedes the present work. It does not itself state a rigidity theorem for an arbitrary polynomial scalar classifier.

### BrunsVetter1988

**Winfried Bruns and Udo Vetter, Determinantal Rings, Lecture Notes in Mathematics 1327, Springer (1988)** [BrunsVetter1988]. [Publisher](https://doi.org/10.1007/BFb0080378), [author-hosted text](https://www.home.uni-osnabrueck.de/wbruns/brunsw/detrings.pdf).

Theorem 2.10 proves primality of the ideal of maximal minors of a generic matrix over an integral domain. Remark 2.12 extends the statement to arbitrary minor size. These results provide the standard irreducibility input for generic determinantal varieties. The passage to trace-one Hermitian coordinates and the continuation from physical boundary strata are justified in the project proofs; they are not automatic consequences of an arbitrary hyperplane section being irreducible.

## Complete families and the qubit–qutrit comparison

### ZhangXie2026

**Lin Zhang and Bing Xie, “Bargmann Invariants Are Insufficient for Complete Local-Unitary Orbit Discrimination,” arXiv:2609.11090v1 (2026)** [ZhangXie2026]. [Primary full text](https://arxiv.org/html/2609.11090v1).

Theorem 4 gives a complete qubit–qutrit test through the four inequalities $e_3,e_4,e_5,e_6\ge0$ for the partial transpose, expressed using moments through order six and marginal trace words. It does not assert that four statistics are minimal. The paper's impossibility results restrict the ordinary marginal-word Bargmann algebra; they do not exclude arbitrary polynomial readouts.

This is a direct comparison for the present three-statistic construction. The all-degree lower bound in this repository concerns arbitrary polynomial outputs, and the six-copy upper bound uses a different decision triple.

### Fraser2026 and ChenDjokovic2013

**Thomas C. Fraser, Vjosa Blakaj, Roberto Rubboli, Felix Huber, and Marco Fanizza, “Complete entanglement detection using polynomial invariants,” arXiv:2606.16712v1 (2026)** [Fraser2026]. [Primary full text](https://arxiv.org/html/2606.16712v1).

This work constructs a complete family of invariant nonlinear witnesses using tensor powers. Completeness of a family does not imply that its information can be retained in one polynomial expectation value.

**Lin Chen and Dragomir Z. Đoković, “Dimensions, lengths and separability in finite-dimensional quantum systems,” Journal of Mathematical Physics 54, 022201 (2013)** [ChenDjokovic2013]. [Publisher](https://doi.org/10.1063/1.4790405), [primary preprint, v4](https://arxiv.org/abs/1206.3775v4).

Corollary 3 proves semialgebraicity of the separable set. Conjectures 4 and 5 separately formulate stronger descriptions by finite conjunctions of polynomial inequalities. This distinction matters: a finite Boolean polynomial description is not, by itself, a proof of a single polynomial classifier or a finite conjunction of individually nonnegative witnesses. The low-dimensional constructions here use explicit PPT criteria and do not need such an inference.

## Single-copy and few-copy measurement comparisons

### Carmeli2016

**Claudio Carmeli, Teiko Heinosaari, Antti Karlsson, Jussi Schultz, and Alessandro Toigo, “Verifying the Quantumness of Bipartite Correlations,” Physical Review Letters 116, 230403 (2016)** [Carmeli2016]. [Publisher](https://doi.org/10.1103/PhysRevLett.116.230403), [primary preprint](https://arxiv.org/pdf/1510.03240).

The tomography necessity concerns single-copy measurements. The collective-measurement discussion explicitly recognizes the binary four-copy two-qubit determinant protocol. This is historical context for the resource question, not an all-copy scalar impossibility theorem.

### Lu2016

**Dawei Lu et al., “Tomography is necessary for universal entanglement detection with single-copy observables,” Physical Review Letters 116, 230501 (2016)** [Lu2016]. [Publisher](https://doi.org/10.1103/PhysRevLett.116.230501), [primary preprint](https://arxiv.org/abs/1511.00581).

The nonadaptive no-go restricts measurements to single copies. It does not rule out polynomial statistics measured collectively on a finite block.

### Bartkiewicz2015 and Goswami2019

| Reference | Retained information and scope |
| --- | --- |
| Karol Bartkiewicz et al., “Method for universal detection of two-photon polarization entanglement,” Physical Review A 91, 032315 (2015) [Bartkiewicz2015]. [Publisher](https://doi.org/10.1103/PhysRevA.91.032315), [primary text](https://arxiv.org/pdf/1405.5560). | The optical construction measures several invariant combinations and normalization quantities. Its optimality discussion concerns its modular optical architecture. |
| Suchetana Goswami et al., “Universal detection of entanglement in two-qubit states using only two copies,” Physical Review A 99, 012327 (2019) [Goswami2019]. [Publisher](https://doi.org/10.1103/PhysRevA.99.012327), [primary text](https://arxiv.org/pdf/1808.08246). | The two-copy weak-value protocol retains multiple postselection outcomes, probabilities, and pointer shifts; it permits complete state identification. One postselection setting does not mean one retained binary probability. |

These results are compatible with a four-copy minimum specifically for an exactly universal binary apparatus.

## Statistical precursors and the fixed-apparatus restriction

### Genoni2008

**Marco G. Genoni, Paolo Giorda, and Matteo G. A. Paris, “Optimal estimation of entanglement,” Physical Review A 78, 032303 (2008)** [Genoni2008]. [Publisher](https://doi.org/10.1103/PhysRevA.78.032303), [primary text](https://arxiv.org/pdf/0804.1705).

This paper studies local quantum estimation, optimal observables, and the difficulty of estimating weak entanglement for selected families. The measurements and promises differ from a fixed binary apparatus required to classify every mixed state. Difficulty near weak entanglement is therefore prior art; the present theorem identifies a specific penalty imposed by exact universal readout.

### LiuWei2025

**Zhenhuan Liu and Fuchuan Wei, “Separation between entanglement criteria and entanglement detection protocols,” Physical Review Research 7, 033121 (2025)** [LiuWei2025]. [Published full text](https://journals.aps.org/prresearch/pdf/10.1103/hm8j-wgqm), [publisher](https://doi.org/10.1103/hm8j-wgqm), [earlier preprint](https://arxiv.org/abs/2403.01664).

The published paper demonstrates a separation between criterion complexity and detection-protocol sample complexity in growing dimension, with specified random-state priors and adaptive single-copy protocols. It also discusses the benefits of collective measurements. This establishes a related statistical distinction, but does not give the fixed-dimensional, distance-to-SEP minimax theorem for an exactly universal binary collective detector studied here. Comparisons should use the published version; the initial preprint has different theorem constants.

The repository's $\delta^{-8}$ repetition law is conditional on exact universal binary readout at fixed block size. It is not a lower bound for general entanglement detection, protocols retaining more outputs, or apparatuses required to solve only a specified nonzero-gap promise. The distinction between readout count and sample cost is already present in [Leifer2004] and [LiuWei2025].

### Haah2017

**Jeongwan Haah, Aram W. Harrow, Zhengfeng Ji, Xiaodi Wu, and Nengkun Yu, “Sample-optimal tomography of quantum states,” IEEE Transactions on Information Theory 63(9), 5628–5641 (2017)** [Haah2017]. [Publisher](https://doi.org/10.1109/TIT.2017.2719044), [primary preprint, v2](https://arxiv.org/abs/1508.01797v2).

This is background on the copy complexity of state estimation. The fixed-dimensional comparison in [Sampling cost](../science/sampling_cost.md) supplies its own elementary Pauli-estimation upper bound and commuting-state lower bound. It is not attributed to the tomography paper as a universal-binary entanglement theorem.

## Approximation theory used for the promise-gap block bound

### Sherstov2013

**Alexander A. Sherstov, “The Intersection of Two Halfspaces Has High Threshold Degree,” SIAM Journal on Computing 42(6), 2329–2374 (2013)** [Sherstov2013]. [Publisher](https://doi.org/10.1137/100785260), [author-hosted text](https://web.cs.ucla.edu/~sherstov/pdf/hshs.pdf).

Theorem 1.10, on page 6 of the author-hosted manuscript, proves

$$
\deg_{\pm}(\mathrm{MAJ}_n\wedge\mathrm{MAJ}_n)=\Omega(\log n)
$$

for two independent majorities on disjoint variables, with a matching upper bound discussed there. The paper also develops the relevant relation between rational approximation and polynomial sign representation.

This project imports that threshold-degree theorem. Its additional step is the physical qubit–qutrit embedding and the conversion of arbitrary scalar postprocessing into a sign-representing polynomial. A logarithmic optimal block size permits a small output-probability margin and does not imply a logarithmic total-copy cost.

## Scope of the novelty review

The review followed the determinant-observable literature, its geometric and measurement descendants, recent polynomial witness families, and the statistical and threshold-degree connections above. Among the primary sources inspected, none states this repository's exact three-statistic/four-outcome qubit–qutrit theorem or its universal binary rigidity and repetition theorem.

This is a bounded comparison, not an exhaustive priority determination. Complete cited-by lists were not accessible, some experimental descendants were screened only through abstracts, and the unpublished higher-dimensional follow-up mentioned in [Demianowicz2011] was not independently resolved. The repository therefore avoids categorical first-result claims. The explicit constructions and proofs should be assessed independently of this literature-search limitation.
