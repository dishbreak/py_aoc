from pathlib import Path
from typing import Callable


def get_policy(string_def: str) -> Callable[[str], bool]:
    pts = string_def.split(" ")
    ranges = pts[0].split("-")
    min_val = int(ranges[0])
    max_val = int(ranges[1])
    target_char = pts[1][0]

    def policy(password: str) -> bool:
        ct = 0
        for c in password:
            if c == target_char:
                ct = ct + 1
        return ct >= min_val and ct <= max_val

    return policy

def get_policy_v2(string_def: str) -> Callable[[str], bool]:
    pts = string_def.split(" ")
    pos = [int (x)-1 for x in pts[0].split("-")]
    target_char = pts[1][0]

    def check_pos(pw: str, pos: int) -> bool:
        try:
            return pw[pos] == target_char
        except IndexError:
            return False

    def policy(password: str) -> bool:
        if pos[1] >= len(password):
            return False
        pos0 = check_pos(password, pos[0])
        pos1 = check_pos(password, pos[1])
        return (pos0 or pos1) and not (pos0 and pos1)

    return policy

def check_line(
        line: str,
        policy_factory: Callable[[str], Callable[[str], bool]]) -> bool:
    pts = line.split(": ")
    policy = policy_factory(pts[0])
    password = pts[1]
    return policy(password)

def load_input() -> list[str]:
    with Path.open("inputs/day02.txt") as f:
        return list(f)

def part1(lines: list[str]) -> int:
    acc = 0
    for line in lines:
        if check_line(line, get_policy):
            acc += 1
    return acc

def part2(lines: list[str]) -> int:
    acc = 0
    for line in lines:
        if check_line(line, get_policy_v2):
            acc += 1
    return acc


def main() -> None:
    lines = load_input()
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")

if __name__ == "__main__":
    main()
