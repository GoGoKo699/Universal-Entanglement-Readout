# Exact outcome minima

The number of outcomes of a fixed collective detector has a sharp minimum in
the smallest bipartite dimensions. The minimum concerns exact classification
from the detector's probability vector. It does not assert error-free
classification from finitely many observed outcomes.

The operational assumptions and the distinction between block size, outcome
count, and statistical repetitions are specified in [the model](model.md).
The imported separability and polynomial-measurement results are identified in
[related work](../references/RELATED_WORK.md).

## R1: outcome hierarchy

Let a detector consume a fixed finite number $`k`$ of independent copies of an
unknown mixed state on each run. Its fixed POVM has $`m`$ outcomes. An arbitrary
classical decision function may use the exact probability vector. The minimum
outcome counts are:

| State domain | Minimum $`m`$ | Retained coordinates $`m-1`$ | Attained block size |
|---|---:|---:|---:|
| All states on $`\mathbb C^2\otimes\mathbb C^2`$ | $`2`$ | $`1`$ | $`4`$ |
| States on $`\mathbb C^2\otimes\mathbb C^3`$ with invertible qutrit marginal | $`3`$ | $`2`$ | $`6`$ |
| All states on $`\mathbb C^2\otimes\mathbb C^3`$ | $`4`$ | $`3`$ | $`6`$ |

The middle minimum also holds under the stronger promise that the global state
is positive definite. The two-qubit construction is the established determinant
test of Augusiak, Demianowicz, and Horodecki. The six-copy values are upper bounds
on block size; no minimal-six-copy assertion enters R1.

The lower bounds permit every finite $`k`$. They do not assume that the decision
function is continuous, semialgebraic, or a conjunction of polynomial sign tests.
The phrase “retained coordinates” does not assert that those coordinate
functions are algebraically independent.

### Polynomial form of a fixed detector

For an effect $`E_i`$ on $`k`$ copies,

```math
p_i(\rho)=\mathrm{Tr}[E_i\rho^{\otimes k}]
```

is a real polynomial of degree at most $`k`$ on the affine space of trace-one
Hermitian matrices. Since $`\sum_i p_i=1`$, the first $`m-1`$ coordinates determine
the full vector. Correct classification therefore requires the two image sets

```math
(p_1,\ldots,p_{m-1})(\mathrm{SEP})
\quad\text{and}\quad
(p_1,\ldots,p_{m-1})(\mathrm{ENT})
```

to be disjoint. This necessary condition is the only property of the classical
decision function used below.

## Analytic obstruction at a separable corner

### Lemma 1: no analytic scalar classifies a quadrant

Let $`r>0`$. There is no real-analytic scalar $`p`$ on a neighborhood of
$`[-r,r]^2`$ whose value determines, throughout that square, whether
$`s\ge0`$ and $`t\ge0`$.

**Proof.** The image of the compact connected quadrant $`[0,r]^2`$ is a compact
interval $`[a,b]`$. Correct classification would require every point in the square
outside that quadrant to have its $`p`$ value outside $`[a,b]`$.

For $`0<t<r`$, the point $`(0,t)`$ belongs to the quadrant and is approached by
points $`(s,t)`$ with $`s<0`$. If $`p(0,t)`$ were in the interior of $`[a,b]`$,
continuity would put some of these exterior points in the same interval.
Consequently $`p(0,t)\in\{a,b\}`$. A continuous map from the connected interval
$`0<t<r`$ to this at-most-two-point set is constant. The one-variable analytic
identity theorem extends that constancy across $`t=0`$ to negative $`t`$. An
exterior point $`(0,t)`$ with $`t<0`$ then has the same value as a quadrant point,
which contradicts classification. The argument includes $`a=b`$. $`\square`$

### A full-rank physical seed

Use the basis $`(00,01,02,10,11,12)`$ and the six complex numbers

```math
Z=\{0,1,-1,i,-i,2\}.
```

For $`z\in Z`$, define the product vectors

```math
v(z)=(1,z)\otimes(1,z,z^2),\qquad
w(z)=(1,\bar z)\otimes(1,z,z^2),
```

and put

```math
X=\sum_{z\in Z}v(z)v(z)^\dagger,\qquad
R=\sum_{z\in Z}w(z)w(z)^\dagger.
```

Partial transpose on the qubit gives $`R^\Gamma=X`$. Explicitly,

```math
R=\begin{pmatrix}
6&2&4&2&8&8\\
2&8&8&4&8&20\\
4&8&20&8&16&32\\
2&4&8&8&8&16\\
8&8&16&8&20&32\\
8&20&32&16&32&68
\end{pmatrix}.
```

