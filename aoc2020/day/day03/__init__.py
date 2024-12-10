from logging import DEBUG, log
from pathlib import Path


class Slope:
    def __init__(self, lines: list[str]) -> None:
        self.__slope = parse_slope(lines)
        self.__cursor = (0, 0)
        self.__bottom = len(lines) - 1
        self.__width = len(lines[0])

    def move(self, vec: tuple[int, int]) -> None:
        log(DEBUG, "moving %s from %s", vec, self.__cursor)
        self.__cursor = add(self.__cursor, vec)
        self.__cursor = (self.__cursor[0] % self.__width, self.__cursor[1])
        log(DEBUG, "now at %s", self.__cursor)

    def at_tree(self) -> bool:
        log(DEBUG, "%s --> %s", self.__cursor, self.at_point(self.__cursor))
        return self.at_point(self.__cursor) == "#"

    def at_bottom(self) -> bool:
        return self.__cursor[1] >= self.__bottom

    def at_point(self, pt: tuple[int, int]) -> str:
        if pt not in self.__slope:
            return "."
        return self.__slope[pt]


def parse_slope(lines: list[str]) -> dict[tuple[int, int], str]:
    result: dict[tuple[int, int], str] = {}
    for j, line in enumerate(lines):
        for i, c in enumerate(line):
            result[(i, j)] = c
    return result


def add(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
    return (p1[0] + p2[0], p1[1] + p2[1])


def load_input() -> list[str]:
    with Path.open("inputs/day03.txt") as f:
        return list(f)


def part1(lines: list[str]) -> int:
    space = Slope(lines)
    acc = 0
    while not space.at_bottom():
        if space.at_tree():
            acc += 1
        space.move((3, 1))
    if space.at_tree():
        acc += 1
    return acc


def main() -> None:
    lines = load_input()
    print(f"Part 1: {part1(lines)}")
