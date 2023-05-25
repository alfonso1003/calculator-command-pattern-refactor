""" Implement using Command Pattern with Undo/Redo via State """

from __future__ import annotations

from typing import List

from calculator_command_event_history.chain_calculator import Calculator
from calculator_command_event_history.commands import CalculatorCommand


class ChainCalculatorController:
    def __init__(self, calculator: Calculator):
        self._calculator = calculator
        self._history: List[CalculatorCommand] = []
        self._current_idx: int = 0

    def register(self, command: CalculatorCommand) -> ChainCalculatorController:
        del self._history[self._current_idx :]
        self._history.append(command)
        self._current_idx += 1
        return self

    def undo(self) -> ChainCalculatorController:
        if self._current_idx:
            self._current_idx -= 1
        return self

    def redo(self) -> ChainCalculatorController:
        if self._current_idx < len(self._history):
            self._current_idx += 1
        return self

    @property
    def calculator_total(self):
        for command in self._history[: self._current_idx]:
            command.execute(self._calculator)
        return self._calculator.total
