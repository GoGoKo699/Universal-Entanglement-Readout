"""Exact checks of the fixed six-copy observable formulas.

The script contracts the antisymmetric permutation sums and compares their
expectations with independent principal-minor and adjugate calculations.
Universal operator-norm bounds are proved in science/collective_measurements.md.
Only the Python standard library is required.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial
import json


Q = Fraction
DIM = 6


def identity(size=DIM):
    return [[Q(i == j) for j in range(size)] for i in range(size)]


def scale(matrix, scalar):
    return [[scalar * entry for entry in row] for row in matrix]


def combine(*matrices):
    return [[sum(matrix[i][j] for matrix in matrices)
             for j in range(DIM)] for i in range(DIM)]


def multiply(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(len(right)))
             for j in range(len(right[0]))] for i in range(len(left))]


def trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))


def determinant(matrix):
    """Rational Gaussian elimination, independent of the permutation sums."""
    work = [[Q(entry) for entry in row] for row in matrix]
    size = len(work)
    value = Q(1)
    for column in range(size):
        pivot_row = next((row for row in range(column, size)
                          if work[row][column]), None)
        if pivot_row is None:
            return Q(0)
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            value = -value
        pivot = work[column][column]
        value *= pivot
        for row in range(column + 1, size):
            multiplier = work[row][column] / pivot
            for entry in range(column + 1, size):
                work[row][entry] -= multiplier * work[column][entry]
    return value


def principal_coefficient(matrix, order):
    return sum(determinant([[matrix[i][j] for j in subset] for i in subset])
               for subset in combinations(range(len(matrix)), order))


def trace_adjugate_product(direction, matrix):
    """Tr[D adj(H)] as a sum of entries times signed minors."""
    value = Q(0)
    for i in range(DIM):
        for j in range(DIM):
            if direction[i][j]:
                minor = [[matrix[row][column]
                          for column in range(DIM) if column != j]
                         for row in range(DIM) if row != i]
                value += direction[i][j] * (-1) ** (i + j) * determinant(minor)
    return value


def determinant_directional_derivative(direction, matrix):
    """Derivative from multilinearity in columns, without an adjugate."""
    value = Q(0)
    for column in range(DIM):
        replacement = [[direction[i][j] if j == column else matrix[i][j]
                        for j in range(DIM)] for i in range(DIM)]
        value += determinant(replacement)
    return value


def marginal_and_reduction(rho):
    marginal = [[rho[b][c] + rho[b + 3][c + 3] for c in range(3)]
                for b in range(3)]
    direction = [[marginal[i % 3][j % 3] if i // 3 == j // 3 else Q(0)
                  for j in range(DIM)] for i in range(DIM)]
    reduced = combine(direction, scale(rho, -1))
    return marginal, direction, reduced


@lru_cache(maxsize=None)
def permutation_cycles(order):
    data = []
    for permutation in permutations(range(order)):
        seen = set()
        cycles = []
        for start in range(order):
            if start in seen:
                continue
            cycle = []
            index = start
            while index not in seen:
                seen.add(index)
                cycle.append(index)
                index = permutation[index]
            cycles.append(tuple(cycle))
        sign = (-1) ** (order - len(cycles))
        data.append((sign, tuple(cycles)))
    return tuple(data)


def powers_and_traces(matrix, maximum):
    powers = [identity()]
    for _ in range(maximum):
        powers.append(multiply(powers[-1], matrix))
    return powers, [trace(power) for power in powers]


def antisymmetric_equal_expectation(power_traces, order):
    total = Q(0)
    for sign, cycles in permutation_cycles(order):
        term = Q(sign)
        for cycle in cycles:
            term *= power_traces[len(cycle)]
        total += term
    return total / factorial(order)


def weighted_adjugate_expectation(power_traces, mixed_traces):
    """The six summands in W_g contracted separately by permutation cycles."""
    total = Q(0)
    single_slot = Q(0)
    for sign, cycles in permutation_cycles(6):
        for chosen_index, chosen_cycle in enumerate(cycles):
            term = Q(sign) * mixed_traces[len(chosen_cycle) - 1]
            for other_index, other_cycle in enumerate(cycles):
                if other_index != chosen_index:
                    term *= power_traces[len(other_cycle)]
            # Any slot in this cycle can carry D. Its trace is Tr[D H^(l-1)].
            total += len(chosen_cycle) * term
            if 0 in chosen_cycle:
                single_slot += term
    total /= factorial(6)
    single_slot /= factorial(6)
    assert total == 6 * single_slot
    return total


def check_linear_maps():
    """Exact matrix-unit certificates for T and R on the full one-copy space."""
    size = DIM * DIM
    transfer = [[0] * size for _ in range(size)]
    for row in range(DIM):
        for column in range(DIM):
            source = DIM * row + column
            if row // 3 == column // 3:
                for qubit in range(2):
                    out_row = 3 * qubit + row % 3
                    out_column = 3 * qubit + column % 3
                    transfer[DIM * out_row + out_column][source] += 1
    reduction = [[transfer[i][j] - int(i == j) for j in range(size)]
                 for i in range(size)]
    assert all(transfer[i][j] == transfer[j][i]
               and reduction[i][j] == reduction[j][i]
               for i in range(size) for j in range(size))
    # R is a signed permutation in the matrix-unit basis, so it is an HS isometry.
    assert all(sum(entry != 0 for entry in row) == 1 for row in reduction)
    assert all(sum(reduction[row][column] != 0 for row in range(size)) == 1
               for column in range(size))
    assert all(entry in (-1, 0, 1) for row in reduction for entry in row)

    # Compare to J X^Gamma J^T, J=[[0,-1],[1,0]] on the qubit.
    for row in range(DIM):
        for column in range(DIM):
            a, b = divmod(row, 3)
            c, d = divmod(column, 3)
            out_row = 3 * (1 - c) + b
            out_column = 3 * (1 - a) + d
            sign = (1 if c == 0 else -1) * (1 if a == 0 else -1)
            source = DIM * row + column
            assert reduction[DIM * out_row + out_column][source] == sign

    diagonal_vector = [int(i // DIM == i % DIM) for i in range(size)]
    image_t = [sum(transfer[i][j] * diagonal_vector[j] for j in range(size))
               for i in range(size)]
    image_r = [sum(reduction[i][j] * diagonal_vector[j] for j in range(size))
               for i in range(size)]
    assert image_t == [2 * value for value in diagonal_vector]
    assert image_r == diagonal_vector
    return {"matrix_units_checked": size,
            "self_adjoint_maps": True,
            "reduction_is_hilbert_schmidt_isometry": True,
            "qubit_partial_transpose_identity": True,
            "unnormalized_trace_convention": "T(I)=2I; R(I)=I"}


def outer(vector):
    return [[Q(left) * Q(right) for right in vector] for left in vector]


def example_states():
    bell = scale(outer([1, 0, 0, 0, 1, 0]), Q(1, 2))
    seed_integer = [
        [6, 2, 4, 2, 8, 8],
        [2, 8, 8, 4, 8, 20],
        [4, 8, 20, 8, 16, 32],
        [2, 4, 8, 8, 8, 16],
        [8, 8, 16, 8, 20, 32],
        [8, 20, 32, 16, 32, 68],
    ]
    seed = scale(seed_integer, Q(1, 130))
    mixed = scale(identity(), Q(1, 6))
    equal_case = scale(combine(scale(bell, 2), outer([0, 1, 0, 0, 0, 1])), Q(1, 4))
    rank_five = combine(scale(bell, Q(1, 2)),
                        scale(outer([0, 0, 1, 0, 0, 0]), Q(1, 2)))
    return [
        ("maximally_mixed", mixed),
        ("embedded_bell", bell),
        ("rank_five_npt", rank_five),
        ("two_negative_g_zero", equal_case),
        ("rank_four_pt_seed", seed),
        ("noncommuting_full_rank_ppt", combine(scale(seed, Q(99, 100)),
                                                scale(mixed, Q(1, 100)))),
    ]


def check():
    map_certificate = check_linear_maps()
    antisymmetrizer_traces = {}
    for order, expected_rank in [(4, 15), (6, 1)]:
        value = Q(sum(sign * DIM ** len(cycles)
                      for sign, cycles in permutation_cycles(order)), factorial(order))
        assert value == expected_rank
        antisymmetrizer_traces[str(order)] = int(value)

    cases = []
    noncommuting_checked = False
    for name, rho in example_states():
        assert trace(rho) == 1
        _, direction, reduced = marginal_and_reduction(rho)
        powers, power_traces = powers_and_traces(reduced, 6)
        mixed_traces = [trace(multiply(direction, powers[index])) for index in range(6)]

        f_collective = antisymmetric_equal_expectation(power_traces, 6)
        g_collective = weighted_adjugate_expectation(power_traces, mixed_traces)
        h_collective = antisymmetric_equal_expectation(power_traces, 4)

        f_minors = determinant(reduced)
        g_minors = trace_adjugate_product(direction, reduced)
        h_minors = principal_coefficient(reduced, 4)
        assert (f_collective, g_collective, h_collective) == (f_minors, g_minors, h_minors)
        assert g_collective == determinant_directional_derivative(direction, reduced)

        # The subset average has 15 placements, each padded by (Tr rho)^2=1.
        assert len(tuple(combinations(range(6), 4))) == 15
        assert Q(15, 15) * h_collective * trace(rho) ** 2 == h_minors

        commutes = multiply(direction, reduced) == multiply(reduced, direction)
        if name == "noncommuting_full_rank_ppt":
            assert not commutes and f_collective > 0 and g_collective > 0
            noncommuting_checked = True
        if name == "two_negative_g_zero":
            assert (f_collective, g_collective, h_collective) == (Q(1, 4096), 0, Q(-1, 64))

        probabilities = [Q(1, 4) + value / 80
                         for value in (f_collective, g_collective, h_collective)]
        probabilities.append(1 - sum(probabilities))
        assert all(0 < value < 1 for value in probabilities)
        cases.append({"name": name,
                      "f": str(f_collective),
                      "g": str(g_collective),
                      "h": str(h_collective),
                      "D_and_H_commute": commutes,
                      "collective_contractions_equal_minor_formulas": True})
    assert noncommuting_checked

    # Conservative analytic bounds: 1,12,sqrt(15), with sqrt(15)<4.
    assert 15 < 4 ** 2
    norm_bounds = [Q(1), Q(12), Q(4)]
    four_bounds = [Q(1, 4) - bound / 80 for bound in norm_bounds]
    four_bounds.append(Q(1, 4) - sum(norm_bounds) / 80)
    assert four_bounds == [Q(19, 80), Q(1, 10), Q(1, 5), Q(3, 80)]
    three_bounds = [Q(1, 3) - Q(1, 48),
                    Q(1, 3) - Q(12, 48),
                    Q(1, 3) - Q(13, 48)]
    assert three_bounds == [Q(5, 16), Q(1, 12), Q(1, 16)]
    assert all(bound > 0 for bound in four_bounds + three_bounds)

    return {"all_checks_passed": True,
            "arithmetic": "Exact fractions and integer permutation cycles; standard library only.",
            "linear_map_certificate": map_certificate,
            "antisymmetrizer_traces": antisymmetrizer_traces,
            "polarization_derivative_factor": 6,
            "four_copy_subset_average_terms": 15,
            "norm_certificate_scope": "Analytic proofs in science/collective_measurements.md; no test-state positivity inference.",
            "four_outcome_scale": "1/80",
            "four_effect_lower_bounds": [str(bound) for bound in four_bounds],
            "three_outcome_scale": "1/48",
            "three_effect_lower_bounds": [str(bound) for bound in three_bounds],
            "cases": cases}


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
