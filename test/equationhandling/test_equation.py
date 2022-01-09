from unittest import TestCase

from src.equationhandling.equation import Equation
from src.equationhandling.equation_variable import CalculatedVariable
from src.equationhandling.equation_variables_collection import VariablesCollection


class TestEquation(TestCase):
    def test_evaluate_equation_expression_given_simple_equation(self):
        variables = VariablesCollection()
        var_name = "x1"
        var = CalculatedVariable(var_name)
        variables.add_variable(var)
        equation = Equation(variables)
        equation.add_term("-")
        equation.add_term(var_name)
        equation.add_term("1")

        result = equation.evaluate_equation_expression()

        self.assertEqual(result, -0.5)

    def test_evaluate_equation_expression_given_one_variable_and_addition_simple_equation(self):
        variables = VariablesCollection()
        var_name = "x1"
        var = CalculatedVariable(var_name)
        variables.add_variable(var)
        equation = Equation(variables)
        equation.add_term("-")
        equation.add_term("+")
        equation.add_term(var_name)
        equation.add_term("1")
        equation.add_term("1")

        result = equation.evaluate_equation_expression()

        self.assertEqual(result, 0.5)

    def test_evaluate_equation_expression_given_one_variable_and_subtraction_simple_equation(self):
        variables = VariablesCollection()
        var_name = "x1"
        var = CalculatedVariable(var_name)
        variables.add_variable(var)
        equation = Equation(variables)
        equation.add_term("-")
        equation.add_term("-")
        equation.add_term(var_name)
        equation.add_term("1")
        equation.add_term("1")

        result = equation.evaluate_equation_expression()

        self.assertEqual(result, -1.5)

    def test_evaluate_equation_expression_given_one_variable_and_multiplication_simple_equation(self):
        variables = VariablesCollection()
        var_name = "x1"
        var = CalculatedVariable(var_name)
        variables.add_variable(var)
        equation = Equation(variables)
        equation.add_term("-")
        equation.add_term("*")
        equation.add_term(var_name)
        equation.add_term("2")
        equation.add_term("1")

        result = equation.evaluate_equation_expression()

        self.assertEqual(result, 0)

    def test_evaluate_equation_expression_given_one_variable_and_division_simple_equation(self):
        variables = VariablesCollection()
        var_name = "x1"
        var = CalculatedVariable(var_name)
        variables.add_variable(var)
        equation = Equation(variables)
        equation.add_term("-")
        equation.add_term("/")
        equation.add_term(var_name)
        equation.add_term("0.25")
        equation.add_term("1")

        result = equation.evaluate_equation_expression()

        self.assertEqual(result, 1)

    def test_evaluate_equation_expression_given_one_variable_and_power_simple_equation(self):
        variables = VariablesCollection()
        var_name = "x1"
        var = CalculatedVariable(var_name)
        variables.add_variable(var)
        equation = Equation(variables)
        equation.add_term("-")
        equation.add_term("^")
        equation.add_term(var_name)
        equation.add_term("2")
        equation.add_term("1")

        result = equation.evaluate_equation_expression()

        self.assertEqual(result, -0.75)
