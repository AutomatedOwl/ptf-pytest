import pytest

def pytest_addoption(parser):
    parser.addoption('--test-dir', action='store')
    parser.addoption('--interface', action='store')
