# From Watrous to universal entanglement readout

A source repeatedly supplies the same unknown bipartite state. A collective
apparatus consumes several copies and produces one classical label. This
project asks how much of the apparatus's output distribution must be retained
to determine separability, and what statistical cost follows when the retained
distribution is binary.

The selected educational anchor is **John Watrous, The Theory of Quantum
Information**, Cambridge University Press, 2018. Section references below
refer to the author's **2018 prepublication manuscript**, whose front matter
is dated January 2018. The author identifies the published book as appearing
in April 2018. Use the [author's page](https://cs.uwaterloo.ca/~watrous/TQI/)
and its [manuscript contents](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf)
to locate the readings. The manuscript is linked, not reproduced in this
repository.

Watrous supplies the quantum-information foundations. This bridge supplies
the project-specific connections to polynomial classification, boundary
geometry, and statistical lower bounds. The [30-milestone map](MILESTONES.md)
organizes the complete understanding route; the [model](../science/model.md)
owns the exact theorem domains and resource definitions.

## Targeted reading from the single anchor

Use these sections alongside the relevant milestones. They are focused
lookups within one source, not a requirement to finish the book first.

| Project use | Watrous manuscript sections | What to bring into this project |
|---|---|---|
| States, separability, and rank, M01–M04 | [Sections 2.1.2–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [Sections 6.1.1 and 6.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf) | Density operators, partial trace, separable convex combinations, and the PPT condition. |
| Physical apparatus and retained labels, M05 | [Sections 2.2.1–2.2.2 and 2.3.1–2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Channels, POVMs, and measurement records. Theorem 2.37 relates measurements to channels with classical output; Theorem 2.42 gives the measurement dilation. |
| Tensor observables and their normalization, M06–M07 | [Sections 1.1.2–1.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [Sections 7.1.1–7.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) | Tensor products, operator norms, antisymmetric subspaces, and permutation averaging. |
| Trace distance and witnesses, M08 | [Section 1.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [Section 3.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | Norm duality and the operational role of state distinguishability. Theorem 3.4 is the Holevo–Helstrom theorem. |
| The separable boundary, M09–M10 | [Section 1.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [Sections 6.1.1 and 6.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf) | Convexity, separability, and partial transposition. The analytic and algebraic continuation arguments are supplied in the project proofs. |
| Probability gaps and information, M11 | [Sections 5.1.1–5.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf) | Classical relative entropy as a measure of distinguishability between output distributions. |
| The unrestricted statistical comparison, M26 | [Section 5.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf) | Theorem 5.35 gives quantum relative-entropy monotonicity under channels. |
| Integrating the operational question, M12, and the final story, M30 | [Model and exact claims](../science/model.md) and [resource interpretation](../science/interpretation.md) | Combine the foundations with the actual apparatus restrictions and proved conclusions. |

Section 6.1.1 gives the separable-state framework, including compactness and
convexity. Section 6.2.3 introduces the PPT framework and its limitations.
The dimension-specific equivalence between PPT and separability in
$`2\times2`$ and $`2\times3`$ is an imported research theorem, attributed in
[Related work](../references/RELATED_WORK.md#peres1996-and-ppt1996).
The project does not extend that equivalence to arbitrary local dimensions.

## Notation and conventions

Watrous uses column vectors and adjoints where the project sometimes uses
Dirac notation. The mathematical objects are the same.

| Watrous notation or convention | Project notation or convention | Meaning |
|---|---|---|
| $`\mathcal X\otimes\mathcal Y`$ | $`\mathcal H=\mathbb C^{d_A}\otimes\mathbb C^{d_B}`$ | One bipartite input space. |
| $`u`$, $`u^*`$, $`uu^*`$ | $`\lvert\psi\rangle`$, $`\langle\psi\rvert`$, $`\lvert\psi\rangle\langle\psi\rvert`$ | A vector, its adjoint, and its pure-state projector. |
| $`\mu(j)`$ | $`E_j`$ | The positive effect associated with a retained outcome. |
| $`\mathrm{SepD}(\mathcal X:\mathcal Y)`$ | $`\mathrm{SEP}`$ | Normalized separable states, rather than the full cone of separable positive operators. |
| $`(T\otimes\mathrm{id})(\rho)`$ | $`\rho^\Gamma`$ | Partial transpose on the first subsystem in a fixed product basis. |
| $`\lVert X\rVert_1,\lVert X\rVert_2,\lVert X\rVert_\infty`$ | The same Schatten norms | Trace, Hilbert–Schmidt, and operator norm, respectively. |

In the qubit–qutrit formulas, the symbol $`B`$ denotes the **matrix**
$`B=\mathrm{Tr}_A\rho`$, and $`D=I_2\otimes B`$. This marginal is normalized:
$`\mathrm{Tr}B=1`$. Partial traces are ordinary, unnormalized linear maps;
there is no extra factor of $`1/2`$ in $`D`$.

The project measures distance to separability by

```math
\Delta(\rho)=\inf_{\sigma\in\mathrm{SEP}}
\frac12\lVert\rho-\sigma\rVert_1.
```

The factor $`1/2`$ matters when converting a witness estimate into a distance
bound. Watrous uses base-two logarithms for relative entropy, as specified at
the beginning of Section 5.1.1. The sampling proof uses natural logarithms.
Thus, for probability vectors,

```math
D_{\mathrm{KL}}^{\mathrm{project}}(p\Vert q)
=(\ln2)\,D^{\mathrm{Watrous}}(p\Vert q).
```

This changes numerical constants expressed in bits or nats, not the powers
of the promised distance.

## One fixed apparatus and its complete record

For [M05](MILESTONES.md#m05-a-fixed-povm-and-its-complete-record) and
[M12](MILESTONES.md#m12-the-complete-operational-question), begin with
$`k`$ independent copies, $`\rho^{\otimes k}`$, and fixed effects
$`E_1,\ldots,E_m`$ satisfying

```math
E_j\ge0,\qquad \sum_{j=1}^mE_j=I,\qquad
p_j(\rho)=\mathrm{Tr}(E_j\rho^{\otimes k}).
```

A fixed ancilla and fixed processing inside the apparatus are absorbed into
these effects. The source state remains unknown, and the apparatus cannot
select a state-dependent observable using an uncounted measurement record.
Because the probabilities sum to one, $`m-1`$ real coordinates specify the
complete distribution. This count does not require those coordinates to be
algebraically independent.

For example, suppose a fair coin selects between two binary measurements
with outcome-one probabilities $`u(\rho)`$ and $`v(\rho)`$. Retaining both the
setting and the binary outcome gives the four-symbol distribution

```math
\left(\frac{u}{2},\frac{1-u}{2},
\frac{v}{2},\frac{1-v}{2}\right).
```

This record recovers both $`u`$ and $`v`$. Retaining only the binary outcome gives
the single probability $`(u+v)/2`$, which generally loses that information.
The fixed setting probabilities cause some coordinate redundancy, but the
complete labeled record still has four outcome labels. The same accounting
applies to success flags and conditional records used by a decision rule.

The final decision is always a binary statement, separable or entangled.
That fact does not determine how many outcome labels the apparatus retained.
Exact universality instead requires the probability images of the two state
classes to be disjoint. A decision function can then assign the correct
label to every true probability vector. The function may be discontinuous.

This is an identifiability statement. One observed label, or any fixed finite
sample, does not reveal an arbitrary probability vector exactly. The
statistical question introduces a positive distance promise and a target
error probability separately.

## Tensor copies turn polynomial statistics into observables

The connection in [M06](MILESTONES.md#m06-polynomial-degree-and-collective-realization)
starts with the trace identity

```math
\mathrm{Tr}\bigl[(F\otimes G)(\rho\otimes\rho)\bigr]
=\mathrm{Tr}(F\rho)\mathrm{Tr}(G\rho).
```

A quadratic expression in single-copy expectation values is therefore a
linear expectation on two copies. More generally, choose a Hermitian
coordinate basis, so that each real coordinate is
$`x_\alpha(\rho)=\mathrm{Tr}(F_\alpha\rho)`$. A monomial of degree $`r`$
has the representation

```math
\prod_{j=1}^{r}x_{\alpha_j}(\rho)
=\mathrm{Tr}\left[
\left(F_{\alpha_1}\otimes\cdots\otimes F_{\alpha_r}
\otimes I^{\otimes(k-r)}\right)\rho^{\otimes k}
\right]
```

for every $`k\ge r`$. Identity factors supply the lower-degree terms because
$`\mathrm{Tr}\rho=1`$. Adding the monomials with their real coefficients
gives a fixed Hermitian $`W_q`$ representing any real polynomial $`q`$ of degree
at most $`k`$:

```math
q(\rho)=\mathrm{Tr}(W_q\rho^{\otimes k}).
```

The converse is immediate by expanding $`\rho^{\otimes k}`$ in coordinates:
every fixed $`k`$-copy outcome probability is a polynomial of degree at most
$`k`$ on the trace-one affine space. The established collective-measurement
principle is credited to Brun and related direct-measurement work in
[the source account](../references/RELATED_WORK.md#brun2004-and-leifer2004).

A Hermitian representative becomes a binary effect once its full operator
norm is controlled. If $`M\ge\max\{1,\lVert W_q\rVert_\infty\}`$, then

```math
E_q=\frac I2+\frac{W_q}{2M},\qquad
0\le E_q\le I,\qquad
p_{E_q}(\rho)=\frac12+\frac{q(\rho)}{2M}.
```

For a finite family of polynomials, distribute a fixed identity baseline
among one more effect than the number of statistics, and choose a common
scale small enough to keep all effects positive. The
[collective measurement proof](../science/collective_measurements.md#general-polynomial-to-observable-lemma)
gives an explicit coefficient bound and that construction.

Two kinds of bound have distinct roles. A bound on $`q(\rho)`$ concerns
expectations on identical input tensors. Positivity of the measurement
requires a bound on $`W_q`$ throughout the complete tensor-product Hilbert
space. The project provides such operator bounds for its explicit
measurements. Their existence and positivity do not by themselves establish
a large probability margin or a short implementation circuit.

## Partial transpose and antisymmetry in the construction

[M03](MILESTONES.md#m03-partial-transpose-and-the-dimension-boundary) uses
partial transpose as an entanglement criterion. For separable states,

```math
\rho=\sum_i t_i\,\rho_i^A\otimes\rho_i^B
\quad\Longrightarrow\quad
\rho^\Gamma=\sum_i t_i\,(\rho_i^A)^T\otimes\rho_i^B\ge0.
```

Here $`t_i\ge0`$ and $`\sum_i t_i=1`$. The converse holds in the two local
dimensions used for the constructive classification results. Complete
positivity, introduced in Watrous Chapter 2, explains why partial transpose
cannot be a general physical transformation of an unknown bipartite input.

The apparatus uses a different identity. Partial transpose is self-adjoint
under the trace pairing, so for any fixed Hermitian $`P`$ on $`r`$ copies,

```math
\mathrm{Tr}\bigl[P(\rho^\Gamma)^{\otimes r}\bigr]
=\mathrm{Tr}\bigl[P^{\Gamma_{A_1\cdots A_r}}\rho^{\otimes r}\bigr].
```

Thus partial transpose can be applied algebraically to the known observable
when defining a measurement. The resulting Hermitian operator is shifted
and scaled into a positive effect as above. No unknown state is physically
partially transposed.

For [M07](MILESTONES.md#m07-spectral-coefficients-and-antisymmetric-observables),
Watrous Section 7.1.1 supplies the antisymmetric-subspace language. Let $`V_\pi`$
permute $`r`$ whole copies, and define

```math
A_r=\frac1{r!}\sum_{\pi\in S_r}\mathrm{sgn}(\pi)V_\pi.
```

For a Hermitian $`d\times d`$ matrix $`X`$,

```math
\mathrm{Tr}(A_rX^{\otimes r})=e_r(X),\qquad r\le d.
```

To see this, diagonalize $`X`$. Each normalized wedge of $`r`$ distinct
eigenvectors contributes the product of its $`r`$ eigenvalues. Summing over
the wedges gives the elementary symmetric coefficient $`e_r`$. At $`r=d`$,
this is $`\det X`$, even when $`X`$ has negative eigenvalues. The project
uses the identity with matrices related to $`\rho^\Gamma`$.

The factor $`1/r!`$ makes $`A_r`$ a projector. For qubit–qutrit copies,
$`A_6`$ has rank one and $`A_4`$ has rank $`\binom64=15`$. These ranks enter the
operator-norm certificates in
[the six-copy construction](../science/collective_measurements.md#certified-operator-norm-bounds).
Permutation averaging also preserves every expectation on
$`\rho^{\otimes k}`$, a connection used later to identify the symmetric
four-copy effect.

## Marginal rank changes the complete criterion

The bridge from [M04](MILESTONES.md#m04-marginal-rank-and-physical-support)
to M17–M19 begins with the qubit–qutrit matrices

```math
B=\mathrm{Tr}_A\rho,\qquad D=I_2\otimes B,\qquad H=D-\rho.
```

The qubit reduction identity gives

```math
H=(\sigma_y\otimes I_3)\rho^\Gamma(\sigma_y\otimes I_3),
```

so $`H`$ and $`\rho^\Gamma`$ have the same eigenvalues. The complete
classification uses three polynomials:

```math
f=\det H,\qquad
g=\mathrm{Tr}[D\mathrm{adj}(H)],\qquad
h=e_4(H).
```

The adjugate is defined even when $`H`$ is singular. In particular,

```math
g=\left.\frac{d}{dt}\det(H+tD)\right|_{t=0}
```

is a polynomial identity with no matrix inverse.

When $`B\gt0`$, the proof forms
$`K=D^{-1/2}HD^{-1/2}`$. This congruence preserves the number of positive,
negative, and zero eigenvalues. It also gives $`K\le I`$ and
$`\mathrm{Tr}K=3`$. These spectral constraints leave only a few
possible ways for $`K`$ to have negative eigenvalues. The determinant and
the weighted derivative identify them:

```math
f=(\det B)^2\det K,\qquad
g=(\det B)^2e_5(K).
```

The resulting rule on this promised domain is

```math
\rho\in\mathrm{SEP}
\quad\Longleftrightarrow\quad
(f\gt0\text{ and }g\gt0)
\text{ or }(f=0\text{ and }g\ge0).
```

An NPT matrix can have two negative eigenvalues and a positive
determinant. The inertia argument in
[Outcome minima](../science/outcome_minima.md#invertible-qutrit-marginal)
shows how $`g`$ resolves that case. The inequality must be strict:
the [equality example](../science/outcome_minima.md#equality-cases-and-verification)
is an NPT state with $`(f,g,h)=(1/4096,0,-1/64)`$, so accepting
$`g=0`$ when $`f\gt0`$ would misclassify it.

When $`B`$ is singular, positivity of $`\rho`$ confines its support to
$`\mathbb C^2\otimes\mathrm{supp}B`$. If $`B`$ has rank two, this support
is a two-qubit space. The remaining two directions force $`f=g=0`$,
while $`h`$ is the determinant of the surviving four-dimensional block.
For instance, the Bell state embedded in that support has

```math
B=\mathrm{diag}(1/2,1/2,0),\qquad
(f,g,h)=(0,0,-1/16),
```

and is entangled. If $`B`$ has rank one, the state is a product and
$`f=g=h=0`$. The full-domain rule therefore includes the third statistic:

```math
\rho\in\mathrm{SEP}
\quad\Longleftrightarrow\quad
(f\gt0\text{ and }g\gt0)
\text{ or }
\bigl(f=0\text{ and }[g\gt0\text{ or }(g=0\text{ and }h\ge0)]\bigr).
```

Global positive definiteness implies $`B\gt0`$, while an invertible marginal
does not require the global state to be full rank. The state domain must
therefore be stated using the intended promise. The matrix $`K`$ is a proof
device; the implemented observables represent $`f,g,h`$ directly. They
require neither an estimate of $`B`$ nor state-dependent whitening.

## Why the outcome lower bounds require geometry

The quantum foundations lead to polynomial output coordinates, but their
minimum number depends on which separable and entangled states they can
identify. The two-qubit determinant already shows that a high-dimensional
state can have a property classified by one scalar. A count of state
parameters alone does not decide the present question.

### A scalar cannot encode a physical corner

For [M09](MILESTONES.md#m09-analytic-geometry-of-a-scalar-image) and
M13–M14, the project constructs a full-rank qubit–qutrit family
$`\rho(s,t)`$ on a small square. Its partial transpose has eigenvalues
$`s,t`$ and four positive eigenvalues. Hence

```math
\rho(s,t)\in\mathrm{SEP}\quad\Longleftrightarrow\quad s\ge0,\ t\ge0.
```

Suppose an analytic scalar $`p(s,t)`$ classified this quadrant. Its image
on the compact nonnegative quadrant would be an interval $`[a,b]`$. An axis
point $`(0,t)`$ with $`t\gt0`$ is separable and is approached by entangled
points with $`s\lt0`$. Its scalar value must therefore be an endpoint.
If the value were in the interval's interior, sufficiently nearby
entangled points would also have values inside $`[a,b]`$.

Continuity makes the scalar constant along that connected positive
axis segment. Analytic continuation along the axis extends the same
value to negative $`t`$, where the state is entangled. The two classes
then share a probability value. This contradiction uses no regularity
assumption on the classical decision function.

The [explicit physical seed and proof](../science/outcome_minima.md#analytic-obstruction-at-a-separable-corner)
establish the family and the analytic lemma. The full-rank seed ensures
that the contradiction already occurs under an invertible-marginal
promise.

### Two coordinates lead to an identity on a rank stratum

For [M10](MILESTONES.md#m10-polynomial-identities-beyond-a-physical-patch)
and M15–M16, start on a physical patch where
$`\Lambda=\rho^\Gamma`$ is positive semidefinite of rank four and
$`\rho\gt0`$. If the first of two polynomial statistics varies along a
tangent direction of this patch, the implicit function theorem can
adjust that direction to hold the statistic constant. The second
statistic would then have to classify a two-dimensional diagonal
slice of the kernel block, which is exactly the quadrant above.
That is impossible. Both statistics must consequently be constant on
an open connected patch of the rank-four stratum.

The diagonal slice has two directions; it is not the full normal space
of the rank-four Hermitian stratum. The proof needs only this slice.
Its next step concerns polynomial identities rather than a physical
motion through states.

Let $`q(\Lambda)`$ be one output coordinate evaluated on
$`\rho=\Lambda^\Gamma`$, and let $`d`$ be any integer at least its degree.
If $`q=c`$ on the trace-one patch, trace homogenization produces a
polynomial

```math
P(X)=(\mathrm{Tr}X)^d
\left[q\left(\frac{X}{\mathrm{Tr}X}\right)-c\right].
```

After expansion, the denominators cancel. Factor a positive semidefinite
rank-four matrix as $`X=YY^\dagger`$, with $`Y`$ a complex $`6\times4`$ matrix. The
polynomial $`P(YY^\dagger)`$ vanishes on an open set of the real and
imaginary parts of $`Y`$, so it vanishes identically. Complexifying these
coordinates makes the two matrix factors independent and gives

```math
P(YZ^T)=0
```

for all complex $`6\times4`$ matrices $`Y,Z`$. Every matrix of rank at most
four has this form. The original constant values therefore extend to
trace-one Hermitian matrices of rank at most four, including indefinite
ones.

The embedded Bell state's partial transpose is such a rank-four
matrix, with spectrum $`-1/2,1/2,1/2,1/2,0,0`$. Both output coordinates
would equal their values on the separable patch. This proves the
stronger obstruction on all states. The contradiction uses a
singular-marginal state, explaining why the same argument does not
exclude the attained two-statistic criterion under $`B\gt0`$.

These analytic and algebraic steps are local project derivations in
[Outcome minima](../science/outcome_minima.md#two-polynomial-coordinates-are-insufficient-on-all-states).
They are not assertions that Watrous contains this converse.

## The two-qubit boundary forces a determinant factor

M21–M23 use a related boundary argument with a different algebraic
conclusion. For an exactly universal binary two-qubit probability,
the compact connected separable set has scalar image $`[a,b]`$. On a
connected smooth boundary patch approached by entangled states,
continuity forces the probability to equal one endpoint $`c`$ throughout
the patch.

In this case the patch lies in the hypersurface
$`\det(\rho^\Gamma)=0`$. The determinant on the trace-one Hermitian
space has degree four and is absolutely irreducible, meaning that it
does not factor even after its real coordinates are complexified.
The project's continuation argument turns vanishing on the smooth
real patch into divisibility:

```math
p_E(\rho)-c=\det(\rho^\Gamma)q(\rho),\qquad
\deg q\le k-4.
```

A universal probability is nonconstant, so $`q`$ is nonzero and $`k\ge4`$.
At four copies, $`q`$ is a nonzero constant. This is the source of
four-copy necessity and of uniqueness of the probability polynomial
up to an affine rescaling. The
[rigidity proof](../science/binary_rigidity.md#4-irreducibility-and-continuation-on-the-trace-one-space)
supplies irreducibility and the passage from a real patch to a
polynomial divisor. Constancy at finitely many sampled states would
not establish either conclusion.

The known determinant construction attains four-copy existence.
With the normalization checked in the project, its effect $`E_*`$ has

```math
p_{E_*}(\rho)=\frac12+\det(\rho^\Gamma).
```

For two-qubit states, a negative determinant is equivalent to
entanglement, including the singular-state cases. This determinant
criterion and its collective realization are credited to
[Augusiak, Demianowicz, and Horodecki](../references/RELATED_WORK.md#augusiak2008).

Permutation averaging gives a unique symmetric four-copy effect
for each feasible probability polynomial. An arbitrary effect can
also contain components invisible to all identical tensor inputs.
Consequently, uniqueness of the measured polynomial does not assert
uniqueness of every physical implementation. At higher copy counts,
the determinant factor remains necessary; arbitrary choices of its
polynomial quotient need not give a universal detector.

## From fourth-order sensitivity to the repetition law

For M24–M26, consider the two-qubit family

```math
|\psi_\theta\rangle
=\cos\theta\,|00\rangle+\sin\theta\,|11\rangle,\qquad
\rho_\theta=|\psi_\theta\rangle\langle\psi_\theta|,\qquad
0\le\theta\le\frac\pi4.
```

Writing $`\delta_\theta=\sin\theta\cos\theta`$, the partial-transpose
eigenvalues are
$`\cos^2\theta,\sin^2\theta,\delta_\theta,-\delta_\theta`$. Thus

```math
\det(\rho_\theta^\Gamma)=-\delta_\theta^4.
```

Dephasing the two Schmidt terms gives a separable state at half-trace
distance $`\delta_\theta`$. The witness
$`V=(|\Psi^-\rangle\langle\Psi^-|)^\Gamma`$, where
$`|\Psi^-\rangle=(|01\rangle-|10\rangle)/\sqrt2`$, has
$`\lVert V\rVert_\infty=1/2`$ and expectation $`-\delta_\theta`$ on
$`\rho_\theta`$. Its expectation is nonnegative on separable states.
Norm duality gives the opposite distance inequality, proving
$`\Delta(\rho_\theta)=\delta_\theta`$.

The normalized determinant detector therefore changes its probability
from $`1/2`$ at the product endpoint to $`1/2-\delta_\theta^4`$. For this
effect, the usual $`n^{-1/2}`$ scale of frequency fluctuations suggests
the eighth-power repetition cost. A lower bound over **all** allowed
effects needs more than this example.

The rigidity theorem supplies vanishing through third order along
the same family for every universal effect. The full-rank separable
boundary state

```math
\tau=\frac{I_4}{6}
+\frac{|\Phi^+\rangle\langle\Phi^+|}{3},
\qquad
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},
```

satisfies $`\tau\ge I_4/6`$ and $`\det(\tau^\Gamma)=0`$. Therefore
$`c=\mathrm{Tr}(E\tau^{\otimes k})`$ and positivity give

```math
\lVert E\rVert_\infty\le6^k c,\qquad
\lVert I-E\rVert_\infty\le6^k(1-c).
```

A universal effect is neither zero nor the identity. Full rank of
$`\tau^{\otimes k}`$ consequently implies $`0\lt c\lt1`$.
These two estimates control the scale of the probability even when
$`c`$ is close to zero or one. Combining them with a fourth-derivative
bound along the pure-state family yields, uniformly over all universal
effects at fixed $`k`$,

```math
|p_E(\rho_\theta)-c|
\le B_k\min(c,1-c)\delta_\theta^4,\qquad
B_k=\frac{\pi^4k^4 6^k}{24}.
```

For a prescribed $`0\lt\delta\le1/2`$, choose $`\theta`$ with
$`\delta_\theta=\delta`$ and compare $`\rho_\theta`$ to the separable
state $`\rho_0=|00\rangle\langle00|`$. Rigidity gives
$`p_E(\rho_0)=c`$ because its partial-transpose determinant is zero.
The two output laws therefore represent opposite promised hypotheses.

For Bernoulli probabilities, natural-log relative entropy obeys

```math
D_{\mathrm{KL}}\bigl(\mathrm{Ber}(p)\Vert
\mathrm{Ber}(c)\bigr)
\le\frac{(p-c)^2}{c(1-c)}.
```

The factor $`\min(c,1-c)`$ in the uniform bound controls this
denominator. The relative entropy per block is at most
$`B_k^2\delta_\theta^8`$. It adds over independent repetitions and
cannot increase under a classical decision rule. Requiring both
errors to be at most $`\eta`$ forces the decision distributions to
have relative entropy at least

```math
L_\eta=(1-2\eta)\log\frac{1-\eta}{\eta}.
```

This proves $`n\ge L_\eta/(B_k^2\delta^8)`$.
The complete derivative and information argument is in
[Sampling cost](../science/sampling_cost.md#3-a-probability-bound-uniform-over-all-universal-effects).

For the matching upper bound, the imported determinant–concurrence
inequality and a direct trace-distance comparison give
$`|\det(\rho^\Gamma)|\ge\Delta(\rho)^4`$ on all entangled two-qubit
states. The determinant effect therefore separates the promised
classes by at least $`\delta^4`$ in probability. A threshold halfway
across that gap and Hoeffding's inequality give
$`n\le\lceil2\delta^{-8}\log(1/\eta)\rceil`$.

For fixed $`k\ge4`$, $`0\lt\delta\le1/2`$, and $`0\lt\eta\le1/4`$, the best
repetition count in the globally universal binary class is consequently

```math
n_{\mathrm{univ},k}(\delta,\eta)
=\Theta_k\left(\delta^{-8}\log\frac1\eta\right).
```

The effect may be selected using $`\delta`$ and $`\eta`$, then repeated
unchanged on independent blocks. Its exact probability must still
classify every mixed two-qubit state, including states outside the
finite-data promise.

This is the optimum over the allowed effects. Some higher-copy
universal probabilities can vanish to higher order and perform
worse. The lower-bound constant depends on $`k`$, and the theorem
does not make it uniform when $`k`$ grows with the shrinking gap.
Every run uses $`k`$ copies, so the total input count is $`kn`$.

The [unrestricted comparison](../science/sampling_cost.md#6-comparison-with-unrestricted-measurements)
has total-copy cost $`\Theta(\delta^{-2}\log(1/\eta))`$ in the fixed
two-qubit dimension. Its upper bound retains several tomographic
statistics; its lower bound permits arbitrary joint measurements.
This comparison identifies the cost associated with insisting on a
single exactly universal binary probability.

## A distance promise changes the apparatus class

M27–M28 consider qubit–qutrit states with a different requirement.
A detector chosen for a fixed $`\delta\gt0`$ must distinguish

```math
\rho\in\mathrm{SEP}
\quad\text{from}\quad
\Delta(\rho)\ge\delta,
```

and its behavior on $`0\lt\Delta(\rho)\lt\delta`$ is unrestricted. A
polynomial sign filter can now interpolate across the unconstrained
region. The exact scalar obstruction does not apply to this relaxed
classification task.

The upper construction first turns the physical distance promise
into a negative gap in at least one characteristic coefficient
$`e_3,\ldots,e_6`$ of $`\rho^\Gamma`$. A bounded rational filter combines
the four coefficient signs into one inequality. Its denominators
are strictly positive, so clearing them preserves the signs and
produces a polynomial of degree $`O(\log(1/\delta))`$. The collective
representation then turns this polynomial into a binary effect.

For the lower bound, the physical corner supports a finite grid
encoding the conjunction of two majority functions. A scalar
classifier would produce a polynomial sign representation on that
grid, contradicting a smaller degree than the imported
[threshold-degree theorem](../references/RELATED_WORK.md#sherstov2013)
allows. The quantum reduction and the explicit upper construction
are supplied in [Promise-gap block size](../science/promise_gap.md).
This research dependency is not a second educational anchor.

The resulting law is

```math
k_{\mathrm{gap}}(\delta)=\Theta\left(\log\frac1\delta\right)
\qquad(\delta\downarrow0)
```

in fixed dimensions $`2\times3`$, with the binary probability known
to arbitrary precision. It bounds the copies **inside one block**.
Normalization of the constructed polynomial can leave a very small
probability margin, so the law gives no logarithmic bound on total
samples.

| Statement | Requirement on the apparatus | Resource controlled |
|---|---|---|
| R1 | Exact classification of every state in its stated domain | Minimum retained outcomes, allowing any finite block size |
| R3 | Exact universality on all mixed two-qubit states, even while testing a nonzero distance promise | Best independent repetitions at fixed block size |
| S1 | Correct classification only of the two promised qubit–qutrit classes | Minimum block size with arbitrarily precise probabilities |

The distinction between R3 and S1 is in the apparatus requirement.
Both introduce a distance promise, but only R3 requires the apparatus
to classify the intermediate states from its exact probability.

## Connecting the bridge to the complete record

The milestone map uses these connections in order: M01–M12 assemble
the operational framework; M13–M20 establish and attain the outcome
hierarchy; M21–M23 establish binary rigidity; M24–M26 derive the
statistical law; M27–M28 analyze the changed promise; and M29–M30
integrate attribution, evidence, and the scientific story.

The [scientific reading route](../science/model.md#reading-and-verification)
connects the topic-based accounts and their complete proofs. The
[resource interpretation](../science/interpretation.md) joins the conclusions
and their physical meaning. [Related work](../references/RELATED_WORK.md)
identifies the imported theorem ingredients and the scope of the
contributions. The [exact verification guide](../verification/README.md)
specifies which finite constructions and identities the scripts check.
Those checks complement the analytical proofs; they do not replace
universal arguments or the cited threshold-degree theorem.
