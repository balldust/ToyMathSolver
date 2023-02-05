from typing import Set, List

from src.equationhandling.equation_variable import (
    EquationVariable,
    CalculatedVariable,
    AssignedVariable,
)


class VariablesCollection:
    def __init__(self):
        self._variables = set()

    def add_variable(self, var: EquationVariable):
        if issubclass(var.__class__, EquationVariable):
            self._remove_calculated_variable_to_replace_with_assigned(var)
            self._variables.add(var)
        else:
            raise Exception(
                "Illegal operation: Cannot add object that"
                + " is not an EquationVariable"
            )

    def _remove_calculated_variable_to_replace_with_assigned(
        self, var: EquationVariable
    ):
        if isinstance(var, AssignedVariable) and var in self._variables:
            self._variables.remove(var)

    def has_variable(self, name: str) -> bool:
        for var in self._variables:
            if var.name.lower() == name.lower():
                return True
        return False

    def get_variable_value(self, name: str) -> float:
        for var in self._variables:
            if var.name.lower() == name.lower():
                return var.value

    def calculated_variables(self) -> List[CalculatedVariable]:
        calculated_vars = []
        for var in self._variables:
            if isinstance(var, CalculatedVariable):
                calculated_vars.append(var)
        return calculated_vars

    @property
    def variables(self) -> Set[EquationVariable]:
        return self._variables
