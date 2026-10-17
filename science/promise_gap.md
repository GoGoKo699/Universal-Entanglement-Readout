# Binary block size under a distance promise

The exact qubit–qutrit scalar obstruction disappears when the detector is allowed to ignore a nonzero neighborhood of the separable boundary. Its block size must nevertheless grow as that neighborhood shrinks. This supporting result concerns the number of copies processed within a block and assumes arbitrary probability resolution.

Use the [fixed apparatus model](model.md) and distance $`\Delta(\rho)=\inf_{\sigma\in\mathrm{SEP}}\Vert\rho-\sigma\Vert_1/2`$. Let $`k_{\mathrm{gap}}(\delta)`$ be the least integer $`k`$ for which a binary effect on $`k`$ qubit–qutrit copies distinguishes all separable states from all states with $`\Delta(\rho)\ge\delta`$ through its exactly known probability. The effect may depend on $`\delta`$, and no decision is required for $`0<\Delta(\rho)<\delta`$.

**Theorem S1.** At fixed local dimensions $`2\times3`$,

```math
k_{\mathrm{gap}}(\delta)=\Theta\!\left(\log\frac1\delta\right)
\qquad(\delta\downarrow0).
```

The lower bound permits arbitrary classical processing of the scalar. The upper bound gives a state-independent binary POVM, but gives no useful uniform bound on its probability margin. It therefore supplies no logarithmic total-copy or gate-complexity guarantee.

## 1. A physical quadrant with a certified distance

The explicit family in [Outcome minima](outcome_minima.md) has the form

```math
\rho(s,t)=(1-s-t)\rho_0+s(|u\rangle\langle u|)^\Gamma+t(|v\rangle\langle v|)^\Gamma,
\qquad |s|,|t|\le r=10^{-4}.
```

Here $`\rho_0>0`$, and $`u,v`$ are orthonormal vectors in the kernel of $`\rho_0^\Gamma`$. Throughout the square the states are full rank. Their partial transposes have eigenvalues $`s,t`$ and four positive eigenvalues. Therefore

```math
\rho(s,t)\in\mathrm{SEP}\quad\Longleftrightarrow\quad s\ge0\text{ and }t\ge0.
```

Both $`u`$ and $`v`$ have two equal Schmidt coefficients. Thus the witnesses

```math
W_s=(|u\rangle\langle u|)^\Gamma,\qquad W_t=(|v\rangle\langle v|)^\Gamma
```

have operator norm $`1/2`$. If $`s\le-\delta`$, then for every separable $`\sigma`$,

```math
\delta\le-s\le\mathrm{Tr}[W_s(\sigma-\rho(s,t))]
\le\frac12\Vert\sigma-\rho(s,t)\Vert_1.
```

The same argument applies when $`t\le-\delta`$. A negative coordinate of magnitude at least $`\delta`$ therefore certifies the required trace-distance promise, regardless of the other coordinate.

## 2. Lower bound from two majority functions

Suppose $`p(\rho)=\mathrm{Tr}(E\rho^{\otimes k})`$ solves the promised problem. Since $`\mathrm{SEP}`$ is compact and connected, its scalar image is an interval $`[a,b]`$. Every entangled state satisfying the distance promise must have its probability outside that interval. This assertion uses only correctness of the decision map, not any assumed threshold structure.

For sufficiently small $`\delta`$, choose an odd integer $`n\le r/\delta`$ with $`n=\Theta(r/\delta)`$, and substitute

```math
s=\frac rn\sum_{i=1}^n x_i,\qquad
t=\frac rn\sum_{i=1}^n y_i,\qquad x_i,y_i\in\{-1,1\}.
```

Odd $`n`$ excludes ties, so every coordinate has absolute value at least $`r/n\ge\delta`$. These states are separable precisely when both Boolean sums are positive. Every other grid state satisfies the promised entanglement gap.

On this finite grid, choose $`\zeta>0`$ smaller than the minimum of $`(p-a)(p-b)`$ over the entangled grid points. The polynomial

