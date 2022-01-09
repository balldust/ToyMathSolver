# Code adapted from: https://wiki.python.org/moin/PyQt/Python%20syntax%20highlighting
from PyQt5 import QtCore, QtGui

from src.equationinterpreter.error_handling.syntax_error import EquationSyntaxError
from src.util.listeners.error_listeners import SyntaxErrorListener


def create_format(color, style=''):
    """Return a QTextCharFormat with the given attributes.
    """
    _color = QtGui.QColor()
    _color.setNamedColor(color)

    _format = QtGui.QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QtGui.QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)

    return _format


# Syntax styles that can be shared by all languages
STYLES = {
    'operator': create_format('red'),
    'brace': create_format('darkGray'),
    'comment': create_format('darkGreen', 'italic'),
    'numbers': create_format('magenta'),
}


class TextHighlighterMeta(type(QtGui.QSyntaxHighlighter), type(SyntaxErrorListener)):
    pass


class TextHighlighter(QtGui.QSyntaxHighlighter, SyntaxErrorListener, metaclass=TextHighlighterMeta):
    operators = [
        '=', ':=', ';',
        # Arithmetic
        '\+', '-', '/', '\^'
    ]

    def __init__(self, parent: QtGui.QTextDocument) -> None:
        super().__init__(parent)
        self._error_block_numbers = []
        # Multi-line strings (expression, flag, style)
        self.comment = (QtCore.QRegExp('//'), 1, STYLES['comment'])

        rules = []
        rules += [(r'%s' % o, 0, STYLES['operator'])
                  for o in TextHighlighter.operators]

        # All other rules
        rules += [
            # Numeric literals
            (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, STYLES['numbers'])
        ]

        # Build a QRegExp for each pattern
        self.rules = [(QtCore.QRegExp(pat), index, fmt)
            for (pat, index, fmt) in rules]

    def highlightBlock(self, text):
        """Apply syntax highlighting to the given block of text.
        """
        if self.currentBlock().blockNumber() in self._error_block_numbers:
            _color = QtGui.QColor()
            _color.setNamedColor("gray")

            _format = QtGui.QTextCharFormat()
            _format.setBackground(_color)
            self.setFormat(0, len(text), _format)
        else:
            self._format_text(text)


    def _format_text(self, text):
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)
            while index >= 0:
                # We actually want the index of the nth match
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        # Do multi-line strings
        self.match_multiline(text, *self.comment)

    def match_multiline(self, text, delimiter, in_state, style):
        """Do highlighting of multi-line strings. ``delimiter`` should be a
        ``QRegExp`` for triple-single-quotes or triple-double-quotes, and
        ``in_state`` should be a unique integer to represent the corresponding
        state changes when inside those strings. Returns True if we're still
        inside a multi-line string when this function is finished.
        """
        # If inside triple-single quotes, start at 0
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        # Otherwise, look for the delimiter on this line
        else:
            start = delimiter.indexIn(text)
            # Move past this match
            add = delimiter.matchedLength()

        # As long as there's a delimiter match on this line...
        while start >= 0:
            # Look for the ending delimiter
            end = delimiter.indexIn(text, start + add)
            # Ending delimiter on this line?
            if end >= add:
                base_length = end - start + add
                length = base_length if base_length > 0 else base_length + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            # No; multi-line string
            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add
            # Apply formatting
            self.setFormat(start, length, style)
            # Look for the next match
            start = delimiter.indexIn(text, start + length)

        # Return True if still inside a multi-line string, False otherwise
        return self.currentBlockState() == in_state

    def handle_errors(self, errors: list[EquationSyntaxError]):
        self._error_block_numbers = [err.line - 1 for err in errors]
        for i in range(self.document().blockCount()):
            block = self.document().findBlockByLineNumber(i)
            self.rehighlightBlock(block)
        self._error_block_numbers = []
