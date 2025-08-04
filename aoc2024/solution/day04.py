from typing import Tuple
from collections import defaultdict
from collections.abc import Iterator


def coordinates(
    start_row: int, row: int, start_col: int, col: int
) -> Iterator[int, int]:
    for i in range(start_row, row):
        for j in range(start_col, col):
            yield (j, i)


def part1(space: dict[tuple[int, int], str], rows: int, cols: int) -> int:
    acc = 0

    for pt in coordinates(0, rows, 0, cols):
        acc += trace(space, pt)
    return acc


lines: list[list[Tuple[int, int]]] = [
    [(0, 0), (1, 1), (2, 2), (3, 3)],
    [(0, 0), (-1, 1), (-2, 2), (-3, 3)],
    [(0, 0), (1, -1), (2, -2), (3, -3)],
    [(0, 0), (-1, -1), (-2, -2), (-3, -3)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, -1), (0, -2), (0, -3)],
    [(0, 0), (-1, 0), (-2, 0), (-3, 0)],
]


def trace(space, pt):
    acc = 0
    for line in lines:
        pts = list((pt[0] + p[0], pt[1] + p[1]) for p in line)
        word = "".join([space[(x)] for x in pts])
        if word == "XMAS":
            acc += 1
    return acc


# M.S
# .A.
# M.S


diagonals = [
    [
        (0, 0),
        (1, 1),
        (2, 2),
    ],
    [
        (2, 0),
        (1, 1),
        (0, 2),
    ],
]


def search(space, pt):
    pts = [[(pt[0] + p[0], pt[1] + p[1]) for p in line] for line in diagonals]
    words = ["".join([space[(x)] for x in pts]) for pts in pts]
    return words.count("MAS") + words.count("SAM") == 2


def part2(space: dict[tuple[int, int], str], rows: int, cols: int) -> int:
    acc = 0
    for pt in coordinates(0, rows, 0, cols):
        acc += search(space, pt)
    return acc


def toSpaceHash(input: list[str]) -> dict[tuple[int, int], str]:
    result = defaultdict(str)
    i = 0
    j = 0
    for line in input:
        i = 0
        for c in line:
            result[(i, j)] = c
            i += 1
        j += 1
    return result


def main():
    with open("inputs/day4.txt") as f:
        lines = f.readlines()
        rows = len(lines)
        cols = len(lines[0])
    space = toSpaceHash(lines)
    print(f"Part 1: {part1(space, rows, cols)}")
    print(f"Part 2: {part2(space, rows, cols)}")


if __name__ == "__main__":
    main()
