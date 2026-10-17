# Universal Entanglement Readout

**How much information must one fixed collective apparatus retain to detect every entangled mixed state?** This project gives attained outcome minima in the smallest bipartite dimensions and a sharp statistical cost for the binary two-qubit exception.

Each run applies the same state-independent POVM to a fixed finite number of independent copies. The exact classification results allow arbitrary classical processing of the true outcome probabilities.

| Input states | Minimum outcomes per run | Sufficient copies per run |
|---|---:|---:|
| Arbitrary two-qubit states | **2** | **4** |
| Qubit–qutrit states with an invertible qutrit marginal | **3** | **6** |
| Arbitrary qubit–qutrit states | **4** | **6** |

The four-copy two-qubit detector is [established prior work](references/RELATED_WORK.md#augusiak2008). The outcome lower bounds permit every finite block size, and the six-copy qubit–qutrit constructions are explicit upper bounds. The four-outcome lower bound also embeds into every other nontrivial bipartite dimension except $2\times2$; sufficiency of four outcomes is established here for $2\times3$.

For exactly universal binary two-qubit detectors at any fixed block size $k\ge4$, the best worst-case repetition count for a half-trace-distance gap $\delta$ and error target $0<\eta\le1/4$ is

$$
n_{\mathrm{univ},k}(\delta,\eta)
=\Theta_k\!\left(\delta^{-8}\log\frac1\eta\right).
$$

Every such probability polynomial obeys

$$
p_E(\rho)=c+\det(\rho^\Gamma)q(\rho).
$$

The determinant factor forces at least fourth-order flatness along a weakly entangled pure-state path. An effect-independent information bound gives the repetition lower bound, and a normalized four-copy determinant measurement attains its exponent. The requirement of exact universality on all mixed states is essential. This is distinct from unrestricted entanglement testing, whose fixed-dimensional total-copy benchmark is derived in the statistical account.

## Read the science

Start with the [manuscript account](manuscript/main.md) for the question, mechanism, and connected argument. The [model and exact claims](science/model.md) provide the canonical assumptions and resource definitions.

| To inspect | Read |
|---|---|
| Minimum outcomes and all rank branches | [Outcome minima](science/outcome_minima.md) |
| Explicit six-copy observables and positive POVM effects | [Collective measurements](science/collective_measurements.md) |
| Universal determinant factorization and four-copy necessity | [Binary rigidity](science/binary_rigidity.md) |
| Sharp repetition law and unrestricted comparison | [Sampling cost](science/sampling_cost.md) |
| Binary block size under a nonzero distance promise | [Supporting promise-gap theorem](science/promise_gap.md) |
| Established ingredients and nearby measurement models | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Exact calculations and their scope | [Verification](verification/README.md) |

The supporting qubit–qutrit promise-gap theorem gives a minimum binary block size proportional to $\log(1/\delta)$ when arbitrarily fine probability resolution is permitted. Its probability margin is not controlled, so this is a block-size result rather than a total-sampling bound.

## Learn the project

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [Watrous bridge](learning/WATROUS_BRIDGE.md) identifies the relevant sections of the author's available manuscript, translates the notation, and develops the connections to this project's geometric and statistical arguments.

The [30-milestone map](learning/MILESTONES.md) gives a common route through the whole project. Its **12 background/preliminaries milestones** build the operational framework; its **18 narrative/innovation milestones** connect the proof mechanisms to the attained hierarchy and its resource consequences. The targets depend on the project, while explanations and examples can adapt to the reader.

For guided study, the [coaching guide](learning/COACHING.md) specifies Revise → Learn → Test, the initial two-question challenge, targeted learning after an unsuccessful attempt, and the all-correct retry rule. [The LLM reading guide](llms.txt) connects these learning materials to the authoritative scientific files. Specialists can use the direct proof route above.

## Reproduce the finite checks

From the repository root, run:

```bash
python3 verification/run_all.py
```

The suite uses only Python's standard library and compares deterministic exact-arithmetic results with the committed outputs. It checks the physical corner, rank-sensitive criterion, binary observable certificate, rational filter, and collective measurement contractions. General converses and asymptotic laws are established by the written proofs and cited theorems, not by finite enumeration.

## Scope

The measurements are global and state independent. No QRAM, efficient gate decomposition, or minimal six-copy implementation is assumed. Exact identifiability and finite-sample guarantees are separate statements. The three-outcome rank promise, the fixed block size in the sampling law, and the statistical-margin limitation in the supporting theorem remain part of the claims.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
