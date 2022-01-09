# Generated from C:/Users/Alex/PycharmProjects/PersonalProject/src/antlr\Calc.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete listener for a parse tree produced by CalcParser.
class CalcListener(ParseTreeListener):

    # Enter a parse tree produced by CalcParser#parse.
    def enterParse(self, ctx:CalcParser.ParseContext):
        pass

    # Exit a parse tree produced by CalcParser#parse.
    def exitParse(self, ctx:CalcParser.ParseContext):
        pass


    # Enter a parse tree produced by CalcParser#EquationExpression.
    def enterEquationExpression(self, ctx:CalcParser.EquationExpressionContext):
        pass

    # Exit a parse tree produced by CalcParser#EquationExpression.
    def exitEquationExpression(self, ctx:CalcParser.EquationExpressionContext):
        pass


    # Enter a parse tree produced by CalcParser#assignment.
    def enterAssignment(self, ctx:CalcParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CalcParser#assignment.
    def exitAssignment(self, ctx:CalcParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CalcParser#comment.
    def enterComment(self, ctx:CalcParser.CommentContext):
        pass

    # Exit a parse tree produced by CalcParser#comment.
    def exitComment(self, ctx:CalcParser.CommentContext):
        pass


    # Enter a parse tree produced by CalcParser#ArithmeticExpressionPow.
    def enterArithmeticExpressionPow(self, ctx:CalcParser.ArithmeticExpressionPowContext):
        pass

    # Exit a parse tree produced by CalcParser#ArithmeticExpressionPow.
    def exitArithmeticExpressionPow(self, ctx:CalcParser.ArithmeticExpressionPowContext):
        pass


    # Enter a parse tree produced by CalcParser#ArithmeticExpressionParens.
    def enterArithmeticExpressionParens(self, ctx:CalcParser.ArithmeticExpressionParensContext):
        pass

    # Exit a parse tree produced by CalcParser#ArithmeticExpressionParens.
    def exitArithmeticExpressionParens(self, ctx:CalcParser.ArithmeticExpressionParensContext):
        pass


    # Enter a parse tree produced by CalcParser#ArithmeticExpressionNumericEntity.
    def enterArithmeticExpressionNumericEntity(self, ctx:CalcParser.ArithmeticExpressionNumericEntityContext):
        pass

    # Exit a parse tree produced by CalcParser#ArithmeticExpressionNumericEntity.
    def exitArithmeticExpressionNumericEntity(self, ctx:CalcParser.ArithmeticExpressionNumericEntityContext):
        pass


    # Enter a parse tree produced by CalcParser#ArithmeticExpressionMultDiv.
    def enterArithmeticExpressionMultDiv(self, ctx:CalcParser.ArithmeticExpressionMultDivContext):
        pass

    # Exit a parse tree produced by CalcParser#ArithmeticExpressionMultDiv.
    def exitArithmeticExpressionMultDiv(self, ctx:CalcParser.ArithmeticExpressionMultDivContext):
        pass


    # Enter a parse tree produced by CalcParser#ArithmeticExpressionPlusMinus.
    def enterArithmeticExpressionPlusMinus(self, ctx:CalcParser.ArithmeticExpressionPlusMinusContext):
        pass

    # Exit a parse tree produced by CalcParser#ArithmeticExpressionPlusMinus.
    def exitArithmeticExpressionPlusMinus(self, ctx:CalcParser.ArithmeticExpressionPlusMinusContext):
        pass


    # Enter a parse tree produced by CalcParser#NumericConst.
    def enterNumericConst(self, ctx:CalcParser.NumericConstContext):
        pass

    # Exit a parse tree produced by CalcParser#NumericConst.
    def exitNumericConst(self, ctx:CalcParser.NumericConstContext):
        pass


    # Enter a parse tree produced by CalcParser#NumericVariable.
    def enterNumericVariable(self, ctx:CalcParser.NumericVariableContext):
        pass

    # Exit a parse tree produced by CalcParser#NumericVariable.
    def exitNumericVariable(self, ctx:CalcParser.NumericVariableContext):
        pass



del CalcParser