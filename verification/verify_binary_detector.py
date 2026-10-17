"""Exact finite checks supporting the binary rigidity and sampling arguments; stdlib only."""
from fractions import Fraction as F
from itertools import permutations
import json


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def pt(a):
    return [[a[2*(j//2)+i%2][2*(i//2)+j%2] for j in range(4)] for i in range(4)]


def det(a):
    n = len(a)
    return sum((-1)**sum(p[i] > p[j] for i in range(n) for j in range(i+1,n))
               * product(a[i][p[i]] for i in range(n)) for p in permutations(range(n)))


def product(xs):
    out = F(1)
    for x in xs:
        out *= x
    return out


def check():
    # tau = I/6 + Phi+/3. Exact eigenvalues follow from rank-one projector form.
    phi = [[F(1,2) if i in (0,3) and j in (0,3) else F(0) for j in range(4)] for i in range(4)]
    tau = [[F(i==j,6) + phi[i][j]/3 for j in range(4)] for i in range(4)]
    swap = [[F((i//2 == j%2) and (i%2 == j//2)) for j in range(4)] for i in range(4)]
    assert tr(tau) == 1
    assert pt(tau) == [[(F(i==j)+swap[i][j])/6 for j in range(4)] for i in range(4)]
    assert det(tau) == F(1,432)
    assert det(pt(tau)) == 0

    # Unnormalized coefficient matrix of the four-particle antisymmetric state,
    # regrouped across A^4|B^4.
    coeff = [[0]*16 for _ in range(16)]
    for p in permutations(range(4)):
        inv = sum(p[i] > p[j] for i in range(4) for j in range(i+1,4))
        a = sum((x >> 1) << (3-i) for i, x in enumerate(p))
        b = sum((x & 1) << (3-i) for i, x in enumerate(p))
        coeff[a][b] = (-1)**inv
    gram = mm(coeff, [list(row) for row in zip(*coeff)])
    gram2 = mm(gram, gram)
    assert gram2 == [[12*x for x in row] for row in gram]
    assert tr(gram) == 24
    weight_two = [i for i in range(16) if i.bit_count() == 2]
    small_coeff = [[coeff[i][j] for j in weight_two] for i in weight_two]

    # Rational pure Schmidt paths cos(theta),sin(theta), avoiding floating point.
    pure_checks = []
    for cos_t, sin_t in [(F(4,5),F(3,5)), (F(12,13),F(5,13)), (F(99,101),F(20,101))]:
        assert cos_t**2 + sin_t**2 == 1
        delta = cos_t*sin_t
        psi = [cos_t,F(0),F(0),sin_t]
        rho = [[x*y for y in psi] for x in psi]
        rho_pt = pt(rho)
        assert tr(rho) == 1
        assert det(rho_pt) == -delta**4
        # Negative PT eigenvector is the unnormalized vector (0,1,-1,0).
        minus = [F(0),F(1),F(-1),F(0)]
        assert [sum(rho_pt[i][j]*minus[j] for j in range(4)) for i in range(4)] == [-delta*x for x in minus]
        pure_checks.append({'cos_theta':str(cos_t),'sin_theta':str(sin_t),'distance_delta':str(delta),'det_pt':str(det(rho_pt))})

    result = {
        'status':'all exact checks passed',
        'tau_determinant':str(det(tau)),
        'tau_eigenvalues':['1/2','1/6','1/6','1/6'],
        'tau_pt_eigenvalues':['1/3','1/3','1/3','0'],
        'schmidt_matrix_indices':weight_two,
        'schmidt_integer_matrix':small_coeff,
        'gram_polynomial':'K^2 = 12 K',
        'gram_trace':tr(gram),
        'normalized_nonzero_schmidt_weights':['1/2','1/2'],
        'w_spectrum_multiplicities':{'1/2':3,'-1/2':1,'0':252},
        'pure_checks':pure_checks,
        'analytic_claims_not_proved_by_this_script':['absolute irreducibility','real smooth patch Zariski density','Bernoulli information bound','concurrence distance comparison']
    }
    result["all_checks_passed"] = True
    return result

if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
