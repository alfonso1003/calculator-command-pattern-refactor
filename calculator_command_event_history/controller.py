""" Implement using Command Pattern with Undo/Redo via Event History """

from __future__ import annotations

from typing import List

from calculator_command_event_history.chain_calculator import Calculator
from calculator_command_event_history.commands import CalculatorCommand


class CalculatorController:
    def __init__(self, calculator: Calculator):
        self._calculator = calculator
        self._history: List[CalculatorCommand] = []
        self._current_idx: int = 0

    def register(self, command: CalculatorCommand) -> CalculatorController:
        del self._history[self._current_idx :]
        self._history.append(command)
        self._current_idx += 1
        return self

    def undo(self) -> CalculatorController:
        if self._current_idx:
            self._current_idx -= 1
        return self

    def redo(self) -> CalculatorController:
        if self._current_idx < len(self._history):
            self._current_idx += 1
        return self

    @property
    def calculator_total(self):
        self._calculator.reset_total()
        for command in self._history[: self._current_idx]:
            command.execute(self._calculator)
        return self._calculator.total
