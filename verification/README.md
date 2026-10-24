# Exact verification

The checks here verify finite ingredients of the analytical arguments. They use integer arithmetic and `fractions.Fraction`, with no numerical eigensolver or tolerance. They are not a substitute for the general proofs.

## Run from a fresh checkout

Python 3.10 or later is sufficient; no third-party package or network access is needed. From the repository root:

```bash
python3 verification/run_all.py
```

The command computes every result and compares it with the corresponding committed JSON in [expected](expected/). It exits with an error if an assertion fails, a reference output is missing, or the newly computed result differs. The default command does not rewrite the reference outputs. Standard Python assertions must be enabled; the runner rejects optimized mode.

For a scientifically reviewed change to a calculation, regenerate the deterministic outputs explicitly:

```bash
python3 verification/run_all.py --record
python3 verification/run_all.py
```

Recording an output is not an independent validation step. Inspect the changed calculation and its scientific meaning before accepting the new reference.

## What is checked

| Script | Exact finite evidence | Analytical claim it supports |
|---|---|---|
| [verify_corner.py](verify_corner.py) | Gaussian-integer product vectors; the $`6\times6`$ matrix and its positive leading minors; rank-four partial transpose; positivity at all four rational corners; exact normal eigenvectors | The full-rank physical quadrant used in the scalar and two-coordinate obstructions |
| [verify_outcome_criterion.py](verify_outcome_criterion.py) | Nineteen states covering marginal rank, partial-transpose rank, positive and negative signs, and the entangled equality case with $`f\gt0,g=0`$ | The three-statistic decision rule and its promised-rank restriction |
| [verify_binary_detector.py](verify_binary_detector.py) | The full-rank two-qubit boundary state; the integer antisymmetric Schmidt matrix and its Gram identity; three rational pure-state determinant examples | The binary normalization and the exact fourth-power hard family |
| [verify_gap_filter.py](verify_gap_filter.py) | Four geometric resolutions; 2,401 four-coordinate combinations; nine physical state examples; exact filter signs, oddness, and bounds | The explicit filter used in the promise-gap upper construction |
| [verify_collective_measurements.py](verify_collective_measurements.py) | All 36 one-copy matrix units for the linear maps; antisymmetrizer traces; six state contractions, including noncommuting $`D,H`$; the derivative factor six; rational positivity scales | The explicit six-copy observables and the accounting of the adjugate statistic |

The matrix-unit check extends by linearity to complex one-copy operators. The contraction examples themselves use real rational states. Universal six-copy effect positivity comes from the [operator-norm proof](../science/collective_measurements.md), which acts on the entire Hilbert space. Checking expectation values on selected inputs would not establish that positivity.

The binary spectrum follows analytically from the exact Gram identity and the spectrum of the partial transpose of a pure projector. The script does not diagonalize a dense $`256\times256`$ operator numerically. The larger six-copy effects are specified by permutation and reduction formulas; their dense matrices are not needed for these checks.

## What requires proofs or external sources

The following statements are not certified by enumerating these examples:

- The analytic scalar quadrant obstruction, Schur-complement argument, and polynomial continuation for arbitrary input states.
- Absolute irreducibility on the trace-one affine space and continuation from a smooth real boundary patch.
- Uniform minimax information bounds and the confidence dependence of the repetition law.
- The threshold-degree theorem imported from Sherstov and the asymptotic promise-gap lower bound.
- Completeness of the low-dimensional PPT criterion, the imported determinant–concurrence bound, or bibliographic priority.

Those dependencies are proved in the [science pages](../science/model.md) or attributed in [Related work](../references/RELATED_WORK.md). No claim of experimental validation or external peer review follows from this suite.

## Current sanity-check record

The review on **24 October 2026** inspected scientific revision `b29a9d73a886bffb940fe3020330ab4b165fde95` and the accompanying literature-only refresh. It found no confirmed defect in R1, R2, R3 or S1. The review reconstructed the outcome obstructions and rank-sensitive criterion, determinant divisibility, collective-observable normalization and positivity, uniform statistical bounds, and promise-gap reduction. It checked the imported determinant–concurrence inequality and Sherstov's Theorem 1.10 against their primary texts.

All five exact checks reproduced their committed JSON under Python 3.12.14. In isolated temporary copies, missing or altered reference outputs, an injected failed assertion, and optimized Python mode each caused a nonzero exit; execution from an unrelated working directory succeeded. The learning review confirmed exactly M01–M30, the 12/18 phase allocation, strictly earlier prerequisites, valid local links and anchors, and the cited Watrous section and theorem pointers.

GitHub's hosted renderer was visually inspected on the [README](../README.md), [Watrous bridge](../learning/WATROUS_BRIDGE.md), [milestone map](../learning/MILESTONES.md), [outcome proof](../science/outcome_minima.md), and [sampling proof](../science/sampling_cost.md). The inspected views included result tables, the physical-corner matrix, partial transpose, antisymmetric-projector notation, bra–ket expressions, and statistical formulas. No display error was found in those views; this was not a screenshot inspection of every equation.

The refreshed [literature comparison](../references/RELATED_WORK.md) distinguishes target-dependent geometric witnesses and adaptive two-copy estimation from the fixed universal apparatus. This internal review and bounded literature search do not certify exhaustive priority or replace independent expert review.
