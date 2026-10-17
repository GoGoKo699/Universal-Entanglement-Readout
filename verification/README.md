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
| [verify_corner.py](verify_corner.py) | Gaussian-integer product vectors; the $6\times6$ matrix and its positive leading minors; rank-four partial transpose; positivity at all four rational corners; exact normal eigenvectors | The full-rank physical quadrant used in the scalar and two-coordinate obstructions |
| [verify_outcome_criterion.py](verify_outcome_criterion.py) | Nineteen states covering marginal rank, partial-transpose rank, positive and negative signs, and the entangled equality case with $f>0,g=0$ | The three-statistic decision rule and its promised-rank restriction |
| [verify_binary_detector.py](verify_binary_detector.py) | The full-rank two-qubit boundary state; the integer antisymmetric Schmidt matrix and its Gram identity; three rational pure-state determinant examples | The binary normalization and the exact fourth-power hard family |
| [verify_gap_filter.py](verify_gap_filter.py) | Four geometric resolutions; 2,401 four-coordinate combinations; nine physical state examples; exact filter signs, oddness, and bounds | The explicit filter used in the promise-gap upper construction |
| [verify_collective_measurements.py](verify_collective_measurements.py) | All 36 one-copy matrix units for the linear maps; antisymmetrizer traces; six state contractions, including noncommuting $D,H$; the derivative factor six; rational positivity scales | The explicit six-copy observables and the accounting of the adjugate statistic |

The matrix-unit check extends by linearity to complex one-copy operators. The contraction examples themselves use real rational states. Universal six-copy effect positivity comes from the [operator-norm proof](../science/collective_measurements.md), which acts on the entire Hilbert space. Checking expectation values on selected inputs would not establish that positivity.

The binary spectrum follows analytically from the exact Gram identity and the spectrum of the partial transpose of a pure projector. The script does not diagonalize a dense $256\times256$ operator numerically. The larger six-copy effects are specified by permutation and reduction formulas; their dense matrices are not needed for these checks.

## What requires proofs or external sources

The following statements are not certified by enumerating these examples:

- The analytic scalar quadrant obstruction, Schur-complement argument, and polynomial continuation for arbitrary input states.
- Absolute irreducibility on the trace-one affine space and continuation from a smooth real boundary patch.
- Uniform minimax information bounds and the confidence dependence of the repetition law.
- The threshold-degree theorem imported from Sherstov and the asymptotic promise-gap lower bound.
- Completeness of the low-dimensional PPT criterion, the imported determinant–concurrence bound, or bibliographic priority.

Those dependencies are proved in the [science pages](../science/model.md) or attributed in [Related work](../references/RELATED_WORK.md). No claim of experimental validation or external peer review follows from this suite.
