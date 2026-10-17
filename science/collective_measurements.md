# Fixed collective measurements

This construction realizes the three qubit–qutrit statistics in
[the outcome theorem](outcome_minima.md) by one fixed six-copy POVM. It specifies
the observables, their coefficients, and a certified scale making every effect
positive. The operational interpretation follows [the model](model.md).

The polynomial-to-collective-observable principle is established by Brun and by
earlier direct-measurement constructions. The antisymmetric determinant
observable is also established. See
[related work](../references/RELATED_WORK.md) for those dependencies.

## General polynomial-to-observable lemma

Let $`\mathcal H`$ be any finite-dimensional Hilbert space. Choose a real basis
$`G_\alpha`$ of its Hermitian operators and its trace-dual Hermitian basis
$`F_\alpha`$, so $`\mathrm{Tr}(F_\alpha G_\beta)=\delta_{\alpha\beta}`$.
The real coordinates of a density operator are

```math
x_\alpha(\rho)=\mathrm{Tr}(F_\alpha\rho),\qquad
\rho=\sum_\alpha x_\alpha(\rho)G_\alpha.
```

Let $`q`$ be a real polynomial of degree at most $`k`$, where $`k\ge1`$, in these
coordinates. Index its monomials by finite lists $`\mu=(\alpha_1,\ldots,\alpha_r)`$
with $`0\le r\le k`$, allowing repeated indices:

```math
q(\rho)=\sum_\mu c_\mu\prod_{j=1}^{|\mu|}x_{\alpha_j}(\rho),
\qquad c_\mu\in\mathbb R.
```

The empty list is the constant term. Define

```math
W_q=\sum_\mu c_\mu
\left(F_{\alpha_1}\otimes\cdots\otimes F_{\alpha_{|\mu|}}
\otimes I^{\otimes(k-|\mu|)}\right).
```

Each summand is Hermitian. Tensor factorization of the trace and
$`\mathrm{Tr}\rho=1`$ give

```math
\mathrm{Tr}(W_q\rho^{\otimes k})=q(\rho).
```

This also handles a polynomial originally specified only on the trace-one
affine space: choose a polynomial extension to the Hermitian coordinates and
pad its lower-degree monomials as above. Averaging $`W_q`$ over the $`k!`$ whole-copy
permutations preserves this expectation and Hermiticity.

An explicit coefficient bound is

```math
\Vert W_q\Vert_\infty\le C_q,
\qquad
C_q=\sum_\mu |c_\mu|
\prod_{j=1}^{|\mu|}\Vert F_{\alpha_j}\Vert_\infty.
```

The empty product equals one. The same bound holds after permutation averaging.
For example, the coordinate functionals
$`F_{ii}=|i\rangle\langle i|`$,
$`F^{\mathrm R}_{ij}=(|i\rangle\langle j|+|j\rangle\langle i|)/2`$, and
$`F^{\mathrm I}_{ij}=i(|i\rangle\langle j|-|j\rangle\langle i|)/2`$ for $`i<j`$
extract the diagonal entries, real parts, and imaginary parts of $`\rho`$.
Their norms are at most one, so the simpler bound
$`C_q\le\sum_\mu|c_\mu|`$ is available in those coordinates.

This is the standard collective representation principle of Brun. The direct
construction here records its normalization. With $`M=\max\{1,C_q\}`$,

```math
E_q=\frac I2+\frac{W_q}{2M}
```

is a valid binary effect, and its probability is
$`1/2+q(\rho)/(2M)`$. This is the representation used when a polynomial scalar
is constructed in [the promise-gap theorem](promise_gap.md). The coefficient
bound certifies a valid effect; it need not give a useful statistical margin.

More generally, let $`q_1,\ldots,q_s`$ be any finite family of real polynomials
with degrees at most the common block size $`k`$. Construct $`W_j`$ and bounds
$`C_j`$ as above. Set

```math
L=\max\left\{1,\sum_{j=1}^s C_j\right\},\qquad
\epsilon=\frac1{2(s+1)L},
```

```math
E_j=\frac I{s+1}+\epsilon W_j\quad(1\le j\le s),\qquad
E_{s+1}=\frac I{s+1}-\epsilon\sum_{j=1}^sW_j.
```

Every effect is at least $`I/[2(s+1)]`$, and the effects sum to $`I`$. Their first
$`s`$ probabilities recover the prescribed polynomials by an affine map. This
proves finite-family realization by one fixed POVM without asserting a short
circuit or a small coefficient norm.

## Tensor factors and fixed linear maps

One input copy has Hilbert space $`\mathcal H=A\otimes B`$, where
$`A=\mathbb C^2`$ and $`B=\mathbb C^3`$. A six-copy block has ordered factors
$`(A_1B_1)\cdots(A_6B_6)`$. Partial traces below are unnormalized.

On one copy, define the linear maps

```math
\mathcal T(X)=I_2\otimes\mathrm{Tr}_A X,\qquad
\mathcal R(X)=\mathcal T(X)-X.
```

