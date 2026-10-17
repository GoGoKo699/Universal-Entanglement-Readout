"""Exact representative checks of the three-statistic 2x3 criterion.

This is a scientific verification script, not a substitute for the analytic proof.
All listed cases use exact rational arithmetic; no eigenvalue tolerance is used.
"""
from fractions import Fraction as Q
from itertools import combinations
import json

N = 6


def zeros(n=N):
    return [[Q(0) for _ in range(n)] for _ in range(n)]


def det(matrix):
    a = [[Q(x) for x in row] for row in matrix]
    n = len(a)
    ans = Q(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            ans = -ans
        val = a[j][j]
        ans *= val
        for i in range(j + 1, n):
            coeff = a[i][j] / val
            for k in range(j + 1, n):
                a[i][k] -= coeff * a[j][k]
    return ans


def add(*matrices):
    return [[sum(a[i][j] for a in matrices) for j in range(N)] for i in range(N)]


def scale(a, value):
    return [[value*x for x in row] for row in a]


def diagonal(values):
    return [[Q(values[i]) if i == j else Q(0) for j in range(N)] for i in range(N)]


def outer(v):
    return [[Q(v[i])*Q(v[j]) for j in range(N)] for i in range(N)]


def pt(a):
    return [[a[(j//3)*3+i%3][(i//3)*3+j%3] for j in range(N)] for i in range(N)]


def fourth_coefficient(a):
    return sum(det([[a[i][j] for j in inds] for i in inds])
               for inds in combinations(range(N), 4))


def stats(rho):
    assert sum(rho[i][i] for i in range(N)) == 1
    b = [[rho[i][j] + rho[i+3][j+3] for j in range(3)] for i in range(3)]
    d = [[b[i % 3][j % 3] if i//3 == j//3 else Q(0)
          for j in range(N)] for i in range(N)]
    hmat = add(d, scale(rho, -1))
    # Exact qubit reduction identity using J=[[0,-1],[1,0]].
    gamma = pt(rho)
    expected_h = [[((-1) if i//3 == 0 else 1)
                   * ((-1) if j//3 == 0 else 1)
                   * gamma[(1-i//3)*3+i%3][(1-j//3)*3+j%3]
                   for j in range(N)] for i in range(N)]
    assert expected_h == hmat
    f = det(hmat)
    # Tr[D adj(H)] = sum_ij D_ij cofactor(H)_ij.
    g = Q(0)
    for i in range(N):
        for j in range(N):
            if d[i][j]:
                minor = [[hmat[r][c] for c in range(N) if c != j]
                         for r in range(N) if r != i]
                g += d[i][j] * (-1)**(i+j) * det(minor)
    h = fourth_coefficient(hmat)
    assert f == det(gamma) and h == fourth_coefficient(gamma)
    sep = (f > 0 and g > 0) or (f == 0 and (g > 0 or (g == 0 and h >= 0)))
    return f, g, h, sep, det(b)


def check():
    bell = scale(outer([1, 0, 0, 0, 1, 0]), Q(1, 2))
    phi2 = outer([0, 1, 0, 0, 0, 1])
    mixed = diagonal([Q(1, 6)]*N)
    rank2_npt = scale(add(scale(bell, 2), phi2), Q(1, 4))
    R = [[6, 2, 4, 2, 8, 8],
         [2, 8, 8, 4, 8, 20],
         [4, 8, 20, 8, 16, 32],
         [2, 4, 8, 8, 8, 16],
         [8, 8, 16, 8, 20, 32],
         [8, 20, 32, 16, 32, 68]]
    rho0 = scale(R, Q(1, 130))
    Pu = scale(outer([0, 1, 0, -1, 0, 0]), Q(1, 2))
    Pv = scale(outer([0, 0, 1, 0, -1, 0]), Q(1, 2))

    cases = [
        ("maximally_mixed", mixed, True),
        ("embedded_bell", bell, False),
        ("embedded_two_qubit_maximally_mixed", diagonal([Q(1,4),Q(1,4),0,Q(1,4),Q(1,4),0]), True),
        ("rank_five_npt_full_marginal", add(scale(bell, Q(1,2)), diagonal([0,0,Q(1,2),0,0,0])), False),
        ("rank_five_ppt_full_marginal", diagonal([0]+[Q(1,5)]*5), True),
        ("two_negative_g_exactly_zero", rank2_npt, False),
        ("full_state_rank_pt_rank_four_ppt", rho0, True),
        ("full_rank_one_negative", scale(add(bell, mixed), Q(1,2)), False),
        ("full_rank_two_negative", add(scale(rank2_npt, Q(99,100)), scale(mixed, Q(1,100))), False),
        ("pure_product", diagonal([1,0,0,0,0,0]), True),
    ]

    radius = Q(1,10000)
    for s in [-radius, 0, radius]:
        for t in [-radius, 0, radius]:
            corner = add(scale(rho0, 1-s-t), scale(pt(Pu),s), scale(pt(Pv),t))
            cases.append(("corner_s_{}_t_{}".format(s,t), corner, s>=0 and t>=0))

    results = []
    for name, rho, expected_sep in cases:
        f, g, h, sep, marginal_det = stats(rho)
        assert sep == expected_sep, (name, f, g, h, sep, expected_sep)
        if marginal_det > 0:
            promised_sep = (f > 0 and g > 0) or (f == 0 and g >= 0)
            assert promised_sep == expected_sep
        results.append({"name": name, "f": str(f), "g": str(g), "h": str(h),
                        "separable": sep, "marginal_det": str(marginal_det)})

    edge = next(item for item in results if item["name"] == "two_negative_g_exactly_zero")
    assert edge["f"] == "1/4096" and edge["g"] == "0" and edge["h"] == "-1/64"

    out = {"method": "Exact rational determinants, cofactors, matrix identities and decision rules.",
           "all_checks_passed": True, "cases": results}
    return out

if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
