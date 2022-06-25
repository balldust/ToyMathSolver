from unittest import TestCase

import parameterized.parameterized

from src.equationhandling.equation_variable import *


class TestEquationVariable(TestCase):
    def test_init_raises_exception_for_invalid_type(self):
        with self.assertRaises(TypeError):
            TestEquationVariable(1)

    def test_init_raises_exception_for_None_name(self):
        with self.assertRaises(TypeError):
            TestEquationVariable(None)

    @parameterized.parameterized.expand(
        [["a", "a"], ["a", "A"]])
    def test_equals(self, name_1, name_2):
        variable_one = TestEquationVariableImpl(name_1)
        variable_two = TestEquationVariableImpl(name_2)

        self.assertTrue(variable_one == variable_two)

    def test_equals_different_name(self):
        variable_one = TestEquationVariableImpl("a")
        variable_two = TestEquationVariableImpl("b")

        self.assertFalse(variable_one == variable_two)


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
