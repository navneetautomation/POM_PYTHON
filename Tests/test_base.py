import pytest
from Tests import conftest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass