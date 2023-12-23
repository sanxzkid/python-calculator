# calculator_project/tests/test_calculator.py
from calculator.calculator import Calculator

def test_add():
    calc = Calculator()
    result = calc.add(3, 7)
    assert result == 10

def test_subtract():
    calc = Calculator()
    result = calc.subtract(10, 5)
    assert result == 5

def test_multiply():
    calc = Calculator()
    result = calc.multiply(2, 4)
    assert result == 8

def test_divide():
    calc = Calculator()
    result = calc.divide(10, 2)
    assert result == 5

def test_divide_by_zero():
    calc = Calculator()
    try:
        calc.divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
    else:
        assert False, "Expected ValueError, but no exception was raised"
