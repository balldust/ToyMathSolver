from PyQt5.QtWidgets import QPlainTextEdit

from src.equationinterpreter.error_handling.syntax_error import EquationSyntaxError
from src.util.listeners.error_listeners import SyntaxErrorListener


class OutputReportView(SyntaxErrorListener):
    def __init__(self):
        self._report_view = QPlainTextEdit()
        self._report_view.setReadOnly(True)

    def handle_errors(self, errors: list[EquationSyntaxError]):
        error_messages = []
        for error in errors:
            error_messages.append(error.message)
        self._report_view.setPlainText('\n'.join(error_messages))

    @property
    def report_view(self) -> QPlainTextEdit:
        return self._report_view