from dataclasses import dataclass
from typing import List, Protocol

from calculator_command_event_history.chain_calculator import Calculator


class CalculatorCommand(Protocol):
    """general protocol for calculator command"""

    def execute(self, calculator: Calculator) -> None:
        pass


@dataclass
class AddCommand:
    value: float = 0.0

    def execute(self, calculator: Calculator) -> None:
        calculator.add(self.value)


@dataclass
class SubtractCommand:
    value: float = 0.0

    def execute(self, calculator: Calculator) -> None:
        calculator.subtract(self.value)


@dataclass
class MultiplyCommand:
    value: float = 0.0

    def execute(self, calculator: Calculator) -> None:
        calculator.multiply(self.value)


@dataclass
class DivideCommand:
    value: float = 0.0

    def execute(self, calculator: Calculator) -> None:
        calculator.divide(self.value)


@dataclass
class BatchCommand:
    commands: List[CalculatorCommand]

    def execute(self, calculator: Calculator) -> None:
        for command in self.commands:
            command.execute(calculator)
