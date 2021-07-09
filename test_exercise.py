from exercise import findPlayers
import pytest 
import unittest.mock
from unittest.mock import patch

@patch('builtins.input', lambda *args: '139')
def test_findPlayers_input_mocking_base_case(capsys):
    findPlayers()
    out,err=capsys.readouterr()
    assert out == '-Nate Robinson\tMike Wilks\n-Nate Robinson\tBrevin Knight\n'

@patch('builtins.input', lambda *args: '0')
def test_findPlayers_input_mocking_zero_case(capsys):
    findPlayers()
    out,err=capsys.readouterr()
    assert out == 'No matches found\n'

@patch('builtins.input', lambda *args: 'abc')
def test_findPlayers_input_mocking_negative_case(capsys):
    findPlayers()
    out,err=capsys.readouterr()
    assert out == 'You are supposed to enter positive number.\n'
    
@patch('builtins.input', lambda *args: 'abc')
def test_findPlayers_input_mocking_string_case(capsys):
    findPlayers()
    out,err=capsys.readouterr()
    assert out == 'You are supposed to enter positive number.\n'    