Its trace is $`130`$. Its leading principal minors are
$`6,44,496,2304,5120,9216`$, so $`R>0`$ by Sylvester's criterion. The vectors
$`v(z)=(1,z,z^2,z,z^2,z^3)`$ span a four-dimensional space: the upper bound follows
from their polynomial form, and four distinct choices of $`z`$ give a Vandermonde
matrix of rank four. Thus $`X`$ has rank four. An orthonormal basis of its kernel
is

```math
u_1=\frac{|01\rangle-|10\rangle}{\sqrt2},\qquad
u_2=\frac{|02\rangle-|11\rangle}{\sqrt2}.
```

The separable state $`\rho_*=R/130`$ is therefore positive definite and has a
positive partial transpose of rank four.

### A physical quadrant

Let $`P_j=(u_ju_j^\dagger)^\Gamma`$ and define

```math
\rho(s,t)=(1-s-t)\rho_*+sP_1+tP_2.
```

This Hermitian matrix has trace one. Since $`\rho_*>0`$, it remains a density
matrix on a sufficiently small square about $`(0,0)`$. Its partial transpose is

```math
\rho(s,t)^\Gamma=(1-s-t)X/130+s u_1u_1^\dagger+t u_2u_2^\dagger.
```

Its eigenvalues are $`s,t`$ and four positive eigenvalues multiplied by
$`1-s-t`$. Hence, on that square,

```math
\rho(s,t)\in\mathrm{SEP}
\quad\Longleftrightarrow\quad
\rho(s,t)^\Gamma\ge0
\quad\Longleftrightarrow\quad s,t\ge0.
```

The first equivalence uses the Horodecki PPT theorem in dimension $`2\times3`$.
The exact rational check in [verify_corner.py](../verification/verify_corner.py)
also certifies the concrete square $`|s|,|t|\le10^{-4}`$ by positive-definite
corner matrices and convexity. The existence argument needs only a sufficiently
small square.

Lemma 1 excludes a single polynomial statistic even on positive-definite global
states. Their marginals are also positive definite. Thus a binary detector is
impossible on both rank-promised domains in R1.

## Two polynomial coordinates are insufficient on all states

### Lemma 2: constancy on the physical rank-four stratum

Suppose a pair of real polynomials $`F=(f_1,f_2)`$ classifies all qubit–qutrit
states. Consider the real-analytic manifold

```math
M=\{\Lambda:\mathrm{Tr}\Lambda=1,\ \Lambda\ge0,
\ \mathrm{rank}\Lambda=4,\ \Lambda^\Gamma>0\}.
```

The seed shows that $`M`$ is nonempty. Positivity of the four nonzero eigenvalues
and strict positivity of $`\Lambda^\Gamma`$ are open conditions on the trace-one
rank-four Hermitian manifold. Both components of
$`G(\Lambda)=F(\Lambda^\Gamma)`$ have zero derivative in every tangent direction
of $`M`$.

**Proof.** Suppose a tangent derivative is nonzero at $`\Lambda_0\in M`$.
After an invertible linear change of the two output coordinates, there is an
analytic curve $`\Lambda(v)`$ in $`M`$ through $`\Lambda_0`$ with
$`\partial_v f_1(\Lambda(v)^\Gamma)|_{v=0}\ne0`$.

Split the Hilbert space into the range and kernel of $`\Lambda_0`$, of dimensions
four and two. In this fixed basis, a nearby rank-four curve has the block form

```math
L(v,0,0)=
\begin{pmatrix}
A(v)&C(v)\\
C(v)^\dagger&C(v)^\dagger A(v)^{-1}C(v)
\end{pmatrix},\qquad A(v)>0.
```

Choose this representative with trace one at $`s=t=0`$, and extend it by

```math
L(v,s,t)=
\begin{pmatrix}
A(v)&C(v)\\
C(v)^\dagger&C(v)^\dagger A(v)^{-1}C(v)+\mathrm{diag}(s,t)
\end{pmatrix},
```

```math
\widetilde\Lambda(v,s,t)=\frac{L(v,s,t)}{\mathrm{Tr}L(v,s,t)},
\qquad
\widetilde\rho(v,s,t)=\widetilde\Lambda(v,s,t)^\Gamma.
```

The denominator remains positive. Strict positivity at the origin implies
$`\widetilde\rho(v,s,t)>0`$ throughout a small real neighborhood. By the Schur
complement,

```math
\widetilde\rho(v,s,t)\in\mathrm{SEP}
\quad\Longleftrightarrow\quad s,t\ge0.
```

The analytic implicit function theorem supplies $`v=v(s,t)`$ on a neighborhood
of the origin such that
$`f_1(\widetilde\rho(v(s,t),s,t))`$ is constant. The analytic scalar

