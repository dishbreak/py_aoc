import pytest

from solutions.day02 import get_bow_length, get_wrapping_paper


@pytest.mark.parametrize(
    "input,result",
    [
        ("2x3x4", 58),
        ("1x1x10", 43),
    ],
)
def test_get_wrapping_paper(input: str, result: int):
    assert result == get_wrapping_paper(input)


@pytest.mark.parametrize(
    "input,result",
    [
        ("2x3x4", 34),
        ("1x1x10", 14),
    ],
)
def test_get_bow_length(input: str, result: int):
    assert result == get_bow_length(input)
