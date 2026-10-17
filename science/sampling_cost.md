# Sampling cost of an exactly universal binary detector

For arbitrary mixed two-qubit states, keeping a fixed finite block size and one binary outcome imposes a sharp statistical cost on exact universal detectors. To distinguish separability from entanglement at half-trace distance at least $`\delta`$, the optimal number of independent repetitions is

```math
\Theta_k\!\left(\delta^{-8}\log\frac1\eta\right)
```

for fixed $`k\ge4`$ and error target $`\eta\le1/4`$. The constants are uniform over all exactly universal effects with that block size, even when the effect is selected using the promised gap.

This document proves result **R3**. Its algebraic input is the determinant factorization proved in [binary_rigidity.md](binary_rigidity.md). Measurement conventions are defined in [model.md](model.md).

## 1. Statistical model and minimax statement

Let $`\mathrm{SEP}`$ be the set of separable two-qubit states, and define

```math
\Delta(\rho)
=\inf_{\sigma\in\mathrm{SEP}}
\frac12\Vert\rho-\sigma\Vert_1.
\tag{1}
```

Fix an integer $`k\ge4`$. In each of $`n`$ independent runs, a fixed effect $`0\le E\le I`$ acts on a fresh block of $`k`$ copies of the same unknown state. The retained outcomes are independent Bernoulli variables with probability

```math
p_E(\rho)=\mathrm{Tr}(E\rho^{\otimes k}).
```

The effect is required to be exactly universal on **all** mixed two-qubit states: some function of its true probability must classify every separable and every entangled state. Let $`\mathcal U_k`$ denote this class of effects.

For $`0<\delta\le1/2`$ and $`0<\eta<1/2`$, define $`n_k^*(\delta,\eta)`$ as the least integer $`n`$ for which some $`E\in\mathcal U_k`$ and some possibly randomized function of the entire retained bit string have both errors at most $`\eta`$ for

```math
H_0:\rho\in\mathrm{SEP},
\qquad
H_1:\Delta(\rho)\ge\delta.
\tag{2}
```

Both $`E`$ and the finite-sample decision rule may depend on $`\delta`$ and $`\eta`$. The requirement $`E\in\mathcal U_k`$ still applies to all mixed states, including states outside the promise in (2).

### R3. Uniform repetition bounds

Set

```math
B_k=\frac{\pi^4}{24}\,k^4\,6^k
=\frac23\,k^4\,6^k\left(\frac\pi2\right)^4,
\qquad
L_\eta=(1-2\eta)\log\frac{1-\eta}{\eta},
\tag{3}
```

where logarithms are natural. Then

```math
\frac{L_\eta}{B_k^2\delta^8}
\ \le\
n_k^*(\delta,\eta)
\ \le\
\left\lceil2\delta^{-8}\log\frac1\eta\right\rceil.
\tag{4}
```

For $`0<\eta\le1/4`$, one has

```math
\frac14\log\frac1\eta
\le L_\eta
\le\log\frac1\eta.
```

Thus (4) gives the stated $`\Theta_k`$ law. Its lower constant depends on $`k`$, but is independent of the chosen effect and of $`\delta,\eta`$.

The resource in (4) is the number of independent runs. If each block uses exactly $`k`$ copies, the total number of input copies is $`kn`$. Padding the four-copy construction with unused copies gives the upper bound for every fixed $`k\ge4`$. The dependence of $`B_k`$ on $`k`$ is deliberately crude; (4) is not an optimal joint tradeoff when $`k`$ grows as the gap shrinks.

## 2. Determinant and distance to separability

Write

```math
f(\rho)=\det(\rho^\Gamma),
```

with $`\Gamma`$ the partial transpose on $`A`$. For entangled two-qubit states, the established determinant-concurrence inequality is

```math
C(\rho)\le2|f(\rho)|^{1/4}.
\tag{5}
```