Then $`D=\mathcal T(\rho)`$ and $`H=\mathcal R(\rho)`$ are exactly the matrices
used in the outcome criterion. In particular, $`\mathcal T`$ contains no factor
of $`1/2`$. On the six-copy operator space, $`\mathcal T_j`$ and $`\mathcal R_j`$
act on $`A_j`$ and leave every other tensor factor intact.

Both maps preserve Hermiticity and are self-adjoint for the Hilbert–Schmidt
pairing. For example,

```math
\mathrm{Tr}[X\mathcal T(Y)]
=\mathrm{Tr}[(\mathrm{Tr}_A X)(\mathrm{Tr}_A Y)]
=\mathrm{Tr}[\mathcal T(X)Y].
```

Maps on different copies commute. The qubit identity

```math
\mathcal R(X)=(\sigma_y\otimes I)X^{T_A}(\sigma_y\otimes I)
```

holds with arbitrary spectator factors. Thus a product of the $`\mathcal R_j`$
is a partial transpose on the indicated qubit factors followed by a fixed
unitary conjugation.

These maps define fixed observables. The construction does not physically apply
partial transpose or reduction to an unknown input state.

## Antisymmetric projectors and normalization

For $`r`$ whole copies, let $`V_\pi`$ be the permutation unitary

```math
V_\pi|x_1,\ldots,x_r\rangle
=|x_{\pi^{-1}(1)},\ldots,x_{\pi^{-1}(r)}\rangle,
\qquad \pi\in S_r.
```

The normalized antisymmetric projector is

```math
A_r=\frac1{r!}\sum_{\pi\in S_r}\mathrm{sgn}(\pi)V_\pi.
```

It satisfies $`A_r^\dagger=A_r`$, $`A_r^2=A_r`$, and
$`\mathrm{rank}A_r=\binom6r`$. In particular, $`A_6`$ is a rank-one projector
and $`A_4`$ has rank $`15`$. For every Hermitian $`6\times6`$ matrix $`X`$,

```math
\mathrm{Tr}[A_rX^{\otimes r}]=e_r(X).
```

One proof diagonalizes $`X`$: each normalized wedge basis vector contributes the
product of $`r`$ distinct eigenvalues. No positivity assumption on $`X`$ is needed.
At $`r=6`$ the expression is $`\det X`$.

The associated symmetric multilinear form is

```math
\mathcal A_r(X_1,\ldots,X_r)
=\mathrm{Tr}[A_r(X_1\otimes\cdots\otimes X_r)].
```

Simultaneous permutation of its arguments leaves it unchanged. Hence

```math
\left.\frac{d}{dt}\det(H+tD)\right|_{t=0}
=6\mathcal A_6(D,H,H,H,H,H).
```

This identity remains valid when $`H`$ is singular. The factor is $`6`$, not $`1`$,
because the derivative has one contribution from each tensor factor.

## Explicit six-copy observables

### Determinant

Define

```math
W_f=\left(\prod_{j=1}^6\mathcal R_j\right)(A_6).
```

Self-adjointness of the maps gives

```math
\mathrm{Tr}[W_f\rho^{\otimes6}]
=\mathrm{Tr}[A_6H^{\otimes6}]=\det H=f.
```

### Weighted adjugate derivative

Define the fully symmetric observable

```math
W_g=\sum_{j=1}^6
\left(\mathcal T_j\prod_{\ell\ne j}\mathcal R_\ell\right)(A_6).
```

The six summands have equal expectation on $`\rho^{\otimes6}`$. Therefore

```math
\begin{aligned}
\mathrm{Tr}[W_g\rho^{\otimes6}]
&=6\mathcal A_6(D,H,H,H,H,H)\\
&=\left.\frac{d}{dt}\det(H+tD)\right|_{t=0}\\
&=\mathrm{Tr}[D\mathrm{adj}(H)]=g.
\end{aligned}
```

The sum is not divided by six. It is the fixed operator for $`g`$ itself.

### Fourth coefficient on a common six-copy block

For each four-element subset $`S\subset\{1,\ldots,6\}`$, let $`A_{4,S}`$ be
$`A_4`$ on the whole copies in $`S`$ and the identity on the two remaining copies.
Set

```math
W_h=\frac1{15}\sum_{|S|=4}
\left(\prod_{j\in S}\mathcal R_j\right)(A_{4,S}).
```

Every summand has expectation
$`e_4(H)(\mathrm{Tr}\rho)^2=h`$. Thus

```math
\mathrm{Tr}[W_h\rho^{\otimes6}]=h.
```

The average over all $`15`$ subsets makes the observable symmetric under all six
copy permutations. A single chosen subset would give the same expectation on
identical inputs, but the displayed average fixes a symmetric convention.

### Coefficients and matrix entries

