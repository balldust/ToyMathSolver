from unittest import TestCase

from src.equationhandling.equation_system import EquationSystem
from src.solvers.nl_solver import NonLinearEquationSolver
from src.solvers.nl_solver_specification import NonLinearSolverSpecifications


class Test(TestCase):
    def test_solve(self):
        equation_system = EquationSystem()
        equation_system.add_new_equation()
        variable = "x1"
        equation_system.add_calculated_variable(variable)
        equation_system.add_term_to_last_equation("-")
        equation_system.add_term_to_last_equation("^")
        equation_system.add_term_to_last_equation(variable)
        equation_system.add_term_to_last_equation("2")
        equation_system.add_term_to_last_equation("4")
        nl_solver = NonLinearEquationSolver(equation_system, NonLinearSolverSpecifications())

        nl_solver.solve()

        expected_value = 2.0
        obtained_value = equation_system.calculated_variables()[0].value
        self.assertAlmostEqual(expected_value, obtained_value, places=3)
