import pytest

from solutions.day01 import part1, part2


# (()) and ()() both result in floor 0.
# ((( and (()(()( both result in floor 3.
# ))((((( also results in floor 3.
# ()) and ))( both result in floor -1 (the first basement level).
# ))) and )())()) both result in floor -3.


@pytest.mark.parametrize(
    "input,result",
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ],
)
def test_part1(input, result):
    assert result == part1(input)


@pytest.mark.parametrize(
    "input,result",
    [
        (")", 1),
        ("()())", 5),
    ],
)
def test_part2(input, result):
    assert result == part2(input)
