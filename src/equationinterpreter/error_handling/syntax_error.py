class EquationSyntaxError:
    def __init__(self, recognizer, offending_symbol, line, column, msg, e):
        self._recognizer = recognizer
        self._offending_symbol = offending_symbol
        self._line = line
        self._column = column
        self._msg = msg
        self._exception = e

    @property
    def line(self):
        return self._line

    @property
    def message(self):
        return self._msg
