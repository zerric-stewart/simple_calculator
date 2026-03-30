import pytest
from src.calculator.calculator import (
    squareNums,
    triNums,
    lazyCaterer,
    magicSquares,
    cubeNums,
    factorialNums,
    pentagonalNums,
)


@pytest.mark.parametrize("n, expected", [
    (2, 4),
    (5, 25),
    (10, 100),
])
def test_squareNums(n, expected):
    assert squareNums(n) == expected


@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (4, 10),
    (7, 28),
])
def test_triNums(n, expected):
    assert triNums(n) == expected


@pytest.mark.parametrize("n, expected", [
    (1, 2),
    (2, 4),
    (5, 16),
])
def test_lazyCaterer(n, expected):
    assert lazyCaterer(n) == expected


@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 5),
    (3, 15),
])
def test_magicSquares(n, expected):
    assert magicSquares(n) == expected


@pytest.mark.parametrize("n, expected", [
    (2, 8),
    (3, 27),
    (4, 64),
])
def test_cubeNums(n, expected):
    assert cubeNums(n) == expected


@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (4, 24),
    (5, 120),
])
def test_factorialNums(n, expected):
    assert factorialNums(n) == expected


@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 5),
    (3, 12),
])
def test_pentagonalNums(n, expected):
    assert pentagonalNums(n) == expected
