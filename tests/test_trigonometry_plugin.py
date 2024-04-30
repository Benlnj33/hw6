# tests/test_trigonometry_plugin.py
import pytest
from unittest.mock import MagicMock
from plugins.Trigonometry import TrigonometryPlugin

@pytest.fixture

def trigonometry_plugin():
    return TrigonometryPlugin()

def test_sin(trigonometry_plugin, capsys):
    # Mock the behavior of the sin function
    trigonometry_plugin.sin = MagicMock(return_value=0.5)
    trigonometry_plugin.sin('30')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Result: 0.5'

def test_cos(trigonometry_plugin, capsys):
    # Mock the behavior of the cos function
    trigonometry_plugin.cos = MagicMock(return_value=0.866)
    trigonometry_plugin.cos('30')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Result: 0.866'

def test_tan(trigonometry_plugin, capsys):
    # Mock the behavior of the tan function
    trigonometry_plugin.tan = MagicMock(return_value=0.577)
    trigonometry_plugin.tan('30')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Result: 0.577'