""" Naive implementation """


from __future__ import annotations

from abc import ABC, abstractmethod


class Calculator(ABC):
    def __init__(self, total: float = 0):
        self.total = total

    @abstractmethod
    def add(self, amount: str):
        pass

    @abstractmethod
    def subtract(self, amount: str):
        pass

    @abstractmethod
    def multiply(self, amount: str):
        pass

    @abstractmethod
    def divide(self, amount: str):
        pass


class ChainCalculator(Calculator):
    def add(self, amount: float) -> ChainCalculator:
        self.total += amount
        return self

    def subtract(self, amount: float) -> ChainCalculator:
        self.total -= amount
        return self

    def multiply(self, amount: float) -> ChainCalculator:
        self.total *= amount
        return self

    def divide(self, amount: float) -> ChainCalculator:
        self.total /= amount
        return self
