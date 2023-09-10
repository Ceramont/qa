import pytest


@pytest.fixture()
def set_up():
    print("vhod")
    yield
    print("vihod")

@pytest.fixture(scope = "module")
def some():
    print("vhod1")
    yield
    print("vihod1")
