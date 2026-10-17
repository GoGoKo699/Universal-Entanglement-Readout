"""Exact rational checks of the promise-gap polynomial construction.

These checks complement the analytic inequalities in science/promise_gap.md.
They do not numerically purport to prove the asymptotic threshold-degree bound.
"""
from fractions import Fraction as Q
from itertools import combinations, product
import json


def det(matrix):
    a = [[Q(x) for x in row] for row in matrix]
    n = len(a)
    out = Q(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[pivot], a[j] = a[j], a[pivot]
            out = -out
        p = a[j][j]
        out *= p
        for i in range(j + 1, n):
            ratio = a[i][j] / p
            for c in range(j + 1, n):
                a[i][c] -= ratio * a[j][c]
    return out


def pt(a):
    return [[a[(c // 3) * 3 + r % 3][(r // 3) * 3 + c % 3]
             for c in range(6)] for r in range(6)]


def elementary(a, degree):
    return sum((det([[a[i][j] for j in subset] for i in subset])
                for subset in combinations(range(len(a)), degree)), Q(0))


def nodes(epsilon):
    assert 0 < epsilon <= 1
    result = [epsilon]
    while result[-1] < 1:
        result.append(2 * result[-1])
    return result


def rational_filter(x, node_list):
    positive, negative = Q(1), Q(1)
    for a in node_list:
        positive *= (x + a) ** 2
        negative *= (x - a) ** 2
    assert positive + negative > 0
    value = (positive - negative) / (positive + negative)
    assert -1 <= value <= 1
    return value


def check():
    filter_checks = []
    for exponent in (3, 8, 16, 32):
        eps = Q(1, 2 ** exponent)
        grid = nodes(eps)
        xs = sorted(set([Q(0), eps / 2, eps, Q(1)] +
                        [min(Q(1), a * Q(3, 2)) for a in grid] + grid))
        for x in xs:
            value = rational_filter(x, grid)
            assert rational_filter(-x, grid) == -value
            if eps <= x <= 1:
                assert value >= Q(4, 5)
        filter_checks.append({"epsilon": str(eps), "nodes": len(grid),
                              "nonnegative_points_checked": len(xs),
                              "oddness_boundedness_and_gap_inequalities": True})

    # Check the four-way conjunction at boundary, transition, and saturation points.
    eps = Q(1, 256)
    grid = nodes(eps)
    possible_xs = [-Q(1), -eps, -eps / 2, Q(0), eps / 2, eps, Q(1)]
    values = {x: rational_filter(x, grid) for x in possible_xs}
    and_count = 0
    for xs in product(possible_xs, repeat=4):
        score = sum(values[x] for x in xs) - 3
        if all(x >= eps for x in xs):
            assert score >= Q(1, 5)
        if any(x <= -eps for x in xs):
            assert score <= -Q(4, 5)
        and_count += 1

    from verify_corner import check as check_corner
    old = check_corner()
    R = [[Q(x) for x in row] for row in old["R"]]
    X = pt(R)
    u = [0, 1, 0, -1, 0, 0]
    v = [0, 0, 1, 0, -1, 0]
    pu = [[Q(u[i] * u[j], 2) for j in range(6)] for i in range(6)]
    pv = [[Q(v[i] * v[j], 2) for j in range(6)] for i in range(6)]
    r = Q(1, 10000)
    cases = []
    for s, t in [(0, 0), (r, r), (0, r), (-r, r), (-r, 0), (-r, -r), (r, -r)]:
        H = [[(1 - s - t) * X[i][j] / 130 + s * pu[i][j] + t * pv[i][j]
              for j in range(6)] for i in range(6)]
        cases.append((f"corner({s},{t})", H, s >= 0 and t >= 0, r))

    bell = [[Q(0) for j in range(6)] for i in range(6)]
    for i in (0, 4):
        for j in (0, 4):
            bell[i][j] = Q(1, 2)
    cases.append(("embedded_bell", pt(bell), False, Q(1, 2)))
    identity = [[Q(int(i == j), 6) for j in range(6)] for i in range(6)]
    cases.append(("maximally_mixed", identity, True, r))

    case_checks = []
    for name, H, separable, delta in cases:
        es = [elementary(H, j) for j in range(1, 7)]
        assert es[0] == 1 and es[1] >= 0
        assert (all(e >= 0 for e in es)) == separable
        gamma = delta ** 6 / (4 * 6 ** 6 * 64)
        epsilon = gamma / 2
        node_list = nodes(epsilon)
        xs = [e / 64 + gamma / 2 for e in es[2:]]
        assert all(-1 <= x <= 1 for x in xs)
        if not separable:
            assert min(es[2:]) <= -(delta ** 6) / (4 * 6 ** 6)
            assert min(xs) <= -epsilon
        else:
            assert min(xs) >= epsilon
        score = sum(rational_filter(x, node_list) for x in xs) - 3
        assert (score > 0) == separable
        case_checks.append({"case": name, "separable": separable,
                            "e3_e4_e5_e6": [str(e) for e in es[2:]],
                            "positive_rational_score": score > 0,
                            "polynomial_degree_upper_bound": 36 * len(node_list)})

    result = {"method": "stdlib exact fractions; no numerical tolerances",
              "filter_checks": filter_checks, "conjunction_grid_points": and_count,
              "state_cases": case_checks, "all_checks_passed": True,
              "proof_dependency": "Analytic inequalities and imported Sherstov threshold-degree theorem, not finite checks, establish the asymptotic result."}
    return result

if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
