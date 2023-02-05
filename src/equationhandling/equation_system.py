from typing import List

from .equation_variable import CalculatedVariable, AssignedVariable
from .equation_variables_collection import VariablesCollection
from ..equationhandling.equation import Equation


class EquationSystem:
    def __init__(self):
        self._all_variables = VariablesCollection()
        self._equations = []

    def add_new_equation(self):
        self._equations.append(Equation(self._all_variables))

    def get_equations(self):
        return self._equations

    def add_term_to_last_equation(self, term_to_add: str):
        self._equations[-1].add_term(term_to_add)

    def add_calculated_variable(self, variable_to_add: str):
        if not self._all_variables.has_variable(variable_to_add):
            new_var = CalculatedVariable(variable_to_add)
            self._all_variables.add_variable(new_var)

    def get_equation_evaluations(self) -> List[float]:
        all_equation_evaluations = []
        for equation in self._equations:
            all_equation_evaluations.append(
                equation.evaluate_equation_expression()
            )
        return all_equation_evaluations

    def calculated_variables(self) -> List[CalculatedVariable]:
        return self._all_variables.calculated_variables()

    def add_assigned_variable(self, variable_to_add: str, value: float):
        new_var = AssignedVariable(variable_to_add)
        new_var.value = value
        self._all_variables.add_variable(new_var)

    def has_variable(self, var_name: str):
        return self._all_variables.has_variable(var_name)

    def no_structural_errors(self):
        return (
            len(self.calculated_variables()) == len(self._equations)
            and len(self._equations) > 0
        )

    def initialize_calculated_variables(self):
        for var in self._all_variables.calculated_variables():
            var.value = var.initial_value

    def set_variable_initial_value(self, var_name: str, value: float):
        for var in self._all_variables.calculated_variables():
            if var.name == var_name:
                var.initial_value = value

    def set_variable_value(self, var_name: str, value: float):
        for var in self._all_variables.calculated_variables():
            if var.name == var_name:
                var.value = value
