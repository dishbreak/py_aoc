import pytest

from day.day01.main import part1, part2


@pytest.fixture
def example_data() -> list[int]:
    return [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]


def test_part1(example_data: list[int]) -> None:
    assert part1(example_data) == 514579

def test_part2(example_data: list[int]) -> None:
    assert part2(example_data) == 241861950