```math
p(s,t)=f_2(\widetilde\rho(v(s,t),s,t))
```

would then classify the quadrant, contrary to Lemma 1. Thus no nonzero tangent
derivative exists. $`\square`$

On a connected coordinate patch of $`M`$, both components of $`G`$ are consequently
constant. Denote this pair by $`(c_1,c_2)`$.

### Lemma 3: polynomial continuation to all matrices of rank at most four

Let $`q(\Lambda)`$ be either component of $`G`$, and let $`c`$ be its constant value
on the patch. Choose a polynomial representative of degree at most $`d`$ in the
real coordinates of Hermitian matrices. Its trace homogenization is

```math
P(X)=(\mathrm{Tr}X)^d
\left[q\left(\frac{X}{\mathrm{Tr}X}\right)-c\right].
```

Expanding the expression gives a homogeneous polynomial. Positive rescaling of
the trace-one patch shows that $`P`$ vanishes on an open patch of the cone of
positive-semidefinite rank-four matrices.

Write $`X=YY^\dagger`$ with $`Y\in\mathbb C^{6\times4}`$. The preimage of that
patch contains a nonempty open set of full-column-rank $`Y`$ in its $`48`$ real
coordinates. Thus the real polynomial $`P(YY^\dagger)`$ vanishes identically.
Write $`Y=U+iV`$. After complexifying the real variables, the change
$`(U,V)\mapsto(U+iV,U-iV)`$ is invertible. The two factors become independent,
and the identity becomes

```math
P(YZ^T)=0\qquad
\text{for all }Y,Z\in\mathbb C^{6\times4}.
```

Here the complexification of the real vector space of Hermitian matrices is
the full complex matrix space. Every complex matrix of rank at most four admits
the factorization $`YZ^T`$. Therefore $`P`$ vanishes on every such matrix. In
particular, $`q=c`$ on every trace-one Hermitian matrix of rank at most four.
This argument applies separately to both components.

### Completion of the lower bound

The embedded Bell state

```math
|\Phi\rangle=(|00\rangle+|11\rangle)/\sqrt2
```

is entangled, while its partial transpose has eigenvalues
$`-1/2,1/2,1/2,1/2,0,0`$ and hence rank four. Lemma 3 forces
$`F(|\Phi\rangle\langle\Phi|)=(c_1,c_2)`$, the same value as the separable
patch. This contradicts classification. Thus two polynomial coordinates cannot
classify all qubit–qutrit states. Fewer coordinates are excluded by appending
constant components. Every fixed finite-copy POVM with at most three outcomes
is therefore insufficient.

## Three explicit statistics give a complete criterion

For a qubit–qutrit state define

```math
B=\mathrm{Tr}_A\rho,\qquad D=I_2\otimes B,\qquad H=D-\rho,
```

```math
f=\det H,\qquad
g=\mathrm{Tr}[D\mathrm{adj}(H)],\qquad
h=e_4(H).
```

The degrees in $`\rho`$ are $`6,6,4`$. The fourth elementary symmetric coefficient
$`e_4(H)`$ is the sum of the principal $`4\times4`$ minors. The qubit reduction
identity is

```math
H=(\sigma_y\otimes I_3)\rho^\Gamma(\sigma_y\otimes I_3).
```

Consequently $`H`$ and $`\rho^\Gamma`$ have the same spectrum. The complete rule is

```math
\boxed{
\rho\in\mathrm{SEP}
\ \Longleftrightarrow\,
(f>0\ \text{and}\ g>0)
\ \text{or}\,
\bigl(f=0\ \text{and}\ [g>0\ \text{or}\ (g=0\ \text{and}\ h\ge0)]\bigr).
}
```

### Invertible qutrit marginal

Assume $`B>0`$, and introduce the congruent matrix

```math
K=D^{-1/2}HD^{-1/2}=I_6-R_0,\qquad
R_0=D^{-1/2}\rho D^{-1/2}.
```

Since $`R_0\ge0`$ and $`\mathrm{Tr}_A R_0=I_3`$,

```math
K\le I_6,\qquad\mathrm{Tr}K=3.
```

Congruence preserves inertia. If $`K`$ has a negative eigenvalue, it has at least
four positive eigenvalues: at most three positive eigenvalues, each at most one,
would force its trace below three. Its possible NPT inertias are consequently
$`(1,0,5)`$, $`(1,1,4)`$, and $`(2,0,4)`$, where the entries count negative, zero,
and positive eigenvalues.

The determinant identity

```math
\det(H+tD)=(\det B)^2\det(K+tI_6)
```

gives, by differentiating at zero,

```math
g=(\det B)^2 e_5(K).
```

The adjugate derivative identity is polynomial, so this step also holds when
$`H`$ is singular.

