from PyQt5.QtWidgets import QTableView, QWidget
from PyQt5 import QtCore

from src.util.controllers.main_view_controller import MainViewController
from src.util.listeners.variable_listeners import CalculatedVariableObserver


class VariablesTable(CalculatedVariableObserver):
    def __init__(self, controller: MainViewController):
        self._view = QTableView()
        model = VariablesTableModel(controller)
        self._view.setModel(model)
        self._view.horizontalHeader().setStretchLastSection(True)
        self._view.verticalHeader().setVisible(True)
        self._view.horizontalScrollBar().setVisible(False)

    def update_variables(self):
        model = self._view.model()
        model.beginResetModel()
        self._view.setModel(model)
        model.endResetModel()

    @property
    def view(self) -> QWidget:
        return self._view


class VariablesTableModel(QtCore.QAbstractTableModel):
    def __init__(self, controller: MainViewController):
        super(VariablesTableModel, self).__init__()
        self._controller = controller
        self._horizontal_headers = ['Initial value', 'Final value']

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._horizontal_headers[section]
            except (IndexError,):
                return QtCore.QVariant()
        elif orientation == QtCore.Qt.Vertical:
            try:
                if self._controller:
                    return self._controller.get_calculated_variables()[section].name
                else:
                    return QtCore.QVariant()
            except (IndexError,):
                return QtCore.QVariant()

    def flags(self, index):
        if index.column() == 0:
            return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
        else:
            return QtCore.Qt.ItemIsSelectable

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            if self._controller:
                calculated_vars = self._controller.get_calculated_variables()
                var = calculated_vars[index.row()]
                return var.initial_value if index.column() == 0 else var.value
            return QtCore.QVariant()
        return QtCore.QVariant()

    def rowCount(self, index):
        if self._controller:
            return len(self._controller.get_calculated_variables())
        return 0

    def columnCount(self, index):
        return len(self._horizontal_headers)

    def setData(self, index, value, role):
        if index.isValid():
            if isinstance(value, str) and value.isnumeric():
                var_name = self.headerData(index.row(), QtCore.Qt.Vertical)
                self._controller.set_variable_initial_value(var_name, float(value))
                return True
            else:
                return False
        return True
