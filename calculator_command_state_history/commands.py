from dataclasses import dataclass
from typing import List, Protocol

from calculator_command_state_history.chain_calculator import Calculator


class CalculatorCommand(Protocol):
    """general protocol for calculator command"""

    def execute(self, calculator: Calculator) -> None:
        pass

    def undo(self, calculator: Calculator) -> None:
        pass

    def redo(self, calculator: Calculator) -> None:
        pass


@dataclass
class AddCommand:
    value: float = 0.0

    def execute(self, calculator: Calculator) -> None:
        calculator.add(self.value)

    def undo(self, calculator: Calculator) -> None:
        calculator.subtract(self.value)

    def redo(self, calculator: Calculator) -> None:
        calculator.add(self.value)


@dataclass
class SubtractCommand:
    value: float = 0.0

    def execute(self, calculator: Calculator) -> None:
        calculator.subtract(self.value)

    def undo(self, calculator: Calculator) -> None:
        calculator.add(self.value)

    def redo(self, calculator: Calculator) -> None:
        calculator.subtract(self.value)


@dataclass
class MultiplyCommand:
    value: float = 0.0

    def execute(self, calculator: Calculator) -> None:
        calculator.multiply(self.value)

    def undo(self, calculator: Calculator) -> None:
        calculator.divide(self.value)

    def redo(self, calculator: Calculator) -> None:
        calculator.multiply(self.value)


@dataclass
class DivideCommand:
    value: float = 0.0

    def execute(self, calculator: Calculator) -> None:
        calculator.divide(self.value)

    def undo(self, calculator: Calculator) -> None:
        calculator.multiply(self.value)

    def redo(self, calculator: Calculator) -> None:
        calculator.divide(self.value)


@dataclass
class BatchCommand:
    commands: List[CalculatorCommand]

    def execute(self, calculator: Calculator) -> None:
        for command in self.commands:
            command.execute(calculator)

    def undo(self, calculator: Calculator) -> None:
        for command in reversed(self.commands):
            command.undo(calculator)

    def redo(self, calculator: Calculator) -> None:
        for command in self.commands:
            command.redo(calculator)
