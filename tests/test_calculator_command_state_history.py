import pytest

from calculator_command_state_history.chain_calculator import ChainCalculator
from calculator_command_state_history.commands import (
    AddCommand,
    BatchCommand,
    DivideCommand,
    MultiplyCommand,
    SubtractCommand,
)
from calculator_command_state_history.controller import CalculatorController


class TestChainCalculator:
    @classmethod
    def setup_method(cls):
        cls.chain_calculator = ChainCalculator()
        cls.chain_calculator_initial_value = ChainCalculator(100)

        cls.chain_calculator_controller = CalculatorController(cls.chain_calculator)
        cls.chain_calculator_controller_initial_value = CalculatorController(
            cls.chain_calculator_initial_value
        )

    def test_initialize_total(self):
        assert self.chain_calculator.total == 0
        assert self.chain_calculator_initial_value.total == 100

    def test_addition(self):
        result = self.chain_calculator_controller.execute(
            AddCommand(100)
        ).calculator_total
        assert result == 100

    def test_addition_initial_value(self):
        result = self.chain_calculator_controller_initial_value.execute(
            AddCommand(100)
        ).calculator_total
        assert result == 200

    def test_subtraction(self):
        result = self.chain_calculator_controller.execute(
            SubtractCommand(100)
        ).calculator_total
        assert result == -100

    def test_subtraction_initial_value(self):
        result = self.chain_calculator_controller_initial_value.execute(
            SubtractCommand(100)
        ).calculator_total
        assert result == 0

    def test_multiplication(self):
        result = self.chain_calculator_controller.execute(
            MultiplyCommand(100)
        ).calculator_total
        assert result == 0

    def test_multiplication_inital_value(self):
        result = self.chain_calculator_controller_initial_value.execute(
            MultiplyCommand(100)
        ).calculator_total
        assert result == 10000

    def test_division(self):
        result = self.chain_calculator_controller.execute(
            DivideCommand(100)
        ).calculator_total
        assert result == 0

    def test_division_inital_value(self):
        result = self.chain_calculator_controller_initial_value.execute(
            DivideCommand(100)
        ).calculator_total
        assert result == 1

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.chain_calculator_controller_initial_value.execute(DivideCommand(0))

    def test_batch(self):
        result = self.chain_calculator_controller.execute(
            BatchCommand(
                [
                    AddCommand(100),
                    MultiplyCommand(2),
                    SubtractCommand(50),
                    DivideCommand(5),
                ]
            )
        ).calculator_total
        assert result == 30

    def test_batch_initial_value(self):
        result = self.chain_calculator_controller_initial_value.execute(
            BatchCommand(
                [
                    AddCommand(100),
                    MultiplyCommand(2),
                    SubtractCommand(50),
                    DivideCommand(5),
                ]
            )
        ).calculator_total
        assert result == 70


class TestChainCalculatorChaining:
    @classmethod
    def setup_method(cls):
        cls.chain_calculator = ChainCalculator()
        cls.chain_calculator_controller = CalculatorController(cls.chain_calculator)

    def test_chaining(self):
        result = (
            self.chain_calculator_controller.execute(AddCommand(100))
            .execute(MultiplyCommand(2))
            .execute(SubtractCommand(50))
            .execute(DivideCommand(5))
            .calculator_total
        )
        assert result == 30

    def test_chaining_undo_redo(self):
        result = (
            self.chain_calculator_controller.execute(AddCommand(100))
            .execute(MultiplyCommand(2))
            .execute(SubtractCommand(50))
            .execute(DivideCommand(5))
            .calculator_total
        )
        assert result == 30

        undo_result = (
            self.chain_calculator_controller.undo()
            .undo()
            .undo()
            .undo()
            .calculator_total
        )
        assert undo_result == 0

        redo_result = (
            self.chain_calculator_controller.redo()
            .redo()
            .redo()
            .redo()
            .calculator_total
        )
        assert redo_result == 30

    def test_batch_chaining(self):
        result = (
            self.chain_calculator_controller.execute(
                BatchCommand(
                    [
                        AddCommand(100),
                        MultiplyCommand(2),
                    ]
                )
            )
            .execute(
                BatchCommand(
                    [
                        SubtractCommand(50),
                        DivideCommand(5),
                    ]
                )
            )
            .calculator_total
        )
        assert result == 30


class TestChainCalculatorUndoRedo:
    @classmethod
    def setup_method(cls):
        cls.chain_calculator = ChainCalculator()
        cls.chain_calculator_initial_value = ChainCalculator(100)

        cls.chain_calculator_controller = CalculatorController(cls.chain_calculator)
        cls.chain_calculator_controller_initial_value = CalculatorController(
            cls.chain_calculator_initial_value
        )

    def test_addition_undo_redo(self):
        result = self.chain_calculator_controller.execute(
            AddCommand(100)
        ).calculator_total
        assert result == 100

        undo_result = self.chain_calculator_controller.undo().calculator_total
        assert undo_result == 0

        redo_result = self.chain_calculator_controller.redo().calculator_total
        assert redo_result == 100

    def test_subtraction_undo_redo(self):
        result = self.chain_calculator_controller.execute(
            SubtractCommand(100)
        ).calculator_total
        assert result == -100

        undo_result = self.chain_calculator_controller.undo().calculator_total
        assert undo_result == 0

        redo_result = self.chain_calculator_controller.redo().calculator_total
        assert redo_result == -100

    def test_multiplication_undo_redo(self):
        result = self.chain_calculator_controller_initial_value.execute(
            MultiplyCommand(2)
        ).calculator_total
        assert result == 200

        undo_result = (
            self.chain_calculator_controller_initial_value.undo().calculator_total
        )
        assert undo_result == 100

        redo_result = (
            self.chain_calculator_controller_initial_value.redo().calculator_total
        )
        assert redo_result == 200

    def test_division_undo_redo(self):
        result = self.chain_calculator_controller_initial_value.execute(
            DivideCommand(2)
        ).calculator_total
        assert result == 50

        undo_result = (
            self.chain_calculator_controller_initial_value.undo().calculator_total
        )
        assert undo_result == 100

        redo_result = (
            self.chain_calculator_controller_initial_value.redo().calculator_total
        )
        assert redo_result == 50

    def test_multiplication_by_zero_undo(self):
        """Can't undo and throws division by zero error! 😔"""
        self.chain_calculator_controller_initial_value.execute(MultiplyCommand(0))

        with pytest.raises(ZeroDivisionError):
            self.chain_calculator_controller_initial_value.undo()

    def test_batch_undo_redo(self):
        result = self.chain_calculator_controller.execute(
            BatchCommand(
                [
                    AddCommand(100),
                    MultiplyCommand(2),
                    SubtractCommand(50),
                    DivideCommand(5),
                ]
            )
        ).calculator_total
        assert result == 30

        result = self.chain_calculator_controller.undo().calculator_total
        assert result == 0

        result = self.chain_calculator_controller.redo().calculator_total
        assert result == 30