For two negative eigenvalues, write the spectrum of $`K`$ as
$`-a,-b,c_1,c_2,c_3,c_4`$, with $`a,b,c_i>0`$. The trace condition and $`c_i\le1`$
imply $`\sum_i c_i=3+a+b`$ and hence $`c_i\ge a+b`$ for each $`i`$. Therefore

```math
\begin{aligned}
e_5(K)
&=\left(\prod_i c_i\right)
\left[ab\sum_i\frac1{c_i}-(a+b)\right]\\
&\le\left(\prod_i c_i\right)
\left[\frac{4ab}{a+b}-(a+b)\right]\\
&=-\left(\prod_i c_i\right)\frac{(a-b)^2}{a+b}\le0.
\end{aligned}
```

The complete full-marginal-rank classification follows:

| Inertia or positivity of $`H`$ | $`f`$ | $`g`$ | Decision |
|---|---:|---:|---|
| Positive definite | $`>0`$ | $`>0`$ | Separable |
| PPT, rank five | $`0`$ | $`>0`$ | Separable |
| PPT, rank at most four | $`0`$ | $`0`$ | Separable |
| One negative, rank six | $`<0`$ | Unrestricted | Entangled |
| One negative, rank five | $`0`$ | $`<0`$ | Entangled |
| Two negatives, rank six | $`>0`$ | $`\le0`$ | Entangled |

For rank five, $`e_5(K)`$ is the product of the five nonzero eigenvalues. For rank
at most four it vanishes, and the trace argument excludes NPT when $`B>0`$.
Thus $`f,g`$ alone suffice on this promise:

```math
\rho\in\mathrm{SEP}
\quad\Longleftrightarrow\quad
(f>0\text{ and }g>0)\text{ or }(f=0\text{ and }g\ge0).
```

### Singular qutrit marginal

Positivity implies
$`\mathrm{supp}\rho\subseteq\mathbb C^2\otimes\mathrm{supp}B`$.
To see this, a vector in $`\ker B`$ has zero total expectation against the two
qubit basis vectors. Each expectation is nonnegative, so both vanish; a vector
of zero quadratic form belongs to the kernel of a positive matrix.

If $`\mathrm{rank}B=2`$, local restriction gives a two-qubit state.
$`H`$ has a $`4\times4`$ block and two additional zero rows and columns in a
suitable local basis. Consequently $`f=g=0`$ and $`h`$ is the determinant of that
block. It is nonnegative exactly for separable two-qubit states. This follows
also by whitening on the two-dimensional marginal support: an NPT matrix with
trace two and eigenvalues at most one must have one negative and three positive
eigenvalues. PPT sufficiency then supplies the separability statement.

If $`\mathrm{rank}B=1`$, the state is a product of a qubit state and the
fixed marginal pure state. It is separable and $`f=g=h=0`$. These cases complete
the displayed criterion for every qubit–qutrit state.

### Equality cases and verification

The strict condition $`g>0`$ when $`f>0`$ is necessary. Define

```math
\rho=\frac14\left[
(|00\rangle+|11\rangle)(\langle00|+\langle11|)
+(|01\rangle+|12\rangle)(\langle01|+\langle12|)
\right].
```

This NPT state has

```math
(f,g,h)=(1/4096,0,-1/64).
```

The rank-four PPT seed has $`(f,g,h)=(0,0,1776/17850625)`$, whereas the embedded
Bell state has $`(0,0,-1/16)`$. These values show the role of $`h`$ on the singular
marginal boundary. The exact rational checks in
[verify_outcome_criterion.py](../verification/verify_outcome_criterion.py)
cover the rank and sign branches. The universal result rests on the proof above.

## Attainment and dimensional consequences

[Collective measurements](collective_measurements.md) gives explicit
state-independent six-copy observables with expectations $`f,g,h`$, certified
operator-norm bounds, and concrete positive POVM effects. They yield four outcomes
on all states, and three outcomes when only $`f,g`$ are required. Together with
the two lower bounds, this proves the qubit–qutrit rows of R1.

Any bipartite system with both local dimensions at least two, other than
$`2\times2`$, contains a local $`2\times3`$ or $`3\times2`$ subspace. Restricting a
fixed finite-copy POVM to that subspace preserves its number of outcomes and
preserves separability classification. Therefore **at least four outcomes are
necessary in all these dimensions**. Sufficiency of four outcomes is established
here only for $`2\times3`$ and its exchanged version.

The full-rank promise changes the attained minimum because polynomial
continuation in the stronger lower bound reaches singular-marginal states.
Whitening in the upper proof is an algebraic argument. The physical detector
uses fixed polynomial observables and does not estimate or apply a
state-dependent inverse marginal.
