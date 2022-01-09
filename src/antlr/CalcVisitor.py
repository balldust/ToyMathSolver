# Generated from C:/Users/Alex/PycharmProjects/PersonalProject/src/antlr\Calc.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete generic visitor for a parse tree produced by CalcParser.

class CalcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalcParser#parse.
    def visitParse(self, ctx:CalcParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#EquationExpression.
    def visitEquationExpression(self, ctx:CalcParser.EquationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#assignment.
    def visitAssignment(self, ctx:CalcParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#comment.
    def visitComment(self, ctx:CalcParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#ArithmeticExpressionPow.
    def visitArithmeticExpressionPow(self, ctx:CalcParser.ArithmeticExpressionPowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#ArithmeticExpressionParens.
    def visitArithmeticExpressionParens(self, ctx:CalcParser.ArithmeticExpressionParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#ArithmeticExpressionNumericEntity.
    def visitArithmeticExpressionNumericEntity(self, ctx:CalcParser.ArithmeticExpressionNumericEntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#ArithmeticExpressionMultDiv.
    def visitArithmeticExpressionMultDiv(self, ctx:CalcParser.ArithmeticExpressionMultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#ArithmeticExpressionPlusMinus.
    def visitArithmeticExpressionPlusMinus(self, ctx:CalcParser.ArithmeticExpressionPlusMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#NumericConst.
    def visitNumericConst(self, ctx:CalcParser.NumericConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#NumericVariable.
    def visitNumericVariable(self, ctx:CalcParser.NumericVariableContext):
        return self.visitChildren(ctx)



del CalcParser