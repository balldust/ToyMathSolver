from abc import ABC, abstractmethod
from typing import Any


class PropertyFactory(ABC):
    @abstractmethod
    def named_property(self, name: str) -> Any:
        pass

    @abstractmethod
    def named_property_setter(self, name: str, value: Any) -> bool:
        pass


class NonSettablePropertyFactory(PropertyFactory):
    def __init__(self, name: str):
        self._name = name

    def named_property(self, name: str) -> Any:
        return self._name

    def named_property_setter(self, name: str, value: Any) -> bool:
        return False

