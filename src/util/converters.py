from abc import ABC, abstractmethod
from typing import Any, TypeVar

from src.util.validators import IntegerValidator, FloatValidator

T = TypeVar("T")


class Converter(ABC):
    @abstractmethod
    def convert(self, value: Any) -> T:
        pass


class IntegerValueConverter(Converter):
    def convert(self, value: Any) -> int:
        validator = IntegerValidator()
        if validator.validate(value):
            return int(value)


class FloatValueConverter(Converter):
    def convert(self, value: Any) -> float:
        validator = FloatValidator()
        if validator.validate(value):
            return float(value)
