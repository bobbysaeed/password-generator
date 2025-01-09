from abc import ABC, abstractmethod
class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass
