# Generated from C:/Users/Alex/PycharmProjects/PersonalProject/src/antlr\Calc.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("W\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\5\4#\n\4\3\4\3\4\3\5\7")
        buf.write("\5(\n\5\f\5\16\5+\13\5\3\5\6\5.\n\5\r\5\16\5/\7\5\62\n")
        buf.write("\5\f\5\16\5\65\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6?\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6J\n\6\f")
        buf.write("\6\16\6M\13\6\3\7\3\7\3\7\5\7R\n\7\3\7\5\7U\n\7\3\7\2")
        buf.write("\3\n\b\2\4\6\b\n\f\2\4\3\2\4\5\3\2\6\7\2]\2\23\3\2\2\2")
        buf.write("\4\30\3\2\2\2\6\35\3\2\2\2\b)\3\2\2\2\n>\3\2\2\2\fT\3")
        buf.write("\2\2\2\16\22\5\4\3\2\17\22\5\6\4\2\20\22\5\b\5\2\21\16")
        buf.write("\3\2\2\2\21\17\3\2\2\2\21\20\3\2\2\2\22\25\3\2\2\2\23")
        buf.write("\21\3\2\2\2\23\24\3\2\2\2\24\26\3\2\2\2\25\23\3\2\2\2")
        buf.write("\26\27\7\2\2\3\27\3\3\2\2\2\30\31\5\n\6\2\31\32\7\r\2")
        buf.write("\2\32\33\5\n\6\2\33\34\7\27\2\2\34\5\3\2\2\2\35\36\7\21")
        buf.write("\2\2\36\"\7\30\2\2\37#\7\22\2\2 !\7\7\2\2!#\7\22\2\2\"")
        buf.write("\37\3\2\2\2\" \3\2\2\2#$\3\2\2\2$%\7\27\2\2%\7\3\2\2\2")
        buf.write("&(\7\20\2\2\'&\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2")
        buf.write("*\63\3\2\2\2+)\3\2\2\2,.\7\21\2\2-,\3\2\2\2./\3\2\2\2")
        buf.write("/-\3\2\2\2/\60\3\2\2\2\60\62\3\2\2\2\61-\3\2\2\2\62\65")
        buf.write("\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2\65")
        buf.write("\63\3\2\2\2\66\67\7\20\2\2\67\t\3\2\2\289\b\6\1\29:\7")
        buf.write("\16\2\2:;\5\n\6\2;<\7\17\2\2<?\3\2\2\2=?\5\f\7\2>8\3\2")
        buf.write("\2\2>=\3\2\2\2?K\3\2\2\2@A\f\6\2\2AB\7\3\2\2BJ\5\n\6\7")
        buf.write("CD\f\5\2\2DE\t\2\2\2EJ\5\n\6\6FG\f\4\2\2GH\t\3\2\2HJ\5")
        buf.write("\n\6\5I@\3\2\2\2IC\3\2\2\2IF\3\2\2\2JM\3\2\2\2KI\3\2\2")
        buf.write("\2KL\3\2\2\2L\13\3\2\2\2MK\3\2\2\2NR\7\22\2\2OP\7\7\2")
        buf.write("\2PR\7\22\2\2QN\3\2\2\2QO\3\2\2\2RU\3\2\2\2SU\7\21\2\2")
        buf.write("TQ\3\2\2\2TS\3\2\2\2U\r\3\2\2\2\r\21\23\")/\63>IKQT")
        return buf.getvalue()


