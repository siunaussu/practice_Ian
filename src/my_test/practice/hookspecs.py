import pytest


class MyHookSpec:
    @pytest.hookspec
    def pytest_ydc_test_found(self, item):
        """Called when a ydc-marked test is found."""
        pass
