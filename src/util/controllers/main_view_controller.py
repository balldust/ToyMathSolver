from typing import List

from src.equationhandling.equation_variable import CalculatedVariable
from src.equationinterpreter.error_handling.syntax_error import (
    EquationSyntaxError,
)
from src.execution.problem_execution import ProblemExecution
from src.util.listeners.error_listeners import SyntaxErrorListener
from src.util.listeners.text_listeners import TextListener
from src.util.listeners.variable_listeners import CalculatedVariableObserver


class MainViewController(TextListener):
    def __init__(self, model: ProblemExecution):
        self._model = model
        self._error_listeners: List[SyntaxErrorListener] = []
        self._calculated_variable_listeners: List[
            CalculatedVariableObserver
        ] = []

    def handle_text(self, text: str):
        self._model.set_text(text)
        system_constructed = self._model.construct_system()
        if system_constructed:
            calculated_vars = self._model.get_calculated_variables()
            calculated_vars.sort(key=lambda var: var.name)
            self._notify_variable_listeners()

    def add_view_error_listeners(self, listener: SyntaxErrorListener):
        self._error_listeners.append(listener)

    def add_view_variable_listeners(self, listener: CalculatedVariableObserver):
        self._calculated_variable_listeners.append(listener)

    def get_calculated_variables(self) -> List[CalculatedVariable]:
        calculated_vars = self._model.get_calculated_variables().copy()
        calculated_vars.sort(key=lambda var: var.name)
        return calculated_vars

    def solve_system(self):
        errors = self._model.get_errors()
        self._notify_syntax_error_listeners(errors)
        if not errors:
            system_solved = self._model.solve_system()
            if system_solved:
                self._notify_variable_listeners()

    def _notify_syntax_error_listeners(self, errors: List[EquationSyntaxError]):
        for listener in self._error_listeners:
            listener.handle_errors(errors)

    def _notify_variable_listeners(self):
        for listener in self._calculated_variable_listeners:
            listener.update_variables()

    def set_variable_initial_value(self, var_name: str, value: float):
        self._model.set_variable_initial_value(var_name, value)
