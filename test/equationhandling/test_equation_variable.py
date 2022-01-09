from unittest import TestCase
from src.equationhandling.equation_variable import *


class TestEquationVariable(TestCase):
    def test_init_raises_exception_for_invalid_type(self):
        with self.assertRaises(TypeError):
            TestEquationVariable(1)

    def test_init_raises_exception_for_None_name(self):
        with self.assertRaises(TypeError):
            TestEquationVariable(None)

    def test_equals_same_name(self):
        variable_one = TestEquationVariableImpl("a")
        variable_two = TestEquationVariableImpl("a")

        self.assertTrue(variable_one == variable_two)

    def test_not_equals_same_name(self):
        variable_one = TestEquationVariableImpl("a")
        variable_two = TestEquationVariableImpl("a")

        self.assertFalse(variable_one != variable_two)

    def test_equals_same_name_different_case(self):
        variable_one = TestEquationVariableImpl("a")
        variable_two = TestEquationVariableImpl("A")

        self.assertTrue(variable_one == variable_two)

    def test_not_equals_same_name_different_case(self):
        variable_one = TestEquationVariableImpl("a")
        variable_two = TestEquationVariableImpl("A")

        self.assertFalse(variable_one != variable_two)

    def test_equals_different_name(self):
        variable_one = TestEquationVariableImpl("a")
        variable_two = TestEquationVariableImpl("b")

        self.assertFalse(variable_one == variable_two)

    def test_not_equals_different_name(self):
        variable_one = TestEquationVariableImpl("a")
        variable_two = TestEquationVariableImpl("b")

        self.assertTrue(variable_one != variable_two)


class TestEquationVariableImpl(EquationVariable):
    def __init__(self, name: str):
        super().__init__(name)
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def value(self) -> float:
        return 1.0
