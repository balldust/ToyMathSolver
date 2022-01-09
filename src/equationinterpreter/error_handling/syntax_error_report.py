from antlr4.error.ErrorListener import ErrorListener

from src.equationinterpreter.error_handling.syntax_error import EquationSyntaxError


class SyntaxErrorReporter(ErrorListener):
    def __init__(self):
        self._errors = []

    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        error = EquationSyntaxError(recognizer, offending_symbol, line, column, msg, e)
        self._errors.append(error)

    @property
    def errors(self) -> list[EquationSyntaxError]:
        return self._errors

    def syntax_has_errors(self):
        return len(self._errors) > 0

    def clear_errors(self):
        self._errors = []
