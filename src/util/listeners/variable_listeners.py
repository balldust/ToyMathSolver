from abc import ABC, abstractmethod


class CalculatedVariableObserver(ABC):
    @abstractmethod
    def update_variables(self):
        pass
