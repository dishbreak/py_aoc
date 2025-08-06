import pytest

from solutions.day04 import part1


@pytest.mark.parametrize("input,result", [("abcdef", 609043), ("pqrstuv", 1048970)])
def test_part1(input, result):
    assert result == part1(input)
