from src.equationhandling.equation_variables_collection import (
    VariablesCollection,
)


class Equation:
    def __init__(self, variables: VariablesCollection):
        self._equation_terms = []
        self._variables = variables

    def add_term(self, term: str):
        self._equation_terms.append(term)

    def evaluate_equation_expression(self) -> float:
        result = []
        for term in self._equation_terms[::-1]:
            if self._is_top_term_an_operation(term):
                last_added_number = self._get_value_of_equation_variable(
                    result[-1]
                )
                result.pop()
                last_val = self._get_value_of_equation_variable(result[-1])
                result.pop()
                result.append(
                    self._get_result_based_on_operation(
                        last_added_number, last_val, term
                    )
                )
            else:
                result.append(term)
        return float(result[0])

    @staticmethod
    def _is_top_term_an_operation(term: str) -> bool:
        return (
            term == "+"
            or term == "-"
            or term == "*"
            or term == "/"
            or term == "^"
        )

    def _get_value_of_equation_variable(self, term: str) -> float:
        if self._variables.has_variable(term):
            return self._variables.get_variable_value(term)
        return float(term)

    @staticmethod
    def _get_result_based_on_operation(
        val_left: float, val_right: float, operation: str
    ) -> str:
        if operation == "+":
            return str(val_left + val_right)
        elif operation == "-":
            return str(val_left - val_right)
        elif operation == "*":
            return str(val_left * val_right)
        elif operation == "/":
            return str(val_left / val_right)
        elif operation == "^":
            return str(val_left**val_right)
        else:
            raise Exception("Unexpected value: " + operation)
