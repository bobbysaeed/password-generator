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


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, symbols, digits, chars, length: int = 10):
        self.length = length
        self.symbols = string.punctuation
        self.digits = string.digits
        self.chars = string.ascii_letters

    def generate(self):
        collection_of_parameters = self.digits + self.chars + self.symbols
        return ''.join(random.choice(collection_of_parameters) for _ in range(self.length))