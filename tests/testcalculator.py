
import pytest
from calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


class TestClass:

    def test_addition(self, calculator):
        assert 7 == calculator.addition(3, 4)

    def test_substract(self, calculator):
        assert -1 == calculator.substraction(3, 4)

    def test_multiplication(self, calculator):
        assert 12 == calculator.multiplication(3, 4)

    def test_division(self, calculator):
        assert 2 == calculator.division(4, 2)
