class NonLinearSolverSpecifications:
    default_jacobian_perturbation = 0.001
    default_max_iterations = 50
    default_convergence_tolerance = 1e-5

    def __init__(self):
        self._jacobian_perturbation = (
            NonLinearSolverSpecifications.default_jacobian_perturbation
        )
        self._max_iterations = (
            NonLinearSolverSpecifications.default_max_iterations
        )
        self._convergence_tolerance = (
            NonLinearSolverSpecifications.default_convergence_tolerance
        )

    @property
    def jacobian_perturbation(self):
        return self._jacobian_perturbation

    @jacobian_perturbation.setter
    def jacobian_perturbation(self, value: float):
        self._jacobian_perturbation = value

    @property
    def max_iterations(self):
        return self._max_iterations

    @max_iterations.setter
    def max_iterations(self, value: float):
        self._max_iterations = value

    @property
    def convergence_tolerance(self):
        return self._convergence_tolerance

    @convergence_tolerance.setter
    def convergence_tolerance(self, value: float):
        self._convergence_tolerance = value
