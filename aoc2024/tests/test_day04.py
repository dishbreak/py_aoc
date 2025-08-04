import pytest

from solution.day04 import toSpaceHash, part1, part2


@pytest.fixture
def space_hash():
    lines = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]
    return toSpaceHash(lines)


def test_part1(space_hash):
    assert 18 == part1(space_hash, 10, 10)


def test_part2(space_hash):
    assert 9 == part2(space_hash, 10, 10)
