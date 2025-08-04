def part1(s):
    level = 0
    for c in s:
        if c == "(":
            level = level + 1
        elif c == ")":
            level = level - 1
    return level


def part2(s):
    level = 0
    for i, c in enumerate(s):
        if c == "(":
            level = level + 1
        if c == ")":
            level = level - 1
        if level == -1:
            return i + 1
    return -1


def main():
    s = ""
    with open("inputs/day01.txt", "r") as f:
        s = f.read().strip()
    print(f"Part 1: {part1(s)}")
    print(f"Part 2: {part2(s)}")


if __name__ == "__main__":
    main()
