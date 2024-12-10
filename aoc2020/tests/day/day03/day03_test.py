import pytest

from day.day03 import Slope, part1


@pytest.fixture
def example_data() -> list[str]:
    return [
        # 000000000001
        # 012345678901
        "..##.......",  # 0
        "#...#...#..",  # 1
        ".#....#..#.",  # 2
        "..#.#...#.#",  # 3
        ".#...##..#.",  # 4
        "..#.##.....",  # 5
        ".#.#.#....#",  # 6
        ".#........#",  # 7
        "#.##...#...",  # 8
        "#...##....#",  # 9
        ".#..#...#.#",  # 10
    ]


def test_parse_slope(example_data: list[str]) -> None:
    slope = Slope(example_data)
    assert slope.at_point((-1, -1)) == "."
    assert slope.at_point((6, 2)) == "#"
    assert slope.at_point((0, 3)) == "."
    assert slope.at_point((5, 6)) == "#"


@pytest.mark.parametrize(
    ("move_vec", "result"),
    [
        ((-1, -1), False),
        ((2, 0), True),
        ((0, 3), False),
        ((5, 5), True),
    ],
)
def test_at_tree(
    move_vec: tuple[int, int],
    result: bool,  # noqa: FBT001
    example_data: list[str],
) -> None:
    slope = Slope(example_data)
    slope.move(move_vec)
    assert slope.at_tree() == result


def test_part1(example_data: list[str]) -> None:
    assert part1(example_data) == 7
