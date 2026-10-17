# Binary rigidity for two-qubit entanglement

A fixed binary collective measurement can classify every mixed two-qubit state from its exact outcome probability only if that probability contains the partial-transpose determinant as a polynomial factor. Four copies are necessary and sufficient. At four copies, every universal probability is an affine rescaling of that determinant.

This document proves result **R2**, including the normalization of an explicit four-copy effect. The resulting finite-statistics theorem is proved in [sampling_cost.md](sampling_cost.md). The general measurement conventions and the higher-dimensional outcome minima are given in [model.md](model.md) and [outcome_minima.md](outcome_minima.md).

## 1. Definitions and statement

Let

```math
\mathcal H=\mathbb C^2\otimes\mathbb C^2,
\qquad
\mathcal A=\{X=X^\dagger:\mathrm{Tr}X=1\}.
```

The real affine space $`\mathcal A`$ has dimension fifteen. Let $`\mathcal D`$ be its density operators and $`\mathrm{SEP}\subset\mathcal D`$ its separable states. The operation $`\Gamma`$ is partial transpose on the qubit $`A`$, in a fixed product basis. Define

```math
f(\rho)=\det(\rho^\Gamma).
```

A fixed measurement on $`k`$ independent copies has a binary effect $`0\le E\le I`$ and probability

```math
p_E(\rho)=\mathrm{Tr}(E\rho^{\otimes k}).
```

Its restriction to $`\mathcal A`$ is a real polynomial of total degree at most $`k`$. State-independent ancillas and fixed internal processing are included in $`E`$.

The effect is **exactly universal** if some function of the exactly known number $`p_E(\rho)`$ labels every $`\rho\in\mathrm{SEP}`$ as separable and every $`\rho\in\mathcal D\setminus\mathrm{SEP}`$ as entangled. The function can be arbitrary. Continuity, monotonicity, and a threshold form are not assumptions.

### R2. Rigidity and minimum block size

If $`E`$ is exactly universal, there are a constant $`c\in(0,1)`$ and a nonzero real polynomial $`q`$ on $`\mathcal A`$ such that

```math
p_E(\rho)=c+f(\rho)q(\rho),
\qquad
\deg q\le k-4.
\qquad\text{(1)}
```

Consequently, $`k\ge4`$. When $`k=4`$,

```math
p_E(\rho)=c+\alpha f(\rho),
\qquad \alpha\in\mathbb R\setminus\{0\}.
\qquad\text{(2)}
```

Four copies suffice. The feasible pairs in (2) are exactly

```math
|\alpha|\le2\min(c,1-c),
\qquad \alpha\ne0.
\qquad\text{(3)}
```

In particular, $`c=1/2`$ and $`\alpha=1`$ are attained by the effect constructed below.

Equation (2) is uniqueness of the probability polynomial. An arbitrary physical implementation of that probability need not be unique. Averaging over permutations of the copies does give a unique effect, as proved in Section 7.

## 2. The two-qubit determinant criterion