The formulas above specify finite operators without choosing a measurement
circuit. The permutation coefficients are $`1/720`$ for $`A_6`$ and $`1/24`$ for
$`A_4`$. The subset average for $`W_h`$ adds the factor $`1/15`$, giving $`1/360`$
before application of its reduction maps. All matrix entries are rational in
the computational basis.

For completeness, if the other tensor indices are suppressed,

```math
[\mathcal T_j(X)]_{a_jb_j,\,a'_jb'_j}
=\delta_{a_j,a'_j}\sum_{c=0}^1 X_{cb_j,\,cb'_j},
```

with all other row and column indices held fixed. Subtracting $`X`$ gives
$`\mathcal R_j(X)`$. Together with the permutation rule, this is an entrywise
construction of each observable.

## Certified operator-norm bounds

The following bounds concern the fixed operators on the complete six-copy
Hilbert space, not only their expectations on identical product inputs:

```math
\boxed{\Vert W_f\Vert_\infty\le1,\qquad
\Vert W_g\Vert_\infty\le12,\qquad
\Vert W_h\Vert_\infty\le\sqrt{15}<4.}
```

### Partial transpose of a pure projector

Let $`P=|\psi\rangle\langle\psi|`$ be a normalized pure projector and let
$`\lambda_i`$ be the squared Schmidt coefficients across any bipartition.
The nonzero eigenvalues of the partial transpose are $`\lambda_i`$ and
$`\pm\sqrt{\lambda_i\lambda_j}`$ for $`i<j`$. Its operator norm is
$`\max_i\lambda_i\le1`$. Fixed unitary conjugation does not change this norm.

Since $`A_6`$ is a normalized pure projector, applying any subset of the six
qubit reduction maps to it has operator norm at most one. This proves the
bound for $`W_f`$.

Using $`\mathcal T_j=\mathcal R_j+\mathrm{id}`$ gives the exact identity

```math
W_g=6W_f+\sum_{j=1}^6
\left(\prod_{\ell\ne j}\mathcal R_\ell\right)(A_6).
```

Each of the six additional operators has norm at most one by the same pure
projector argument. The triangle inequality gives $`\Vert W_g\Vert_\infty\le12`$.

### Fourth-coefficient bound

On four copies, reduction is a unitary-conjugated partial transpose and
preserves the Hilbert–Schmidt norm. Consequently

```math
\left\Vert\mathcal R^{\otimes4}(A_4)\right\Vert_\infty
\le\left\Vert\mathcal R^{\otimes4}(A_4)\right\Vert_2
=\Vert A_4\Vert_2
=\sqrt{\mathrm{Tr}A_4}=\sqrt{15}.
```

Appending identity factors does not change the operator norm. Averaging the
$`15`$ placements preserves this upper bound by convexity of the norm.

These analytic certificates suffice for positivity below. No enumeration of
test states is used to infer positivity of the POVM.

## A concrete four-outcome POVM

Let $`I`$ denote the identity on the six-copy space, and define

```math
E_1=\frac I4+\frac{W_f}{80},\qquad
E_2=\frac I4+\frac{W_g}{80},\qquad
E_3=\frac I4+\frac{W_h}{80},
```

```math
E_4=\frac I4-\frac{W_f+W_g+W_h}{80}.
```

Their sum is $`I`$. The norm bounds imply

```math
E_1\ge\frac{19}{80}I,\qquad
E_2\ge\frac1{10}I,\qquad
E_3\ge\frac15I,\qquad
E_4\ge\frac3{80}I.
```

Thus all effects are positive definite. Their exact probabilities satisfy

```math
p_1=\frac14+\frac f{80},\qquad
p_2=\frac14+\frac g{80},\qquad
p_3=\frac14+\frac h{80},\qquad
p_4=1-p_1-p_2-p_3.
```

Recovering $`f,g,h`$ by these affine formulas and applying the outcome criterion
gives the claimed fixed four-outcome detector.

For the invertible-qutrit-marginal promise, use instead

```math
F_1=\frac I3+\frac{W_f}{48},\qquad
F_2=\frac I3+\frac{W_g}{48},\qquad
F_3=\frac I3-\frac{W_f+W_g}{48}.
```

Their respective lower bounds are
$`5I/16`$, $`I/12`$, and $`I/16`$. They therefore form a fixed three-outcome
POVM with recoverable statistics $`f,g`$.

## Verification and scope

[verify_collective_measurements.py](../verification/verify_collective_measurements.py)
checks the antisymmetric permutation coefficients by exact cycle contractions,
the determinant polarization factor, and the fourth coefficient against
independent rational minor calculations. It includes a state for which $`D`$ and
$`H`$ do not commute, as well as the singular and equality cases in the outcome
criterion. The script also checks the rational lower bounds used in the
normalization. The operator-norm proofs above remain the universal certificates.

The construction uses six identical input copies and one fixed finite-outcome
POVM. It establishes existence with explicit effects. It does not claim a
short gate decomposition, locality of the collective measurement, an optimal
six-copy block size, or an optimal normalization. Those resources are separate
from the exact outcome minimum.