class CalcParser ( Parser ):

    grammarFileName = "Calc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'^'", "'*'", "'/'", "'+'", "'-'", "'!='", 
                     "'>='", "'<='", "'>'", "'<'", "'='", "'('", "')'", 
                     "'//'", "<INVALID>", "<INVALID>", "<INVALID>", "'$'", 
                     "<INVALID>", "<INVALID>", "';'", "':='" ]

    symbolicNames = [ "<INVALID>", "POW", "MUL", "DIV", "ADD", "SUB", "NEQ", 
                      "GE", "LE", "GT", "LT", "EQ", "LPAREN", "RPAREN", 
                      "DOUBLESLASH", "ID", "NUMBER", "STRINGLITERAL", "DOLLAR", 
                      "NEWLINE", "WS", "SEMICOLON", "ASSIGN" ]

    RULE_parse = 0
    RULE_equation = 1
    RULE_assignment = 2
    RULE_comment = 3
    RULE_arithmetic_expr = 4
    RULE_numeric_entity = 5

    ruleNames =  [ "parse", "equation", "assignment", "comment", "arithmetic_expr", 
                   "numeric_entity" ]

    EOF = Token.EOF
    POW=1
    MUL=2
    DIV=3
    ADD=4
    SUB=5
    NEQ=6
    GE=7
    LE=8
    GT=9
    LT=10
    EQ=11
    LPAREN=12
    RPAREN=13
    DOUBLESLASH=14
    ID=15
    NUMBER=16
    STRINGLITERAL=17
    DOLLAR=18
    NEWLINE=19
    WS=20
    SEMICOLON=21
    ASSIGN=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CalcParser.EOF, 0)

        def equation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.EquationContext)
            else:
                return self.getTypedRuleContext(CalcParser.EquationContext,i)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(CalcParser.AssignmentContext,i)


        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.CommentContext)
            else:
                return self.getTypedRuleContext(CalcParser.CommentContext,i)


        def getRuleIndex(self):
            return CalcParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParse" ):
                return visitor.visitParse(self)
            else:
                return visitor.visitChildren(self)




    def parse(self):

        localctx = CalcParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcParser.SUB) | (1 << CalcParser.LPAREN) | (1 << CalcParser.DOUBLESLASH) | (1 << CalcParser.ID) | (1 << CalcParser.NUMBER))) != 0):
                self.state = 15
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 12
                    self.equation()
                    pass

                elif la_ == 2:
                    self.state = 13
                    self.assignment()
                    pass

                elif la_ == 3:
                    self.state = 14
                    self.comment()
                    pass


                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(CalcParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EquationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcParser.RULE_equation

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EquationExpressionContext(EquationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.EquationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmetic_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.Arithmetic_exprContext)
            else:
                return self.getTypedRuleContext(CalcParser.Arithmetic_exprContext,i)

        def EQ(self):
            return self.getToken(CalcParser.EQ, 0)
        def SEMICOLON(self):
            return self.getToken(CalcParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquationExpression" ):
                listener.enterEquationExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquationExpression" ):
                listener.exitEquationExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquationExpression" ):
                return visitor.visitEquationExpression(self)
            else:
                return visitor.visitChildren(self)



    def equation(self):

        localctx = CalcParser.EquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_equation)
        try:
            localctx = CalcParser.EquationExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.arithmetic_expr(0)
            self.state = 23
            self.match(CalcParser.EQ)
            self.state = 24
            self.arithmetic_expr(0)
            self.state = 25
            self.match(CalcParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalcParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CalcParser.ASSIGN, 0)

        def SEMICOLON(self):
            return self.getToken(CalcParser.SEMICOLON, 0)

        def NUMBER(self):
            return self.getToken(CalcParser.NUMBER, 0)

        def SUB(self):
            return self.getToken(CalcParser.SUB, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = CalcParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(CalcParser.ID)
            self.state = 28
            self.match(CalcParser.ASSIGN)
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalcParser.NUMBER]:
                self.state = 29
                self.match(CalcParser.NUMBER)
                pass
            elif token in [CalcParser.SUB]:
                self.state = 30
                self.match(CalcParser.SUB)
                self.state = 31
                self.match(CalcParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 34
            self.match(CalcParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLESLASH(self, i:int=None):
            if i is None:
                return self.getTokens(CalcParser.DOUBLESLASH)
            else:
                return self.getToken(CalcParser.DOUBLESLASH, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CalcParser.ID)
            else:
                return self.getToken(CalcParser.ID, i)

        def getRuleIndex(self):
            return CalcParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = CalcParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 36
                    self.match(CalcParser.DOUBLESLASH) 
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CalcParser.ID:
                self.state = 43 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 42
                        self.match(CalcParser.ID)

                    else:
                        raise NoViableAltException(self)
                    self.state = 45 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(CalcParser.DOUBLESLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithmetic_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcParser.RULE_arithmetic_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ArithmeticExpressionPowContext(Arithmetic_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.Arithmetic_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmetic_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.Arithmetic_exprContext)
            else:
                return self.getTypedRuleContext(CalcParser.Arithmetic_exprContext,i)

        def POW(self):
            return self.getToken(CalcParser.POW, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpressionPow" ):
                listener.enterArithmeticExpressionPow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpressionPow" ):
                listener.exitArithmeticExpressionPow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticExpressionPow" ):
                return visitor.visitArithmeticExpressionPow(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticExpressionParensContext(Arithmetic_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.Arithmetic_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(CalcParser.LPAREN, 0)
        def arithmetic_expr(self):
            return self.getTypedRuleContext(CalcParser.Arithmetic_exprContext,0)

        def RPAREN(self):
            return self.getToken(CalcParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpressionParens" ):
                listener.enterArithmeticExpressionParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpressionParens" ):
                listener.exitArithmeticExpressionParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticExpressionParens" ):
                return visitor.visitArithmeticExpressionParens(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticExpressionNumericEntityContext(Arithmetic_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.Arithmetic_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def numeric_entity(self):
            return self.getTypedRuleContext(CalcParser.Numeric_entityContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpressionNumericEntity" ):
                listener.enterArithmeticExpressionNumericEntity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpressionNumericEntity" ):
                listener.exitArithmeticExpressionNumericEntity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticExpressionNumericEntity" ):
                return visitor.visitArithmeticExpressionNumericEntity(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticExpressionMultDivContext(Arithmetic_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.Arithmetic_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmetic_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.Arithmetic_exprContext)
            else:
                return self.getTypedRuleContext(CalcParser.Arithmetic_exprContext,i)

        def MUL(self):
            return self.getToken(CalcParser.MUL, 0)
        def DIV(self):
            return self.getToken(CalcParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpressionMultDiv" ):
                listener.enterArithmeticExpressionMultDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpressionMultDiv" ):
                listener.exitArithmeticExpressionMultDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticExpressionMultDiv" ):
                return visitor.visitArithmeticExpressionMultDiv(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticExpressionPlusMinusContext(Arithmetic_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.Arithmetic_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmetic_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.Arithmetic_exprContext)
            else:
                return self.getTypedRuleContext(CalcParser.Arithmetic_exprContext,i)

        def ADD(self):
            return self.getToken(CalcParser.ADD, 0)
        def SUB(self):
            return self.getToken(CalcParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpressionPlusMinus" ):
                listener.enterArithmeticExpressionPlusMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpressionPlusMinus" ):
                listener.exitArithmeticExpressionPlusMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticExpressionPlusMinus" ):
                return visitor.visitArithmeticExpressionPlusMinus(self)
            else:
                return visitor.visitChildren(self)



    def arithmetic_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalcParser.Arithmetic_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_arithmetic_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalcParser.LPAREN]:
                localctx = CalcParser.ArithmeticExpressionParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 55
                self.match(CalcParser.LPAREN)
                self.state = 56
                self.arithmetic_expr(0)
                self.state = 57
                self.match(CalcParser.RPAREN)
                pass
            elif token in [CalcParser.SUB, CalcParser.ID, CalcParser.NUMBER]:
                localctx = CalcParser.ArithmeticExpressionNumericEntityContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.numeric_entity()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 71
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = CalcParser.ArithmeticExpressionPowContext(self, CalcParser.Arithmetic_exprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expr)
                        self.state = 62
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")

                        self.state = 63
                        self.match(CalcParser.POW)
                        self.state = 64
                        self.arithmetic_expr(5)
                        pass

                    elif la_ == 2:
                        localctx = CalcParser.ArithmeticExpressionMultDivContext(self, CalcParser.Arithmetic_exprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expr)
                        self.state = 65
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 66
                        _la = self._input.LA(1)
                        if not(_la==CalcParser.MUL or _la==CalcParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 67
                        self.arithmetic_expr(4)
                        pass

                    elif la_ == 3:
                        localctx = CalcParser.ArithmeticExpressionPlusMinusContext(self, CalcParser.Arithmetic_exprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expr)
                        self.state = 68
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 69
                        _la = self._input.LA(1)
                        if not(_la==CalcParser.ADD or _la==CalcParser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 70
                        self.arithmetic_expr(3)
                        pass

             
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Numeric_entityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcParser.RULE_numeric_entity

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumericConstContext(Numeric_entityContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.Numeric_entityContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(CalcParser.NUMBER, 0)
        def SUB(self):
            return self.getToken(CalcParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericConst" ):
                listener.enterNumericConst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericConst" ):
                listener.exitNumericConst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericConst" ):
                return visitor.visitNumericConst(self)
            else:
                return visitor.visitChildren(self)


    class NumericVariableContext(Numeric_entityContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.Numeric_entityContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalcParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericVariable" ):
                listener.enterNumericVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericVariable" ):
                listener.exitNumericVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericVariable" ):
                return visitor.visitNumericVariable(self)
            else:
                return visitor.visitChildren(self)



    def numeric_entity(self):

        localctx = CalcParser.Numeric_entityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_numeric_entity)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalcParser.SUB, CalcParser.NUMBER]:
                localctx = CalcParser.NumericConstContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CalcParser.NUMBER]:
                    self.state = 76
                    self.match(CalcParser.NUMBER)
                    pass
                elif token in [CalcParser.SUB]:
                    self.state = 77
                    self.match(CalcParser.SUB)
                    self.state = 78
                    self.match(CalcParser.NUMBER)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [CalcParser.ID]:
                localctx = CalcParser.NumericVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.match(CalcParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.arithmetic_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithmetic_expr_sempred(self, localctx:Arithmetic_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




