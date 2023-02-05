from abc import ABC, abstractmethod

from src.equationinterpreter.error_handling.syntax_error import (
    EquationSyntaxError,
)


class SyntaxErrorListener(ABC):
    @abstractmethod
    def handle_errors(self, errors: list[EquationSyntaxError]):
        pass
