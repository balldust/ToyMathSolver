import typing

from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTreeView,
    QLayout,
    QAbstractItemView,
)
from PyQt5.QtCore import Qt, QModelIndex

from src.execution.problem_execution import ProblemExecution
from src.image_utils import image_utils
from src.util.controllers.settings_view_controller import SettingsViewController

StyleSheet = """
QWidget#Window {
    background-color: black;
}

QTreeView {
    color: white;
    background-color: gray;
    selection-background-color: gray; 
}

"
"""


class SettingsWindow:
    def __init__(self, model: ProblemExecution):
        self._window = QWidget()
        self._controller = SettingsViewController(model)
        self._window.setWindowModality(Qt.ApplicationModal)
        layout = self._create_window_layout()
        window_icon = image_utils.create_qicon_from_filename(
            "settings_button.png"
        )
        self._window.setWindowIcon(window_icon)
        self._window.setLayout(layout)
        self._window.setWindowTitle("Settings")
        self._window.resize(600, 300)
        self._window.setStyleSheet(StyleSheet)

    def _create_window_layout(self) -> QLayout:
        layout = QVBoxLayout()
        self._settings_view = SettingsView(self._controller)
        layout.addWidget(self._settings_view.view)
        return layout

    def show_window(self):
        self._window.show()


class SettingsView:
    def __init__(self, controller: SettingsViewController):
        self._view = QTreeView()
        self._view.setHeaderHidden(True)
        model = SettingsViewModel(self._view, controller)
        self._view.setModel(model)
        self._view.header().resizeSection(0, 300)
        self._view.header().resizeSection(1, 300)
        self._view.header().resizeSection(2, 300)

    @property
    def view(self) -> QWidget:
        return self._view


class SettingsViewModel(QtCore.QAbstractItemModel):
    def __init__(
        self,
        view: QAbstractItemView,
        controller: SettingsViewController,
        parent=None,
    ):
        super(SettingsViewModel, self).__init__(parent)
        self._controller = controller
        self._root = self._controller.get_settings_specifications()
        self._view = view

    def columnCount(self, index=QtCore.QModelIndex()):
        if index.isValid():
            return index.internalPointer().column_count()
        return self._root.column_count()

    def rowCount(self, index=QtCore.QModelIndex()):
        if index.row() > 0:
            return 0
        if index.isValid():
            item = index.internalPointer()
            return item.children_count()
        item = self._root
        return item.children_count()

    def index(self, row, column, index=QtCore.QModelIndex()):
        if not index or not index.isValid():
            parent = self._root
        else:
            parent = index.internalPointer()

        if not QtCore.QAbstractItemModel.hasIndex(self, row, column, index):
            return QtCore.QModelIndex()

        child = parent.child(row)
        if child:
            return QtCore.QAbstractItemModel.createIndex(
                self, row, column, child
            )
        else:
            return QtCore.QModelIndex()

    def parent(self, index):
        if index.isValid():
            p = index.internalPointer().parent
            if p:
                return QtCore.QAbstractItemModel.createIndex(
                    self, p.row(), 0, p
                )
        return QtCore.QModelIndex()

    def hasChildren(self, index):
        if not index.isValid():
            item = self._root
        else:
            item = index.internalPointer()
        return item.has_children()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid() and role == QtCore.Qt.DisplayRole:
            value = index.internalPointer().data(index.column())
            if isinstance(value, QWidget):
                self._view.setIndexWidget(index, value)
            return index.internalPointer().data(index.column())
        return None

    def setData(
        self, index: QModelIndex, value: typing.Any, role: int = ...
    ) -> bool:
        return index.internalPointer().set_data(index.column(), value)

    def flags(self, index):
        if index.column() == 1:
            return (
                QtCore.Qt.ItemIsEditable
                | QtCore.Qt.ItemIsSelectable
                | QtCore.Qt.ItemIsEnabled
            )
        else:
            return QtCore.Qt.ItemIsSelectable
