from itertools import pairwise


def main():
    with open("inputs/day2.txt") as f:
        lines = f.readlines()

    print(f"Part 1:{part1(lines)}")


def is_monotonically_decreasing(input: list[int]) -> bool:
    return all(x > y for x, y in pairwise(input))


def is_monotonically_increasing(input: list[int]) -> bool:
    return all(x < y for x, y in pairwise(input))


def is_monotonic(input: list[int]) -> bool:
    return is_monotonically_decreasing(input) or is_monotonically_increasing(input)


def no_big_jumps(input: list[int]) -> bool:
    r = [abs(x - y) < 3 for x, y in pairwise(input)]
    return all(abs(x - y) <= 3 for x, y in pairwise(input))


def is_safe_report(report: str) -> bool:
    vals = list(map(int, report.split(" ")))
    return is_monotonic(vals) and no_big_jumps(vals)


def part1(input: list[str]) -> int:
    acc = 0
    for report in input:
        acc += 1 if is_safe_report(report) else 0
    return acc


if __name__ == "__main__":
    main()
