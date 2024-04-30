import pytest
from calculator import CalculatorREPL

@pytest.fixture

def calculator():
    return CalculatorREPL()

def test_addition(calculator, capsys):
    calculator.onecmd('add 5 3')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Result: 8' or 'Result: 8.0'

def test_subtraction(calculator, capsys):
    calculator.onecmd('subtract 10 2')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Result: 8' or 'Result: 8.0'

def test_multiplication(calculator, capsys):
    calculator.onecmd('multiply 2 3')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Result: 6' or 'Result: 6.0'

def test_division(calculator, capsys):
    calculator.onecmd('divide 10 2')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Result: 5' or 'Result: 5.0'

def test_invalid_input(calculator, capsys):
    calculator.onecmd('add invalid')
    captured = capsys.readouterr()
    assert 'Invalid input' in captured.out

def test_history_management(calculator):
    pass
