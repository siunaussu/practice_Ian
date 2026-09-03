# conftest.py
import pytest


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "ydc: marks tests as ydc to run"
    )
    config.addinivalue_line(
        "python_functions", "ydc_*"
    )

def pytest_collection_modifyitems(config, items):
    # Example rule: skip tests marked "slow" unless --run-slow is passed
    if config.getoption("--run-ydc"):
        return
    skip_ydc = pytest.mark.skip(reason="need --run-ydc option to run")
    for item in items:
        if "ydc" in item.keywords:
            item.add_marker(skip_ydc)

def pytest_addoption(parser):
    parser.addoption(
        "--run-ydc", action="store_true", default=False, help="run ydc tests"
    )