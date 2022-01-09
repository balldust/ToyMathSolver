from unittest import TestCase

from src.equationhandling.equation_variable import CalculatedVariable, AssignedVariable
from src.equationhandling.equation_variables_collection import VariablesCollection


class TestVariablesCollection(TestCase):
    def test_add_variable(self):
        variables = VariablesCollection()
        var_to_add = CalculatedVariable("x1")

        variables.add_variable(var_to_add)

        self.assertIn(var_to_add, variables._variables)

    def test_add_variable_given_existing_variable_with_same_name(self):
        variables = VariablesCollection()
        var_to_add = CalculatedVariable("x1")
        var_to_add_same_name = CalculatedVariable("x1")

        variables.add_variable(var_to_add)
        variables.add_variable(var_to_add_same_name)

        self.assertEqual(len(variables._variables), 1)

    def test_add_variable_given_existing_variable_with_same_name_different_case(self):
        variables = VariablesCollection()
        var_to_add = CalculatedVariable("x")
        var_to_add_same_name = CalculatedVariable("X")

        variables.add_variable(var_to_add)
        variables.add_variable(var_to_add_same_name)

        self.assertEqual(len(variables._variables), 1)

    def test_add_variable_given_illegal_type(self):
        variables = VariablesCollection()
        with self.assertRaises(Exception):
            variables.add_variable("test")

    def test_has_variable(self):
        variables = VariablesCollection()
        var_name = "x1"
        var_to_add = CalculatedVariable(var_name)
        variables.add_variable(var_to_add)

        self.assertTrue(variables.has_variable(var_name))

    def test_get_variable_value(self):
        variables = VariablesCollection()
        var_name = "x1"
        var_to_add = CalculatedVariable(var_name)
        expected_value = 1
        var_to_add.value = expected_value
        variables.add_variable(var_to_add)

        obtained_value = variables.get_variable_value(var_name)

        self.assertEqual(obtained_value, expected_value)

    def test_calculated_variables(self):
        variables = VariablesCollection()
        var_to_add_calc = CalculatedVariable("x1")
        var_to_add_assigned = AssignedVariable("x2")
        variables.add_variable(var_to_add_calc)
        variables.add_variable(var_to_add_assigned)

        self.assertEqual(len(variables.calculated_variables()), 1)
