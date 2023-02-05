from abc import ABC, abstractmethod
from typing import Any


class Validator(ABC):
    @abstractmethod
    def validate(self, value: Any) -> bool:
        pass


class IntegerValidator(Validator):
    def validate(self, value: Any) -> bool:
        return isinstance(value, int) or (
            isinstance(value, str) and value.isdigit()
        )


class FloatValidator(Validator):
    def validate(self, value: Any) -> bool:
        if isinstance(value, float):
            return True
        elif isinstance(value, str):
            try:
                float(value)
                return True
            except ValueError:
                return False
        return False
