from antlr4 import *
from src.antlr.CalcLexer import CalcLexer
from src.antlr.CalcParser import CalcParser
from src.equationhandling.equation_variable import CalculatedVariable
from src.equationinterpreter.equation_builder import EquationBuilder
from src.equationhandling.equation_system import EquationSystem
from src.equationinterpreter.error_handling.syntax_error import (
    EquationSyntaxError,
)
from src.equationinterpreter.error_handling.syntax_error_report import (
    SyntaxErrorReporter,
)
from src.solvers.nl_solver import NonLinearEquationSolver
from src.solvers.nl_solver_specification import NonLinearSolverSpecifications


class ProblemExecution:
    def __init__(self):
        self._equation_text = ""
        self._equation_system = EquationSystem()
        self._nl_solver_specs = NonLinearSolverSpecifications()
        self._error_reporter = SyntaxErrorReporter()

    def construct_system(self) -> bool:
        new_equation_system = EquationSystem()
        self._error_reporter.clear_errors()
        lexer = CalcLexer(InputStream(self._equation_text))
        tokens = CommonTokenStream(lexer)
        parser = CalcParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(self._error_reporter)
        tree = parser.parse()
        if not self._error_reporter.syntax_has_errors():
            walker = ParseTreeWalker()
            listener = EquationBuilder(new_equation_system)
            walker.walk(listener, tree)
            self._calculate_new_equation_system(new_equation_system)
            return True
        return False

    def _calculate_new_equation_system(
        self, new_equation_system: EquationSystem
    ):
        for var in self._equation_system.calculated_variables():
            if new_equation_system.has_variable(var.name):
                new_equation_system.set_variable_initial_value(
                    var.name, var.initial_value
                )
                new_equation_system.set_variable_value(var.name, var.value)
        self._equation_system = new_equation_system

    def get_errors(self) -> list[EquationSyntaxError]:
        return self._error_reporter.errors

    def solve_system(self) -> bool:
        if self._equation_system.no_structural_errors():
            self._equation_system.initialize_calculated_variables()
            solver = NonLinearEquationSolver(
                self._equation_system, self._nl_solver_specs
            )
            return solver.solve()
        return False

    def get_calculated_variables(self) -> list[CalculatedVariable]:
        return self._equation_system.calculated_variables()

    def set_variable_initial_value(self, var_name: str, value: float):
        self._equation_system.set_variable_initial_value(var_name, value)

    def set_text(self, text: str):
        self._equation_text = text

    @property
    def nl_solver_specs(self) -> NonLinearSolverSpecifications:
        return self._nl_solver_specs