Here $`C`$ is the usual convex-roof concurrence. Equation (5) is the combination of Eqs. (3) and (5) in [Augusiak, Demianowicz, and Horodecki (2008)](https://arxiv.org/pdf/quant-ph/0604109): their $`\pi_2`$ equals $`2|f|^{1/4}`$ on entangled states and bounds concurrence from above. Concurrence and its pure-state decompositions are described in [Wootters (1998)](https://arxiv.org/abs/quant-ph/9709029).

### 2.1. A direct comparison with trace distance

For a pure state with Schmidt weights $`\lambda`$ and $`1-\lambda`$, remove the coherence between the two Schmidt terms. The resulting state $`\sigma_\psi`$ is separable, and

```math
\frac12\bigl\Vert|\psi\rangle\langle\psi|-\sigma_\psi\bigr\Vert_1
=\sqrt{\lambda(1-\lambda)}
=\frac{C(|\psi\rangle)}2.
```

Indeed, the difference is a two-dimensional matrix with off-diagonal entries $`\sqrt{\lambda(1-\lambda)}`$ and eigenvalues of equal magnitude and opposite sign.

For any pure-state ensemble $`\rho=\sum_i p_i|\psi_i\rangle\langle\psi_i|`$, the state $`\sum_i p_i\sigma_{\psi_i}`$ is separable. Convexity of the trace norm gives

```math
\Delta(\rho)\le\frac12\sum_i p_i C(|\psi_i\rangle).
```

Taking the infimum over ensembles yields

```math
\Delta(\rho)\le\frac{C(\rho)}2.
\tag{6}
```

Combining (5) and (6) proves

```math
|f(\rho)|\ge\Delta(\rho)^4
\qquad\text{for every entangled two-qubit state.}
\tag{7}
```

Since entanglement is equivalent to $`f<0`$, (7) supplies a uniform signed probability gap for the upper bound.

### 2.2. A family attaining the fourth power

For $`0\le\theta\le\pi/4`$, let

```math
|\psi_\theta\rangle
=\cos\theta\,|00\rangle+\sin\theta\,|11\rangle,
\qquad
\rho_\theta=|\psi_\theta\rangle\langle\psi_\theta|,
\qquad
\delta_\theta=\sin\theta\cos\theta.
\tag{8}
```

Its partial transpose has eigenvalues

```math
\cos^2\theta,\quad
\sin^2\theta,\quad
\delta_\theta,\quad
-\delta_\theta.
```

Therefore

```math
f(\rho_\theta)=-\delta_\theta^4.
\tag{9}
```

Schmidt dephasing gives $`\Delta(\rho_\theta)\le\delta_\theta`$. To prove equality, define

```math
|\Psi^-\rangle=\frac{|01\rangle-|10\rangle}{\sqrt2},
\qquad
V=(|\Psi^-\rangle\langle\Psi^-|)^\Gamma.
```

One has $`\Vert V\Vert_\infty=1/2`$ and

```math
\mathrm{Tr}(V\rho_\theta)=-\delta_\theta,
\qquad
\mathrm{Tr}(V\sigma)\ge0
\quad\text{for every }\sigma\in\mathrm{SEP}.
```

The latter inequality follows from positivity of the partial transpose of a separable state. Trace-norm duality then gives

```math
\delta_\theta
\le\mathrm{Tr}\bigl(V(\sigma-\rho_\theta)\bigr)
\le\frac12\Vert\sigma-\rho_\theta\Vert_1.
```

Taking the infimum proves

```math
\Delta(\rho_\theta)=\delta_\theta.
\tag{10}
```

Every $`\delta\in[0,1/2]`$ is realized by

```math
\theta=\frac12\arcsin(2\delta).
```

For the statistical lower bound, the separable comparator will be

```math
\rho_0=|00\rangle\langle00|.
\tag{11}
```

It need not be the closest separable state to $`\rho_\theta`$. The rigidity theorem makes its measured probability exactly the same boundary value used below.

## 3. A probability bound uniform over all universal effects

The rigidity theorem gives, for every $`E\in\mathcal U_k`$,

```math
p_E(\rho)=c+f(\rho)q(\rho),
\qquad
0<c<1,
\qquad
\deg q\le k-4.
\tag{12}
```

Bounding $`q`$ separately for each effect would give a lower bound with uncontrolled effect-dependent constants. The following argument is uniform even when $`E`$ changes with $`\delta`$.

### 3.1. The full-rank boundary controls the scale of the effect

Use the separable boundary state

```math
\tau=\frac{I_4}{6}
+\frac{|\Phi^+\rangle\langle\Phi^+|}{3},
\qquad
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}.
\tag{13}
```

It satisfies $`\tau\ge I_4/6`$ and $`f(\tau)=0`$, so (12) gives

```math
c=\mathrm{Tr}(E\tau^{\otimes k}),
\qquad
1-c=\mathrm{Tr}\bigl((I-E)\tau^{\otimes k}\bigr).
```

Since $`\tau^{\otimes k}\ge6^{-k}I`$,

```math
\Vert E\Vert_\infty\le\mathrm{Tr}E\le6^k c,
\qquad
\Vert I-E\Vert_\infty\le\mathrm{Tr}(I-E)\le6^k(1-c).
\tag{14}
```

These inequalities hold for every effect in the class. They also show directly why a nontrivial universal effect cannot have $`c=0`$ or $`c=1`$.

### 3.2. Fourth-order flatness along the family in (8)

The Hermitian generator

```math
G=i\bigl(|11\rangle\langle00|-|00\rangle\langle11|\bigr)
```

has norm one and satisfies

```math
|\psi_\theta\rangle=e^{-i\theta G}|00\rangle.
```

On $`k`$ copies, the generator is

```math
G_k=\sum_{j=1}^k
I^{\otimes(j-1)}\otimes G\otimes I^{\otimes(k-j)},
\qquad
\Vert G_k\Vert_\infty\le k.
```

Write $`u(\theta)=p_E(\rho_\theta)`$. Differentiating the unitary orbit four times and using

```math
\Vert[G_k,X]\Vert_1\le2\Vert G_k\Vert_\infty\Vert X\Vert_1
```

gives

```math
|u^{(4)}(\theta)|\le(2k)^4\Vert E\Vert_\infty.
```

The fourth derivative obtained from the complementary effect is $`-u^{(4)}(\theta)`$, because its probability is $`1-u(\theta)`$. Therefore (14) improves the bound to

```math
|u^{(4)}(\theta)|
\le(2k)^4\,6^k\min(c,1-c).
\tag{15}
```

By (9) and (12),

```math
u(\theta)-c
=-\sin^4\theta\cos^4\theta\,q(\rho_\theta).
```

Thus $`u(0)=c`$ and $`u'(0)=u''(0)=u'''(0)=0`$. Taylor's theorem gives

```math
|u(\theta)-c|
\le\frac{\theta^4}{24}(2k)^4\,6^k\min(c,1-c).
```

For $`0\le\theta\le\pi/4`$, concavity of the sine on $`[0,\pi/2]`$ implies

```math
\delta_\theta=\frac{\sin(2\theta)}2\ge\frac{2\theta}{\pi}.
```

Using $`\theta\le\pi\delta_\theta/2`$ and (3), we obtain

```math
|p_E(\rho_\theta)-c|
\le B_k\min(c,1-c)\delta_\theta^4.
\tag{16}
```

No coefficient bound on $`q`$ and no lower bound on $`c`$ independent of $`E`$ were assumed.

## 4. Information-theoretic lower bound

For $`p\in[0,1]`$ and $`c\in(0,1)`$, the elementary inequality $`\log x\le x-1`$ gives

```math
\begin{aligned}
D_{\mathrm{KL}}\bigl(\mathrm{Ber}(p)\Vert
\mathrm{Ber}(c)\bigr)
&=p\log\frac pc+(1-p)\log\frac{1-p}{1-c}\\
&\le\frac{(p-c)^2}{c(1-c)}.
\end{aligned}
\tag{17}
```

The endpoint cases use the continuous convention $`0\log0=0`$.

Fix the state $`\rho_\theta`$ with $`\delta_\theta=\delta`$. By (12), the product comparator (11) has probability $`c`$. Combining (16) and (17) yields

```math
\begin{aligned}
D_{\mathrm{KL}}\bigl(
\mathrm{Ber}(p_E(\rho_\theta))\Vert
\mathrm{Ber}(p_E(\rho_0))
\bigr)
&\le
B_k^2
\frac{\min(c,1-c)^2}{c(1-c)}
\delta^8\\
&\le B_k^2\delta^8.
\end{aligned}
\tag{18}
```

This estimate is uniform over $`\mathcal U_k`$.

Relative entropy adds for independent repetitions. For a randomized decision rule, append its independent random seed to the data; that seed contributes zero relative entropy. Data processing then bounds the relative entropy of the final decision by $`nB_k^2\delta^8`$.

Under $`\rho_\theta`$, the probability of an entangled decision must be at least $`1-\eta`$. Under $`\rho_0`$, it must be at most $`\eta`$. The relative entropy between these two decision distributions is minimized at the boundary probabilities $`1-\eta,\eta`$. Hence it is at least

```math
\begin{aligned}
D_{\mathrm{KL}}\bigl(
\mathrm{Ber}(1-\eta)\Vert
\mathrm{Ber}(\eta)
\bigr)
&=(1-2\eta)\log\frac{1-\eta}{\eta}\\
&=L_\eta.
\end{aligned}
```

Consequently,

```math
nB_k^2\delta^8\ge L_\eta,
```

which proves the lower half of (4).

The proof permits arbitrary classical use of the complete ordered bit string. It also permits the fixed effect to be selected using $`\delta`$ and $`\eta`$, because (18) holds uniformly for every allowed effect. The theorem is stated for a fixed number of independent repetitions of that effect; no assertion about adaptive measurement changes or random stopping times is needed.

## 5. Matching four-copy upper bound

Let

```math
W=(|\Omega\rangle\langle\Omega|)^{\Gamma_{A_1A_2A_3A_4}},
```

where $`|\Omega\rangle`$ is the normalized totally antisymmetric vector of four four-level systems. The explicit vector and its Schmidt matrix are given in [binary_rigidity.md](binary_rigidity.md). Its spectrum is

```math
\mathrm{spec}W=
\left\{
\frac12\ \text{with multiplicity }3,\,
-\frac12\ \text{with multiplicity }1,\,
0\ \text{with multiplicity }252
\right\}.
```

Thus the effect

```math
E_*=\frac I2+W
```

is valid and has

```math
p_{E_*}(\rho)=\frac12+f(\rho).
```

The determinant criterion and (7) imply

```math
\begin{array}{ll}
\rho\in\mathrm{SEP}:&
p_{E_*}(\rho)\ge\frac12,\\[2mm]
\Delta(\rho)\ge\delta:&
p_{E_*}(\rho)\le\frac12-\delta^4.
\end{array}
\tag{19}
```

Let $`\widehat p`$ be the empirical frequency of outcome one. Declare entanglement when

```math
\widehat p<\frac12-\frac{\delta^4}{2}.
```

The two promised classes are each separated from this threshold by at least $`\delta^4/2`$. Hoeffding's inequality gives each error at most

```math
\exp\left(-2n\left(\frac{\delta^4}{2}\right)^2\right)
=\exp(-n\delta^8/2).
```

Taking

```math
n=\left\lceil2\delta^{-8}\log\frac1\eta\right\rceil
```

therefore proves the upper half of (4) at $`k=4`$. The same effect tensored with the identity on $`k-4`$ unused copies proves it for every $`k\ge4`$.

The apparatus is independent of $`\delta`$. Only the finite-sample threshold and repetition count use the promise. Although this four-copy effect maximizes the local probability sensitivity among four-copy exactly universal effects, the upper bound here only claims the matching asymptotic law and the explicit sufficient repetition count.

## 6. Comparison with unrestricted measurements

The exponent eight is an architectural cost of exact universal binary readout with fixed finite block size. The ordinary fixed-dimensional promise problem can use a richer retained measurement record and has total-copy complexity

```math
\Theta\!\left(\delta^{-2}\log\frac1\eta\right)
```

for $`0<\delta\le1/2`$ and $`0<\eta\le1/4`$. The following elementary argument records the comparison without imposing a growing-dimensional efficiency claim.

### 6.1. Tomographic upper bound

Measure each of the fifteen nonidentity two-qubit Pauli observables on fresh copies, retaining its label and its $`\pm1`$ outcome. If each estimated expectation has error at most $`\varepsilon`$, the Pauli expansion gives a Hermitian trace-one estimate $`\widetilde\rho`$ with

```math
\frac12\Vert\widetilde\rho-\rho\Vert_1
\le\Vert\widetilde\rho-\rho\Vert_2
\le\frac{\sqrt{15}}2\varepsilon.
```

Here $`\Vert\cdot\Vert_2`$ is the Hilbert-Schmidt norm, and the first inequality uses the matrix dimension four. Replace $`\widetilde\rho`$ by a nearest density operator $`\widehat\rho`$ in trace norm. Since the true state is a feasible density operator, the triangle inequality increases the error by at most a factor of two. Set $`\varepsilon=\delta/(3\sqrt{15})`$. Hoeffding's inequality for the $`\pm1`$ outcomes and a union bound over the fifteen observables show that

```math
N=\left\lceil270\delta^{-2}\log\frac{30}{\eta}\right\rceil
```

copies per observable suffice to make all fifteen errors at most $`\varepsilon`$ with probability at least $`1-\eta`$. The total is $`15N`$ copies, and the resulting estimate obeys

```math
\frac12\Vert\widehat\rho-\rho\Vert_1\le\frac{\delta}{3}
```

except with probability $`\eta`$. Distance to a fixed closed set is one-Lipschitz in the same metric. Thresholding $`\Delta(\widehat\rho)`$ between $`\delta/3`$ and $`2\delta/3`$ therefore solves the promise problem. The finitely many constants depend only on the two-qubit dimension. More general state-estimation results are given by [Haah et al. (2017)](https://arxiv.org/abs/1508.01797).

This scheme retains several measurement statistics. It does not define one exactly universal binary probability.

### 6.2. A matching total-copy lower bound

The full-rank boundary state (13) also supplies a commuting family

```math
\widetilde\rho_\delta
=\tau+\frac{4\delta}{3}
\left(|\Phi^+\rangle\langle\Phi^+|-\frac{I_4}{4}\right),
\qquad 0<\delta\le\frac12.
```

Its eigenvalues are $`1/2+\delta`$ on $`|\Phi^+\rangle`$ and $`1/6-\delta/3`$ on each of the three orthogonal directions. It is a density operator. Its partial transpose has negative eigenvalue $`-\delta`$ with eigenvector $`|\Psi^-\rangle`$. The witness $`V`$ from Section 2 gives $`\Delta(\widetilde\rho_\delta)\ge\delta`$, while

```math
\frac12\Vert\widetilde\rho_\delta-\tau\Vert_1=\delta.
```

Thus $`\Delta(\widetilde\rho_\delta)=\delta`$.

Because the two states commute, their quantum relative entropy is

```math
D(\widetilde\rho_\delta\Vert\tau)
=D_{\mathrm{KL}}\bigl(
\mathrm{Ber}(1/2+\delta)\Vert
\mathrm{Ber}(1/2)
\bigr)
\le4\delta^2.
```

Any protocol on $`T`$ copies, including an arbitrary joint measurement, obeys quantum data processing. Repeating the decision-distribution argument of Section 4 gives

```math
T\ge\frac{L_\eta}{4\delta^2}.
```

This comparison isolates the resource restriction responsible for (4). It does not change the class of effects in R3.

## 7. Boundaries of the theorem

- **Global universality versus gap-only testing.** The effect in R3 must identify every mixed state from its exact probability. An effect required to separate only the two promised classes in (2) need not satisfy the determinant factorization and is outside this minimax class.
- **Block size versus total copies.** One run uses $`k`$ copies. The theorem bounds the repetitions at fixed $`k`$ and hence the total copies $`kn`$ at that fixed architecture. The exponential $`k`$-dependence of the displayed lower-bound constant does not settle the best rate when the block size changes with $`\delta`$.
- **Binary probability versus a full histogram.** A measurement with $`m`$ retained outcome labels has $`m-1`$ probability coordinates after normalization. Retaining labels or conditional pointer information also enlarges the statistical record.
- **Arbitrary mixed inputs versus a purity promise.** The hard instances in (8) are pure, but the detector must also classify every mixed state. A detector promised pure inputs has different constraints and can use quantities that fail as universal mixed-state classifiers.
- **Exact probabilities versus finite data.** Exact universality is an identifiability property. The positive gap and explicit error target are introduced only for the finite-data problem.
- **Unconditional outcomes versus postselection.** The model uses one unconditional binary effect on every block. Conditional ratios with success/failure records require a separate accounting of retained outcomes and consumed copies.

The general distinction between measuring few invariants and using few samples is already discussed in [Leifer, Linden, and Winter (2004), Section VII](https://arxiv.org/pdf/quant-ph/0308008). The present theorem specifies a uniform minimax rate for the exact universal binary class. The primary-source comparisons and bibliography are collected in [RELATED_WORK.md](../references/RELATED_WORK.md).
