from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5 import QtGui

from src.util.listeners.text_listeners import TextListener


class EquationView(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self._listeners: list[TextListener] = []

    def register_key_listener(self, listener: TextListener):
        self._listeners.append(listener)

    def keyPressEvent(self, e: QtGui.QKeyEvent):
        super().keyPressEvent(e)
        for listener in self._listeners:
            listener.handle_text(self.toPlainText())
