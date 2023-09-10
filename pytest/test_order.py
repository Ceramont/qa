import pytest


@pytest.mark.run(order=5)
def test_method1():
    print("Метод 1")

@pytest.mark.run(order=1)
def test_method2():
    print("Метод 2")

@pytest.mark.run(order=2)
def test_method3():
    print("Метод 3")

@pytest.mark.run(order=3)
def test_method4():
    print("Метод 4")

@pytest.mark.run(order=4)
def test_method5():
    print("Метод 5")

@pytest.mark.run(order=6)
def test_method6():
    print("Метод 6")
