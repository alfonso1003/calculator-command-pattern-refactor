from dataclasses import dataclass
from typing import List, Protocol

from calculator_command_event_history.chain_calculator import Calculator


class CalculatorCommand(Protocol):
    """general protocol for calculator command"""

    def execute(self, current_value: float) -> float:
        pass

    def undo(self, current_value: float) -> float:
        pass

    def redo(self, current_value: float) -> float:
        pass


@dataclass
class AddCommand:
    value: float = 0.0

    def execute(self, calculator: Calculator) -> float:
        calculator.add(self.value)

    def undo(self, calculator: Calculator) -> float:
        calculator.subtract(self.value)

    def redo(self, calculator) -> float:
        calculator.add(self.value)


@dataclass
class SubtractCommand:
    value: float = 0.0

    def execute(self, calculator: Calculator) -> float:
        calculator.subtract(self.value)

    def undo(self, calculator: Calculator) -> float:
        calculator.add(self.value)

    def redo(self, calculator: Calculator) -> float:
        calculator.subtract(self.value)


@dataclass
class MultiplyCommand:
    value: float = 0.0

    def execute(self, calculator: Calculator) -> float:
        calculator.multiply(self.value)

    def undo(self, calculator: Calculator) -> float:
        calculator.divide(self.value)

    def redo(self, calculator: Calculator) -> float:
        calculator.multiply(self.value)


@dataclass
class DivideCommand:
    value: float = 0.0

    def execute(self, calculator: Calculator) -> float:
        calculator.divide(self.value)

    def undo(self, calculator: Calculator) -> float:
        calculator.multiply(self.value)

    def redo(self, calculator: Calculator) -> float:
        calculator.divide(self.value)


@dataclass
class BatchCommand:
    commands: List[CalculatorCommand]

    def execute(self, current_value: float) -> float:
        for command in self.commands:
            current_value = command.execute(current_value)
        return current_value

    def undo(self, current_value: float) -> float:
        for command in reversed(self.commands):
            current_value = command.undo(current_value)
        return current_value

    def redo(self, current_value: float) -> float:
        for command in self.commands:
            current_value = command.redo(current_value)
        return current_value
