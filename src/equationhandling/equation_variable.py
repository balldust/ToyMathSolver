from abc import ABC, abstractmethod


class EquationVariable(ABC):
    def __init__(self, name: str):
        if not name or type(name) is not str:
            raise TypeError("Name must be of type string.")

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()

    def __ne__(self, other):
        return self.name.lower() != other.name.lower()

    def __hash__(self):
        return hash(self.name.lower())

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def value(self) -> float:
        pass

    @value.setter
    @abstractmethod
    def value(self, value: float):
        pass


class CalculatedVariable(EquationVariable):
    _default_value = 0.5

    def __init__(self, name: str):
        super().__init__(name)
        self._name = name
        self._initial_value = CalculatedVariable._default_value
        self._value = CalculatedVariable._default_value

    @property
    def name(self):
        return self._name

    @property
    def initial_value(self):
        return self._initial_value

    @initial_value.setter
    def initial_value(self, value: float):
        self._initial_value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: float):
        self._value = value


class AssignedVariable(EquationVariable):
    def __init__(self, name: str):
        super().__init__(name)
        self._name = name
        self._value = None

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: float):
        if self._value:
            raise Exception("Cannot change value when value has already been assigned")
        else:
            self._value = value
