import random
import string
from abc import ABC, abstractmethod

class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinCodeGenerator(PasswordGenerator):
    """
    Class to generate a numeric pin code.
    """
    def __init__(self, length: int = 6):
        self.length: int = length

    def generate(self) -> str:
        """
        Generate a numeric pin code.
        """
        return ''.join(random.choice(string.digits) for _ in range(self.length))