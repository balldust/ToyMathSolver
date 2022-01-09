import math

from .nl_solver_specification import NonLinearSolverSpecifications
from ..equationhandling.equation_system import EquationSystem
from ..solvers.la_solver import LinearEquationSolver


class NonLinearEquationSolver:
    def __init__(self, equation_system: EquationSystem, nl_solver_specs: NonLinearSolverSpecifications):
        self._equation_system = equation_system
        self._max_niter = nl_solver_specs.max_iterations
        self._jacobian_perturbation = nl_solver_specs.jacobian_perturbation
        self._convergence_tolerance = nl_solver_specs.convergence_tolerance
        self._jacobian = self._construct_jacobian()

    def solve(self) -> bool:
        return self._solve_newton_raphson()

    def _solve_newton_raphson(self) -> bool:
        la_solver = LinearEquationSolver(self._jacobian)
        niter = 0
        while max([math.fabs(res) for res in self._equation_system.get_equation_evaluations()]) > self._convergence_tolerance:
            niter += 1
            self._update_jacobian()
            updated_variable_values = la_solver.solve_linear_system()
            self._update_variable_values(updated_variable_values)
            if niter > self._max_niter:
                return False
        return True

    def _construct_jacobian(self):
        n_vars = len(self._equation_system.calculated_variables())
        n_equations = len(self._equation_system.get_equations())
        jacobian = [[0 for i in range(n_vars+1)] for j in range(n_equations)]
        return jacobian

    def _update_jacobian(self):
        for row, eq in enumerate(self._equation_system.get_equations()):
            value_before_pertubation = eq.evaluate_equation_expression()
            self._jacobian[row][-1] = value_before_pertubation
            for col, var in enumerate(self._equation_system.calculated_variables()):
                var.value = var.value + self._jacobian_perturbation
                value_after_pertubation = eq.evaluate_equation_expression()
                var.value = var.value - self._jacobian_perturbation
                self._jacobian[row][col] = 1/self._jacobian_perturbation * (value_after_pertubation
                                                                            - value_before_pertubation)

    def _update_variable_values(self, calculated_step):
        for count, var in enumerate(self._equation_system.calculated_variables()):
            var.value = var.value - calculated_step[count]
