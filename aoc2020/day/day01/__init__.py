
from pathlib import Path


def part1(inputs: list[int]) -> int:
    complements = { x: 2020 - x for x in inputs}
    for c in complements.values():
        if c in complements:
            return (2020-c)*c
    return 0

def part2(inputs: list[int]) -> int:
    for a in inputs:
        comps = {2020-a-x : x for x in inputs if a != x}
        for c in inputs:
            if a == c:
                continue
            if c in comps:
                return a*comps[c]*c
    return 0

def load_inputs() -> list[int]:
    with Path.open("inputs/day01.txt") as f:
        return [ int(line) for line in f]

def main() -> None:
    inputs = load_inputs()
    print(f"Part 1: {part1(inputs)}")
    print(f"Part 2: {part2(inputs)}")

if __name__ == "__main__":
    main()
