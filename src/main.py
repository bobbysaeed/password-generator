import random
import string
from abc import ABC, abstractmethod
from typing import List, Optional

import nltk

nltk.download('words')


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


class MemorablePasswordGenerator(PasswordGenerator):
    """
    Class to generate a memorable password.
    """
    def __init__(
        self,
        no_of_words: int = 5,
        separator: str = "-",
        capitalization: bool = False,
        vocabulary: Optional[List[str]] = None
    ):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()

        self.no_of_words: int = no_of_words
        self.separator: str = separator
        self.capitalization: bool = capitalization
        self.vocabulary: List[str] = vocabulary

    def generate(self):
        """Generate a password using the specified vocabulary and separator."""
        selected_words = random.sample(self.vocabulary, self.no_of_words)
        if self.capitalization:
            selected_words = [word.capitalize() for word in selected_words]
        return self.separator.join(selected_words)
