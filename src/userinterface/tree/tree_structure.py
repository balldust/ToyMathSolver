from __future__ import annotations

from typing import Any

from src.util.factories.property_factory import PropertyFactory


class TreeItem:
    def __init__(self, name: str, property_factory: PropertyFactory):
        self._name = name
        self._property_factory = property_factory

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        if self._property_factory:
            return self._property_factory.named_property(self._name)

    def set_value(self, new_value: Any) -> bool:
        if self._property_factory:
            return self._property_factory.named_property_setter(
                self._name, new_value
            )
        return False


class TreeNode:
    def __init__(self, item: TreeItem = None, parent: TreeNode = None):
        self._parent = parent
        self._item = item
        self._children = []

    def data(self, column: int):
        if column == 0:
            return self._item.name
        return self._item.value

    def set_data(self, column: int, value: Any) -> bool:
        if column == 1:
            return self._item.set_value(value)
        return False

    def append_child(self, group: TreeItem):
        self._children.append(TreeNode(group, self))

    def child(self, row) -> TreeNode:
        return self._children[row]

    def children_count(self):
        return len(self._children)

    def has_children(self):
        return len(self._children) > 0

    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        return 0

    @staticmethod
    def column_count():
        return 2

    @property
    def children(self) -> list[Any]:
        return self._children

    @property
    def parent(self):
        return self._parent
