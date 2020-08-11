import pytest

def pytest_addoption(parser):
    parser.addoption('--test-dir', action='store')
    parser.addoption('--interface', action='store')
    parser.addoption("--pypath", dest="pypath", action="append")
