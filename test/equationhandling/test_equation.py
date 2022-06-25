from unittest import TestCase

from parameterized import parameterized

from src.equationhandling.equation import Equation
from src.equationhandling.equation_variable import CalculatedVariable
from src.equationhandling.equation_variables_collection import VariablesCollection


class TestEquation(TestCase):
    simple_equation = ["-", "x1", "1", -0.5]
    one_variable_and_addition =["-", "+", "x1", "1", "1", 0.5]
    one_variable_and_subtraction =["-", "-", "x1", "1", "1", -1.5]
    one_variable_and_multiplication = ["-", "*", "x1", "2", "1", 0]
    one_variable_and_division = ["-", "/", "x1", "0.25", "1", 1]
    one_variable_and_power = ["-", "^", "x1", "2", "1", -0.75]
    params = [
        [simple_equation],
        [one_variable_and_addition],
        [one_variable_and_subtraction],
        [one_variable_and_multiplication],
        [one_variable_and_division],
        [one_variable_and_power]
    ]

    @parameterized.expand(params)
    def test_evaluate_equation_expression(self, params):
        equation_builder = EquationBuilder(params)
        equation = equation_builder.build_equation()

        result = equation.evaluate_equation_expression()

        self.assertEqual(result, params[-1])


class EquationBuilder:
    def __init__(self, equation_terms):
        self.equation_terms = equation_terms
        self.variables_collection = self._create_variables_collection(
            equation_terms[:-1])

    @staticmethod
    def _create_variables_collection(equation_terms):
        variables_collection = VariablesCollection()
        for term in equation_terms:
            try:
                float(term)
            except ValueError:
                variables_collection.add_variable(CalculatedVariable(term))
        return variables_collection

    def build_equation(self):
        equation = Equation(self.variables_collection)
        for term in self.equation_terms[:-1]:
            equation.add_term(term)
        return equation
