""" Implement using Command Pattern with Undo/Redo via State """

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from calculator_command_state_history.chain_calculator import Calculator
from calculator_command_state_history.commands import CalculatorCommand


@dataclass
class CalculatorController:
    calculator: Calculator
    undo_list: List[CalculatorCommand] = field(default_factory=list)
    redo_list: List[CalculatorCommand] = field(default_factory=list)

    def execute(self, command: CalculatorCommand) -> CalculatorController:
        command.execute(self.calculator)
        self.undo_list.append(command)
        self.redo_list = []
        return self

    def undo(self) -> CalculatorController:
        if not self.undo_list:
            return self
        command = self.undo_list.pop()
        command.undo(self.calculator)
        self.redo_list.append(command)
        return self

    def redo(self) -> CalculatorController:
        if not self.redo_list:
            return self
        command = self.redo_list.pop()
        command.redo(self.calculator)
        self.undo_list.append(command)
        return self

    @property
    def calculator_total(self):
        return self.calculator.total
