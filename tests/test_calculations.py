import pytest
from app.calculator.calculator import Calculator
from app.calculation.calculation import CalculationFactory


def test_calculator_calculate_add():
    calc = Calculator()
    result = calc.calculate(2, 3, "add")
    assert result == 5


def test_calculator_history():
    calc = Calculator()
    calc.calculate(2, 3, "add")
    history = calc.get_history()
    assert len(history) == 1
    assert history[0][3] == 5

def test_invalid_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create_calculation(1, 2, "invalid")    