```math
Q(s,t)=[p(\rho(s,t))-a][p(\rho(s,t))-b]-\zeta
```

is strictly negative on the separable grid and strictly positive on its complement. This also works if $`a=b`$. Its degree is at most $`2k`$, and substitution of the two linear Boolean sums does not increase that degree.

The threshold degree of a Boolean function is the least degree of a real polynomial with its prescribed strict signs on every Boolean input. Sherstov's Theorem 1.10 proves

```math
\deg_{\pm}(\mathrm{MAJ}_n\wedge\mathrm{MAJ}_n)=\Omega(\log n).
```

The two majorities act on independent sets of $`n`$ variables. Reversal of every output sign leaves threshold degree unchanged. Applying this imported theorem [Sherstov2013](../references/RELATED_WORK.md#sherstov2013) gives $`2k=\Omega(\log n)`$ and hence

```math
k=\Omega\!\left(\log\frac1\delta\right).
```

Only a strict sign representation on a finite Boolean grid is used. No continuum extension of the threshold-degree theorem is assumed.

## 3. A characteristic-coefficient gap

For the upper bound, put $`H=\rho^\Gamma`$, with real eigenvalues $`\lambda_1,\ldots,\lambda_6`$, and let $`e_j=e_j(H)`$ be their elementary symmetric polynomials. The first two coefficients satisfy

```math
e_1=1,\qquad e_2=\frac{1-\mathrm{Tr}(H^2)}2
=\frac{1-\mathrm{Tr}(\rho^2)}2\ge0.
```

A Hermitian $`H`$ is positive semidefinite if and only if all its $`e_j`$ are nonnegative. One direction follows directly from nonnegative eigenvalues. For the converse, nonnegative coefficients make

```math
\det(xI+H)=x^6+e_1x^5+e_2x^4+e_3x^3+e_4x^2+e_5x+e_6
```

strictly positive for every $`x>0`$, excluding a negative eigenvalue. Thus in $`2\times3`$ it suffices to decide the conjunction $`e_3,e_4,e_5,e_6\ge0`$. This four-coefficient criterion is also a useful comparison with [ZhangXie2026](../references/RELATED_WORK.md#zhangxie2026); S1 does not claim that this criterion or polynomial measurement itself is new.

If $`\Delta(\rho)\ge\delta`$ and $`\lambda_{\min}(H)=-\alpha<0`$, then

```math
\sigma=\frac{\rho+\alpha I}{1+6\alpha}
```

is a density operator with positive partial transpose, hence is separable. Expressing $`\sigma`$ as a convex mixture of $`\rho`$ and $`I/6`$ shows

```math
\Delta(\rho)\le\frac{6\alpha}{1+6\alpha}\le6\alpha,
\qquad\alpha\ge\frac\delta6.
```

The Hilbert–Schmidt norm is invariant under partial transpose, so $`|\lambda_i|\le\Vert H\Vert_2=\Vert\rho\Vert_2\le1`$. Consequently $`\alpha\le1`$ and $`|e_j|\le\binom6j\le20`$. At the positive root $`x=\alpha`$, the first three terms of $`\det(xI+H)`$ are nonnegative. At least one $`j\in\{3,4,5,6\}`$ must therefore satisfy

```math
e_j\le-\frac{\alpha^6}{\alpha^3+\alpha^2+\alpha+1}
\le-\frac{\delta^6}{4\,6^6}.
```

This provides a uniform negative coefficient gap from the physical distance promise.

## 4. An explicit bounded rational sign filter

Set

```math
\gamma=\frac{\delta^6}{4\,6^6\,64},\qquad
\varepsilon=\frac\gamma2,\qquad
x_j=\frac{e_j}{64}+\frac\gamma2\quad(j=3,4,5,6).
```

For $`0<\delta\le1`$ these numbers lie in $`[-1,1]`$. Every separable state has $`x_j\ge\varepsilon`$ for all four indices. Every promised entangled state has at least one $`x_j\le-\varepsilon`$.

Choose

```math
L=\left\lceil\log_2\frac1\varepsilon\right\rceil,
\qquad a_\ell=\varepsilon2^\ell\quad(\ell=0,\ldots,L),
\qquad A(x)=\prod_{\ell=0}^{L}(x+a_\ell)^2,
```

and define

```math
N(x)=A(x)-A(-x),\qquad D(x)=A(x)+A(-x),\qquad R(x)=\frac{N(x)}{D(x)}.
```

The polynomials $`A(x)`$ and $`A(-x)`$ have disjoint real root sets, so $`D(x)>0`$ for every real $`x`$. Both are nonnegative. Hence $`|R(x)|\le1`$ and $`R(-x)=-R(x)`$ everywhere.

If $`\varepsilon\le x\le1`$, one grid node satisfies $`a_\ell\le x<2a_\ell`$. Its factor in

```math
\frac{A(-x)}{A(x)}=\prod_{\ell=0}^{L}\left(\frac{x-a_\ell}{x+a_\ell}\right)^2
```

is at most $`1/9`$, while every other factor is at most one. It follows that

```math
R(x)\ge\frac45\quad(x\ge\varepsilon),\qquad
R(x)\le-\frac45\quad(x\le-\varepsilon),
```

within the interval $`[-1,1]`$. Therefore

```math
\sum_{j=3}^6R(x_j)\ge\frac{16}{5}>3
\quad\text{on separable states},
```

whereas the sum is at most $`3-4/5=11/5<3`$ on promised entangled states. Boundedness on the transition interval is essential because the other three coordinates of an entangled state need not satisfy any gap condition.

## 5. Clearing denominators and realizing one binary probability

Define

```math
q(\rho)=\sum_{j=3}^6N(x_j)\prod_{\substack{i=3\\i\ne j}}^6D(x_i)
-3\prod_{i=3}^6D(x_i).
```

Every denominator is positive, so $`q`$ is positive on all separable states and negative on every state with $`\Delta(\rho)\ge\delta`$. Since $`e_j`$ has degree $`j`$ in $`\rho`$,

```math
\deg q\le2(L+1)(3+4+5+6)=36(L+1)
=O\!\left(\log\frac1\delta\right).
```

The polynomial representation in [Collective measurements](collective_measurements.md) gives a Hermitian $`W`$ on at most $`36(L+1)`$ copies with $`q(\rho)=\mathrm{Tr}(W\rho^{\otimes k})`$, padding lower degrees with trace factors. With any finite certified $`M\ge\max(1,\Vert W\Vert_\infty)`$,

```math
E=\frac12\left(I+\frac WM\right)
```

is a valid fixed binary effect. Its probability is greater than $`1/2`$ on every separable state and less than $`1/2`$ on every promised entangled state. This completes the upper bound and the proof of S1.

Polynomial-to-observable realization is inherited from [Brun2004](../references/RELATED_WORK.md#brun2004-and-leifer2004). The bounded rational filter uses the established connection between rational sign approximation and conjunctions, discussed with attribution in [Sherstov2013](../references/RELATED_WORK.md#sherstov2013). The asserted contribution is the stated quantum block-size law and its operational reduction, not a new threshold-degree or rational-approximation theorem.

## Interpretation and exact checks

For each fixed nonzero $`\delta`$, the strict separation on two compact state sets gives a positive probability margin after normalization. The proof does not give a useful asymptotic lower bound on that margin. Estimating it may require many repetitions, and representing a polynomial by a Hermitian effect alone supplies no efficient gate decomposition.

The lower bound embeds into larger bipartite dimensions. The matching upper bound proved here uses $`\mathrm{PPT}=\mathrm{SEP}`$ specifically in $`2\times3`$. No complete higher-dimensional criterion is inferred from semialgebraicity alone.

[The exact filter check](../verification/verify_gap_filter.py) verifies oddness, boundedness, geometric endpoint inequalities, a four-coordinate conjunction grid, and physical state examples. It complements the uniform inequalities above. The asymptotic lower bound rests on the imported theorem and the analytical reduction, not on this finite computation. See [Verification](../verification/README.md) and [Related work](../references/RELATED_WORK.md).
