from itertools import pairwise
from collections.abc import Callable, Iterator


def main():
    with open("inputs/day2.txt") as f:
        lines = f.readlines()

    print(f"Part 1:{part1(lines)}")
    print(f"Part 2:{part2(lines)}")


def all_pairs_are(f: Callable[[int, int], bool], input: list[int]) -> bool:
    return all(f(x, y) for x, y in pairwise(input))


def all_but_one_pair_are(f: Callable[[int, int], bool], input: list[int]) -> bool:
    i = iter(pairwise(input))
    return any(not f(x, y) for x, y in i) and not any(not f(x, y) for x, y in i)


def all_but_at_most_one_pair(f: Callable[[int, int], bool], input: list[int]) -> bool:
    return all_pairs_are(f, input) or all_but_one_pair_are(f, input)


def increasing(x: int, y: int) -> bool:
    return x < y


def decreasing(x: int, y: int) -> bool:
    return x > y


def no_big_jumps(x: int, y: int) -> bool:
    return abs(x - y) <= 3


def is_safe_report(vals: list[int]) -> bool:
    return (
        all_pairs_are(increasing, vals) or all_pairs_are(decreasing, vals)
    ) and all_pairs_are(no_big_jumps, vals)


def is_safe_enough_report(vals: list[int]) -> bool:
    return is_safe_report(vals) or any(is_safe_report(r) for r in sublists(vals))


def sublists(input: list[int]) -> Iterator[list[int]]:
    for i in range(len(input)):
        n = input.copy()
        n.pop(i)
        yield (n)


def part1(input: list[str]) -> int:
    acc = 0
    for report in input:
        vals = list(map(int, report.split(" ")))
        acc += 1 if is_safe_report(vals) else 0
    return acc


def part2(input: list[str]) -> int:
    acc = 0
    for report in input:
        vals = list(map(int, report.split(" ")))
        acc += 1 if is_safe_enough_report(vals) else 0
    return acc


if __name__ == "__main__":
    main()
