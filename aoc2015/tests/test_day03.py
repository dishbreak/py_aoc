import pytest

from solutions.day03 import part1, part2


@pytest.mark.parametrize(
    "input,result",
    [
        (">", 2),
        ("^>v<", 4),
        ("^v^v^v^v^v", 2),
    ],
)
def test_part1(input, result):
    assert part1(input) == result


@pytest.mark.parametrize(
    "input,result",
    [
        ("^v", 3),
        ("^>v<", 3),
        ("^v^v^v^v^v", 11),
    ],
)
def test_part2(input, result):
    assert part2(input) == result
