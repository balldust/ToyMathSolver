from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
import src.userinterface.syntax_highlight as syntax
from .output_report_view import OutputReportView
from .settings_window import SettingsWindow
from .variables_table import VariablesTable
from ..execution.problem_execution import ProblemExecution
from ..image_utils import image_utils
from ..userinterface.equation_view import EquationView
from ..util.controllers.main_view_controller import MainViewController

StyleSheet = """
QWidget#Window {
    background-color: black;
}

QPushButton#PanelButton {
    background-color: transparent;
}

QPushButton#PanelButton:hover {
    background-color: gray;
}
QHeaderView
{
    background-color: black;
}
QHeaderView::section
{
    background-color: gray;
    color: white;
}

QTableView {
    color: white;
    background-color: black;
    selection-background-color: gray; 
}

QTableView QTableCornerButton::section {
    background-color: gray;
}

QLabel {
    color: white;
    font-size: 16px
}

QPlainTextEdit {
    color:white;
    background-color: black;
    border: 1px solid gray;
    font: Courier;
    font-size: 20px
}
"
"""


class MainWindow:
    def __init__(self):
        self._app = QApplication([])
        self._window = QWidget()
        self._problem_execution = ProblemExecution()
        self._controller = MainViewController(self._problem_execution)
        self._settings_window = SettingsWindow(self._problem_execution)
        self._configure_elements()
        self._bind_components_with_controller()

    def _configure_elements(self):
        layout = QVBoxLayout()
        buttons_layout = self._create_buttons_layout()
        view_layout = self._create_equation_view_and_variables_layout()
        report_layout = self._create_report_layout()
        layout.addLayout(buttons_layout)
        layout.addLayout(view_layout)
        layout.addLayout(report_layout)
        self._configure_window(layout)

    def _create_buttons_layout(self) -> QLayout:
        layout = QHBoxLayout()
        self._solve_button = self._create_panel_button("run_button.png")
        layout.addWidget(self._solve_button)
        self._solve_button.clicked.connect(self._controller.solve_system)
        self._settings = self._create_panel_button("settings_button.png")
        layout.addWidget(self._settings)
        self._settings.clicked.connect(self._show_settings)
        layout.setAlignment(self._solve_button, Qt.AlignRight)
        return layout

    def _show_settings(self):
        self._settings_window.show_window()

    @staticmethod
    def _create_panel_button(filename: str) -> QAbstractButton:
        button = QPushButton()
        icon = image_utils.create_qicon_from_filename(filename)
        button.setIcon(icon)
        button.setObjectName("PanelButton")
        button.setMaximumWidth(30)
        return button

    def _create_equation_view_and_variables_layout(self) -> QLayout:
        layout = QHBoxLayout()
        equation_view_layout = self._create_equation_view_layout()
        layout.addLayout(equation_view_layout)
        variables_layout = self._create_variables_layout()
        layout.addLayout(variables_layout)
        return layout

    def _create_equation_view_layout(self) -> QLayout:
        layout = QVBoxLayout()
        equation_view_label = QLabel("Equations")
        layout.addWidget(equation_view_label)
        self._equation_view = EquationView()
        self._equation_view.register_key_listener(self._controller)
        self._equation_view.setMinimumHeight(400)
        self.highlight = syntax.TextHighlighter(self._equation_view.document())
        layout.addWidget(self._equation_view)
        return layout

    def _create_variables_layout(self) -> QLayout:
        layout = QVBoxLayout()
        variables_label = QLabel("Variables")
        layout.addWidget(variables_label)
        self._variable_table = VariablesTable(self._controller)
        self._variable_table.view.setFixedWidth(280)
        layout.addWidget(self._variable_table.view)
        return layout

    def _create_report_layout(self):
        layout = QVBoxLayout()
        report_label = QLabel("Output report")
        layout.addWidget(report_label)
        self._report_view = OutputReportView()
        layout.addWidget(self._report_view.report_view)
        return layout

    def _configure_window(self, layout):
        self._window.setObjectName("Window")
        self._window.setStyleSheet(StyleSheet)
        self._window.setLayout(layout)
        self._window.resize(900, 600)
        self._window.setWindowTitle("ToyMathSolver")

    def set_solve_button_action(self, func: callable):
        self._solve_button.clicked.connect(func)

    def _bind_components_with_controller(self):
        self._controller.add_view_error_listeners(self.highlight)
        self._controller.add_view_error_listeners(self._report_view)
        self._controller.add_view_variable_listeners(self._variable_table)

    def show_window(self):
        self._window.show()
        sys.exit(self._app.exec_())
