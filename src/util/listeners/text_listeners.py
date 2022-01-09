from abc import ABC, abstractmethod


class TextListener(ABC):
    @abstractmethod
    def handle_text(self, text: str):
        pass

