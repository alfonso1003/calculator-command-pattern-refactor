""" Naive implementation """

from __future__ import annotations


# Implemented as a class
class ChainCalculator:
    def __init__(self, total: float = 0):
        self.total = total

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
