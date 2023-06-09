from abc import ABC, abstractmethod


class Calculator(ABC):
    def __init__(self, total: float = 0):
        self.total = total
        self._inital_total = total

    @abstractmethod
    def add(self, amount: float) -> None:
        pass

    @abstractmethod
    def subtract(self, amount: float) -> None:
        pass

    @abstractmethod
    def multiply(self, amount: float) -> None:
        pass

    @abstractmethod
    def divide(self, amount: float) -> None:
        pass

    @abstractmethod
    def reset_total(self) -> None:
        pass


class ChainCalculator(Calculator):
    def add(self, amount: float) -> None:
        self.total += amount

    def subtract(self, amount: float) -> None:
        self.total -= amount

    def multiply(self, amount: float) -> None:
        self.total *= amount

    def divide(self, amount: float) -> None:
        self.total /= amount

    def reset_total(self) -> None:
        self.total = self._inital_total
