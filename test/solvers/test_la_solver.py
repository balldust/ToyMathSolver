from unittest import TestCase
import src.solvers.la_solver as la


class TestLinearEquationSolver(TestCase):
    def test_solve_linear_system(self):
        initial_matrix = [[1, 2, 3, 14], [1, 1, -1, 0], [2, 1, -1, 1]]
        la_solver = la.LinearEquationSolver(initial_matrix)

        obtained_vars = la_solver.solve_linear_system()

        expected_vars = [1, 2, 3]
        for o, e in zip(obtained_vars, expected_vars):
            self.assertAlmostEqual(o, e, places=5)

    def test_solve_linear_system_given_no_required_manipulation(self):
        initial_matrix = [[4, 1, -1, 3], [0, -5, 5, 5], [0, 0, 10, 30]]
        la_solver = la.LinearEquationSolver(initial_matrix)

        obtained_vars = la_solver.solve_linear_system()

        expected_vars = [1, 2, 3]
        for o, e in zip(obtained_vars, expected_vars):
            self.assertAlmostEqual(o, e, places=5)
