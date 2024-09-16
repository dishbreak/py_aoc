
import pytest

from day.day02 import get_policy, get_policy_v2, part1, part2


@pytest.mark.parametrize(("password", "expected"), [
    ("a", True),
    ("aa", True),
    ("aaaa", False),
    ("abbbbbbbbb", True),
])
def test_get_policy(password: str, expected: bool) -> None:  # noqa: FBT001
    policy = get_policy("1-3 a")
    assert policy(password) == expected


@pytest.mark.parametrize(("password", "expected"), [
    ("a", False),
    ("aa", False),
    ("aaaa", False),
    ("cccccc", False),
    ("aacaabbb", True),
    ("bbabbbbbbb", True),
])
def test_get_policy_v2(password: str, expected: bool) -> None:  # noqa: FBT001
    policy = get_policy_v2("1-3 a")
    assert policy(password) == expected

@pytest.fixture
def example_data() -> list[str]:
    return [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
    ]

def test_part1(example_data: list[str]) -> None:
    assert part1(example_data) == 2

def test_part2(example_data: list[str]) -> None:
    assert part2(example_data) == 1
