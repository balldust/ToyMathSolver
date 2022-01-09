from typing import Any

from src.execution.problem_execution import ProblemExecution
from src.solvers.nl_solver_specification import NonLinearSolverSpecifications
from src.userinterface.tree.tree_structure import TreeNode, TreeItem
from src.util.converters import IntegerValueConverter, FloatValueConverter
from src.util.factories.property_factory import PropertyFactory, NonSettablePropertyFactory


class SettingsViewController:
    def __init__(self, model: ProblemExecution):
        self._model = model

    def get_settings_specifications(self) -> TreeNode:
        root = TreeNode(TreeItem('Name', NonSettablePropertyFactory('Value')))
        self._add_non_linear_solver_specifications(root, 0)
        return root

    def _add_non_linear_solver_specifications(self, root: TreeNode, child: int):
        root.append_child(TreeItem('Non linear solver', None))
        solver_specs_factory = SolverSpecsFactory(self._model.nl_solver_specs)
        root.child(child).append_child(TreeItem(solver_specs_factory.JACOBIAN_PERTURBATION,
                                                             solver_specs_factory))
        root.child(child).append_child(TreeItem(solver_specs_factory.MAXIMUM_ITERATIONS,
                                                             solver_specs_factory))
        root.child(child).append_child(TreeItem(solver_specs_factory.CONVERGENCE_TOLERANCE,
                                                             solver_specs_factory))


class SolverSpecsFactory(PropertyFactory):
    MAXIMUM_ITERATIONS = 'Maximum iterations'
    CONVERGENCE_TOLERANCE = 'Convergence tolerance'
    JACOBIAN_PERTURBATION = 'Jacobian perturbation'

    def __init__(self, solver_specs: NonLinearSolverSpecifications):
        self._solver_specs = solver_specs
        self._property_names = {self.MAXIMUM_ITERATIONS, self.CONVERGENCE_TOLERANCE, self.JACOBIAN_PERTURBATION}

    def named_property(self, name: str) -> Any:
        if name in self._property_names:
            if name == self.JACOBIAN_PERTURBATION:
                return self._solver_specs.jacobian_perturbation
            elif name == self.CONVERGENCE_TOLERANCE:
                return self._solver_specs.convergence_tolerance
            elif name == self.MAXIMUM_ITERATIONS:
                return self._solver_specs.max_iterations
            else:
                return None

    def named_property_setter(self, name: str, value: Any) -> bool:
        if name in self._property_names:
            if name == self.JACOBIAN_PERTURBATION:
                converter = FloatValueConverter()
                converted_value = converter.convert(value)
                self._solver_specs.jacobian_perturbation = converted_value
                return True
            elif name == self.CONVERGENCE_TOLERANCE:
                converter = FloatValueConverter()
                converted_value = converter.convert(value)
                self._solver_specs.convergence_tolerance = converted_value
                return True
            elif name == self.MAXIMUM_ITERATIONS:
                converter = IntegerValueConverter()
                converted_value = converter.convert(value)
                self._solver_specs.max_iterations = converted_value
                return True
            else:
                return False
        return False