We use the established fact that positive partial transpose is equivalent to separability in $`2\times2`$, due to [Horodecki, Horodecki, and Horodecki (1996)](https://arxiv.org/abs/quant-ph/9605038). The determinant form of this criterion and its collective measurement were developed by [Augusiak, Demianowicz, and Horodecki (2008)](https://arxiv.org/abs/quant-ph/0604109).

For completeness, the determinant sign reduction follows from a short inertia argument. Write

```math
B=\mathrm{Tr}_A\rho,\qquad
D=I_2\otimes B,\qquad
H=D-\rho.
```

The qubit reduction identity is

```math
H=(\sigma_y\otimes I_2)\rho^\Gamma(\sigma_y\otimes I_2).
\qquad\text{(4)}
```

If $`B`$ has rank one, positivity confines $`\rho`$ to $`\mathbb C^2\otimes\mathrm{supp}B`$, so $`\rho`$ is a product state. Otherwise $`B>0`$, and

```math
K=D^{-1/2}HD^{-1/2}=I_4-R,
\qquad
R=D^{-1/2}\rho D^{-1/2}\ge0.
```

Since $`\mathrm{Tr}_A R=I_2`$, one has $`\mathrm{Tr}K=2`$ and every eigenvalue of $`K`$ is at most one. If $`K`$ has a negative eigenvalue, its positive eigenvalues must sum to more than two. It must therefore have at least three positive eigenvalues. In dimension four this leaves exactly one negative eigenvalue, three positive eigenvalues, and no zero eigenvalues. Thus $`\det K<0`$. Congruence by $`D^{1/2}`$ preserves inertia and multiplies the determinant by a positive number, so $`\det H<0`$.

Conversely, $`H\ge0`$ implies $`\det H\ge0`$. Combining this argument with (4) and the PPT criterion gives, on the entire state space including singular states,

```math
\rho\in\mathrm{SEP}
\quad\Longleftrightarrow\quad
f(\rho)\ge0.
\qquad\text{(5)}
```

This argument concerns the spectrum of fixed matrices associated with $`\rho`$. It does not require a physical implementation of the state-dependent whitening transformation.

## 3. A universal scalar is constant on a physical boundary patch

### 3.1. The image of the separable set

The separable set is compact and convex. It also has nonempty interior in $`\mathcal A`$. An explicit way to see the latter is to take the thirty-six product states

```math
\frac{I+\varepsilon\sigma_a}{2}
\otimes
\frac{I+\zeta\sigma_b}{2},
\qquad
a,b\in\{x,y,z\},\quad
\varepsilon,\zeta\in\{-1,1\}.
```

Their affine span is $`\mathcal A`$, because they span the local Pauli terms and all nine Pauli products. Their average is $`I_4/4`$, with every weight positive. A positive barycenter of a finite affinely spanning set lies in the interior of its convex hull. Hence this convex hull supplies an open separable neighborhood of $`I_4/4`$.

Let $`p`$ be any polynomial whose scalar value classifies all states. Continuity and connectedness imply

```math
p(\mathrm{SEP})=[a,b].
```

No entangled state can have a probability in this interval. Also $`a<b`$: if $`a=b`$, the polynomial would be constant on a nonempty open subset of $`\mathcal A`$, hence constant on all of $`\mathcal A`$, which cannot classify the two classes.

### 3.2. An explicit smooth boundary point

Set

```math
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},
\qquad
\tau=\frac{I_4}{6}+\frac{|\Phi^+\rangle\langle\Phi^+|}{3}.
\qquad\text{(6)}
```

The spectrum of $`\tau`$ is

```math
\left\{\frac12,\frac16,\frac16,\frac16\right\},
```

so $`\tau>0`$. If $`F`$ swaps the two qubits, then

```math
\tau^\Gamma=\frac{I_4+F}{6}
=\frac{P_{\mathrm{sym}}}{3},
```

whose spectrum is $`\{1/3,1/3,1/3,0\}`$.

The derivative of $`f`$ restricted to $`\mathcal A`$ is nonzero at $`\tau`$. For example, in the trace-zero direction

```math
X=|\Phi^+\rangle\langle\Phi^+|-\frac{I_4}{4},
```

the zero eigenvalue of $`\tau^\Gamma+tX^\Gamma`$ has derivative $`-3/4`$, while the other three eigenvalues equal $`1/3`$ at $`t=0`$. Therefore

```math
\left.\frac{d}{dt}f(\tau+tX)\right|_{t=0}
=-\frac1{36}\ne0.
```

The real implicit function theorem gives a connected smooth hypersurface patch $`\Sigma`$ of $`f=0`$ through $`\tau`$. Shrink the patch and its neighborhood so that $`\rho>0`$ and three eigenvalues of $`\rho^\Gamma`$ remain positive throughout that neighborhood. On $`\Sigma`$, the remaining eigenvalue is zero, so every state on the patch is separable. Negative values of that eigenvalue occur arbitrarily close to every point of $`\Sigma`$ and give physical entangled states.

For $`\sigma\in\Sigma`$, the number $`p(\sigma)`$ cannot lie in $`(a,b)`$, because continuity would place sufficiently nearby entangled probabilities in the same interval. Thus

```math
p(\Sigma)\subseteq\{a,b\}.
```

Connectedness of $`\Sigma`$ forces

```math
p(\rho)=c\quad\text{for every }\rho\in\Sigma
\qquad\text{(7)}
```

for one fixed endpoint $`c\in\{a,b\}`$.

Only disjoint scalar images were used. The classifier itself could be discontinuous or nonmonotone. The smooth geometry of the full-rank two-qubit boundary also appears in [Đoković (2006), Theorem 3.3](https://arxiv.org/pdf/quant-ph/0604190); (6) supplies the particular patch needed here.

## 4. Irreducibility and continuation on the trace-one space

### 4.1. Complexification of Hermitian coordinates

Give the Hermitian matrices their usual real coordinates: real diagonal entries and the real and imaginary parts of each upper-triangular entry. After complexification, the off-diagonal coordinates $`x,y`$ determine

```math
M_{ij}=x+iy,\qquad M_{ji}=x-iy.
```

This is an invertible complex-linear coordinate change, so the complexification is the space of generic complex $`4\times4`$ matrices. Partial transpose is an invertible trace-preserving linear map and consequently preserves irreducibility.

### 4.2. The generic determinant is irreducible

The zero set of the generic determinant consists of the matrices of rank at most three. Each is expressible as $`UV`$ with $`U\in\mathbb C^{4\times3}`$ and $`V\in\mathbb C^{3\times4}`$. The parameter space is irreducible, so the closure of its polynomial image is irreducible. That image is already the entire closed determinant-zero set.

It follows that the determinant has a single irreducible factor, possibly raised to a power. Its derivative is nonzero at $`\mathrm{diag}(1,1,1,0)`$, so that power is one. The determinant is therefore irreducible over $`\mathbb C`$.

### 4.3. Restricting the trace preserves degree and irreducibility

Choose $`t=\mathrm{Tr}M`$ and fifteen complementary linear coordinates $`x`$. The determinant becomes a homogeneous degree-four polynomial $`F(t,x)`$. Its restriction

```math
g(x)=F(1,x)
```

still has degree four: its highest-degree part is $`F(0,x)`$, and the determinant does not vanish identically on traceless matrices, as $`\mathrm{diag}(1,1,1,-3)`$ demonstrates.

If $`g`$ factored into two nonconstant polynomials, homogenizing the two factors with the coordinate $`t`$ would factor $`F`$. This contradicts the irreducibility of the generic determinant. Thus $`g`$, and hence $`f(\rho)=\det(\rho^\Gamma)`$ on $`\mathcal A`$, is **absolutely irreducible**.

### 4.4. A smooth real patch is sufficient for polynomial divisibility

Let $`h`$ be a real polynomial on $`\mathcal A`$ that vanishes on a nonempty open patch of the smooth real hypersurface $`f=0`$. At a smooth point, a real analytic implicit-function chart of this hypersurface extends to a holomorphic chart of its complexification. The restriction of $`h`$ vanishes on an open real subchart. Successive one-variable identity theorems make it vanish on the corresponding complex subchart.

A proper algebraic subset of an irreducible complex hypersurface has strictly smaller complex dimension and cannot contain such an open chart. Therefore $`h`$ vanishes on the whole complex hypersurface. The Nullstellensatz places $`h`$ in the radical of the principal ideal generated by $`f`$. That ideal is prime because $`f`$ is irreducible, so $`f`$ divides $`h`$.

Apply this result to $`h=p-c`$ using (7). We obtain

```math
p-c=fq
```

for a polynomial $`q`$. The quotient has real coefficients because $`p-c`$ and $`f`$ do, and complex conjugation preserves the identity and its unique quotient. Since $`f`$ has degree four, $`\deg q\le\deg p-4`$.

For a universal effect $`E`$, the polynomial is nonconstant, so $`q\ne0`$. This proves $`k\ge4`$ and (1). When $`k=4`$, $`q`$ is a nonzero constant, proving (2).

Finally, the constant $`c`$ equals $`p_E(\tau)`$ with $`\tau>0`$. If $`c=0`$, positivity and full rank of $`\tau^{\otimes k}`$ force $`E=0`$. If $`c=1`$, they force $`E=I`$. Both possibilities are incompatible with universality. Therefore $`0<c<1`$, completing the necessity part of R2.

An immediate consequence, used in [sampling_cost.md](sampling_cost.md), is that every determinant-zero density operator has probability $`c`$, including singular states far from the patch $`\Sigma`$.

## 5. A concrete four-copy observable

Label a computational basis of $`\mathcal H`$ by $`0,1,2,3`$, corresponding to $`00,01,10,11`$. Define the normalized totally antisymmetric vector

```math
|\Omega\rangle
=\frac1{\sqrt{24}}
\sum_{\pi\in S_4}\mathrm{sgn}(\pi)
|\pi(0)\rangle\otimes|\pi(1)\rangle
\otimes|\pi(2)\rangle\otimes|\pi(3)\rangle,
\qquad
P=|\Omega\rangle\langle\Omega|.
\qquad\text{(8)}
```

For every complex $`4\times4`$ matrix $`X`$, the action of $`X^{\otimes4}`$ on the one-dimensional exterior power gives

```math
\mathrm{Tr}(PX^{\otimes4})=\det X.
```

Take partial transpose on all four $`A`$ qubits of $`P`$:

```math
W=P^{\Gamma_{A_1A_2A_3A_4}}.
\qquad\text{(9)}
```

Partial transpose is self-adjoint under the trace pairing. Hence

```math
\mathrm{Tr}(W\rho^{\otimes4})
=\mathrm{Tr}\!\left(P(\rho^\Gamma)^{\otimes4}\right)
=f(\rho).
\qquad\text{(10)}
```

This supplies an explicit instance of the established polynomial-to-collective-observable construction; see [collective_measurements.md](collective_measurements.md) and [Brun (2004)](https://arxiv.org/abs/quant-ph/0401067).

## 6. Spectrum and binary normalization

Across the partition $`A_1A_2A_3A_4\,|\,B_1B_2B_3B_4`$, only weight-two computational strings occur in $`|\Omega\rangle`$. Order those strings on each side as

```math
0011,\quad0101,\quad0110,\quad1001,\quad1010,\quad1100.
```

The bipartite coefficient matrix is $`M/\sqrt{24}`$, with

```math
M=
\begin{pmatrix}
0&1&-1&-1&1&0\\
-1&0&1&1&0&-1\\
1&-1&0&0&-1&1\\
1&-1&0&0&-1&1\\
-1&0&1&1&0&-1\\
0&1&-1&-1&1&0
\end{pmatrix}.
\qquad\text{(11)}
```

Put $`K=MM^T`$. Direct multiplication gives

```math
K^2=12K,\qquad \mathrm{Tr}K=24.
```

Because $`K\ge0`$, its only possible eigenvalues are zero and twelve, and exactly two eigenvalues equal twelve. The two nonzero squared Schmidt coefficients of $`|\Omega\rangle`$ are therefore $`1/2,1/2`$.

For a pure bipartite state with Schmidt coefficients $`s_i`$, its partial transpose has eigenvalues $`s_i^2`$ and $`\pm s_i s_j`$ for $`i<j`$. This follows by diagonalizing the two-dimensional subspaces spanned by $`|ij\rangle`$ and $`|ji\rangle`$. Applied here, it gives

```math
\mathrm{spec}W=
\left\{
\frac12\ \text{with multiplicity }3,\,
-\frac12\ \text{with multiplicity }1,\,
0\ \text{with multiplicity }252
\right\}.
\qquad\text{(12)}
```

Thus

```math
E_*=\frac{I}{2}+W
\qquad\text{(13)}
```

is a valid binary effect. Its outcome probability is

```math
p_{E_*}(\rho)=\frac12+f(\rho).
\qquad\text{(14)}
```

By (5), the exact threshold $`p_{E_*}=1/2`$ distinguishes the classes, with equality assigned to separability. This proves four-copy sufficiency.

## 7. Which four-copy probabilities are physically feasible?

Let $`U_\pi`$ permute the four entire two-qubit copies. For any effect $`E`$, its permutation average

```math
\overline E=\frac1{24}\sum_{\pi\in S_4}U_\pi E U_\pi^\dagger
\qquad\text{(15)}
```

is still an effect and has the same expectation on every $`\rho^{\otimes4}`$. The observable $`W`$ is also permutation invariant: the projector $`P`$ is invariant, and the chosen partial transpose commutes with conjugation by these real copy-permutation matrices.

Suppose $`p_E=c+\alpha f`$. We claim

```math
\overline E=cI+\alpha W.
\qquad\text{(16)}
```

Let $`Q`$ be the difference between the two sides. Its expectation on $`\rho^{\otimes4}`$ vanishes for every density operator. By positive rescaling, it vanishes on $`X^{\otimes4}`$ for every positive-definite Hermitian $`X`$. This is a homogeneous polynomial identity, so it holds for every Hermitian $`X`$.

Polarization now shows that $`Q`$ has zero inner product with every symmetrized tensor product

```math
\frac1{24}\sum_{\pi\in S_4}
A_{\pi(1)}\otimes A_{\pi(2)}
\otimes A_{\pi(3)}\otimes A_{\pi(4)},
```

where the $`A_i`$ are arbitrary Hermitian matrices. Such products span the permutation-invariant Hermitian operator space: start with tensor products of a Hermitian matrix basis and apply the permutation average. Since $`Q`$ belongs to this invariant space, it is orthogonal to itself. Therefore $`\mathrm{Tr}(Q^2)=0`$ and $`Q=0`$, proving (16).

Using (12), the effect constraints $`0\le\overline E\le I`$ are equivalent to

```math
0\le c+\frac{\alpha}{2}\le1,
\qquad
0\le c-\frac{\alpha}{2}\le1.
```

These are precisely (3). Conversely, every pair satisfying (3) gives a valid effect $`cI+\alpha W`$, and $`\alpha\ne0`$ makes its probability universal by (5). This proves the full feasibility statement.

The largest possible value of $`|\alpha|`$ is one, attained at $`c=1/2`$. It also maximizes the local Bernoulli relative-entropy coefficient at the boundary:

```math
D_{\mathrm{KL}}\!\left(
\mathrm{Ber}(c+\alpha z)\,\middle\Vert\,\mathrm{Ber}(c)
\right)
=\frac{\alpha^2z^2}{2c(1-c)}+O(z^3),
\qquad
\frac{\alpha^2}{2c(1-c)}\le2.
```

This is an optimum for the probability scale and the local divergence coefficient. It is not a claim of a global finite-sample optimum over all normalizations and decision rules.

## 8. Scope

The lower bound permits every fixed finite $`k`$ and every exact classical decision function. It concerns arbitrary mixed two-qubit states and the one probability of a binary measurement. A setting with many retained outcome probabilities, a family of changing measurement settings, or a promise restricting inputs to pure states defines a different problem.

At degrees above four, the factorization (1) is necessary but not by itself sufficient. For example, a quotient $`q`$ that vanishes at an entangled state makes that state's probability coincide with $`c`$. No complete characterization of the higher-degree admissible quotients is needed for R2 or the sampling theorem.

Exact classification here means identifiability from the true probability. The number of experimental repetitions needed to estimate that probability is a separate resource, addressed by result R3 in [sampling_cost.md](sampling_cost.md).

The source dependencies and their scopes are collected in [RELATED_WORK.md](../references/RELATED_WORK.md). The determinant criterion and four-copy existence are established ingredients; the argument above states and proves the stronger necessity and probability-rigidity conclusions in the specified model.
