import pytest

from calculator_naive import ChainCalculator


class TestChainCalculator:
    @classmethod
    def setup_method(cls):
        cls.chain_calculator = ChainCalculator()
        cls.chain_calculator_initial_value = ChainCalculator(100)

    def test_initialize_total(self):
        assert self.chain_calculator.total == 0
        assert self.chain_calculator_initial_value.total == 100

    def test_addition(self):
        result = self.chain_calculator.add(100).total
        assert result == 100

        result = self.chain_calculator_initial_value.add(100).total
        assert result == 200

    def test_subtraction(self):
        result = self.chain_calculator.subtract(100).total
        assert result == -100

        result = self.chain_calculator_initial_value.subtract(100).total
        assert result == 0

    def test_multiplication(self):
        calculator = ChainCalculator(2)
        result = calculator.multiply(100).total
        assert result == 200

        result = self.chain_calculator_initial_value.multiply(100).total
        assert result == 10000

    def test_division(self):
        calculator = ChainCalculator(1)
        result = calculator.divide(5).total
        assert result == 0.2

        result = self.chain_calculator_initial_value.divide(100).total
        assert result == 1

    def test_division_by_zero(self):
        calculator = ChainCalculator(1)

        with pytest.raises(ZeroDivisionError):
            calculator.divide(0)


class TestChainCalculatorChaining:
    @classmethod
    def setup_method(cls):
        cls.chain_calculator = ChainCalculator()

    def test_chaining(self):
        result = self.chain_calculator.add(100).multiply(2).subtract(50).divide(5).total
        assert result == 30
