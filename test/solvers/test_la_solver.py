from unittest import TestCase

from parameterized import parameterized

import src.solvers.la_solver as la


class TestLinearEquationSolver(TestCase):
    initial_matrix_random = [[1, 2, 3, 14], [1, 1, -1, 0], [2, 1, -1, 1]]
    initial_matrix_in_required_form = [
        [4, 1, -1, 3],
        [0, -5, 5, 5],
        [0, 0, 10, 30],
    ]
    initial_matrices = [
        [initial_matrix_random],
        [initial_matrix_in_required_form],
    ]

    @parameterized.expand(initial_matrices)
    def test_solve_linear_system(self, initial_matrix):
        la_solver = la.LinearEquationSolver(initial_matrix)

        obtained_vars = la_solver.solve_linear_system()

        expected_vars = [1, 2, 3]
        for o, e in zip(obtained_vars, expected_vars):
            self.assertAlmostEqual(o, e, places=5)
