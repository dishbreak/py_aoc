from pathlib import Path
from collections import Counter
from functools import reduce
import operator


def main():
    input = parse_input()
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")


def part1(input: list[list[int]]) -> int:
    acc = 0
    for p in zip(sorted(input[0]), sorted(input[1])):
        acc += abs(p[0] - p[1])
    return acc


def part2(input: list[list[int]]) -> int:
    hist = Counter(input[0])
    scores = map(lambda a: a * hist[a], input[1])
    return reduce(operator.add, scores)


def parse_input() -> list[list[int]]:
    result = [[], []]
    with open(Path("inputs/day1.txt")) as f:
        for line in f:
            if line == "":
                continue
            pts = line.split("   ")
            result[0].append(int(pts[0]))
            result[1].append(int(pts[1]))
    return result


if __name__ == "__main__":
    main()
