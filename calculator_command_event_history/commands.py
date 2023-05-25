from dataclasses import dataclass
from typing import List, Protocol

from calculator_command_event_history.chain_calculator import Calculator


class CalculatorCommand(Protocol):
    """general protocol for calculator command"""

    def execute(self, calculator: Calculator) -> float:
        pass


@dataclass
class AddCommand:
    value: float = 0.0

    def execute(self, calculator: Calculator) -> float:
        calculator.add(self.value)


@dataclass
class SubtractCommand:
    value: float = 0.0

    def execute(self, calculator: Calculator) -> float:
        calculator.subtract(self.value)


@dataclass
class MultiplyCommand:
    value: float = 0.0

    def execute(self, calculator: Calculator) -> float:
        calculator.multiply(self.value)


@dataclass
class DivideCommand:
    value: float = 0.0

    def execute(self, calculator: Calculator) -> float:
        calculator.divide(self.value)


@dataclass
class BatchCommand:
    commands: List[CalculatorCommand]

    def execute(self, calculator: Calculator) -> float:
        for command in self.commands:
            command.execute(calculator)
