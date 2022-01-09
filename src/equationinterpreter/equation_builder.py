from antlr4 import *
from src.antlr import CalcParser
from src.equationhandling.equation_system import EquationSystem


class EquationBuilder(ParseTreeListener):
    def __init__(self, equation_system: EquationSystem):
        self._equation_system = equation_system
        self._in_assignment = False
        self._in_comment = False

    def enterParse(self, ctx):
        pass

    def exitParse(self, ctx):
        pass

    def enterEquationExpression(self, ctx):
        self._equation_system.add_new_equation()
        self._equation_system.add_term_to_last_equation("-")

    def exitEquationExpression(self, ctx):
        pass

    def enterAssignment(self, ctx):
        self._in_assignment = True
        variable_name = ctx._children[0].getText()
        variable_value = ctx._children[2].getText()
        self._equation_system.add_assigned_variable(variable_name, float(variable_value))

    def exitAssignment(self, ctx):
        self._in_assignment = False

    def enterComment(self, ctx):
        self._in_comment = True

    def exitComment(self, ctx):
        self._in_comment = False

    def enterArithmeticExpressionPow(self, ctx):
        self._equation_system.add_term_to_last_equation(ctx._children[1].getText())

    def exitArithmeticExpressionPow(self, ctx):
        pass

    def enterArithmeticExpressionParens(self, ctx):
        pass

    def exitArithmeticExpressionParens(self, ctx):
        pass

    def enterArithmeticExpressionNumericEntity(self, ctx):
        pass

    def exitArithmeticExpressionNumericEntity(self, ctx):
        pass

    def enterArithmeticExpressionMultDiv(self, ctx):
        self._equation_system.add_term_to_last_equation(ctx._children[1].getText())

    def exitArithmeticExpressionMultDiv(self, ctx):
        pass

    def enterArithmeticExpressionPlusMinus(self, ctx):
        self._equation_system.add_term_to_last_equation(ctx._children[1].getText())

    def exitArithmeticExpressionPlusMinus(self, ctx):
        pass

    def enterNumericConst(self, ctx):
        if not self._in_assignment and not self._in_comment:
            self._equation_system.add_term_to_last_equation(ctx.getText())

    def exitNumericConst(self, ctx):
        pass

    def enterNumericVariable(self, ctx):
        if not self._in_assignment and not self._in_comment:
            variable_of_equation = ctx.getText()
            self._equation_system.add_calculated_variable(variable_of_equation)
            self._equation_system.add_term_to_last_equation(variable_of_equation)

    def exitNumericVariable(self, ctx):
        pass


del CalcParser