import re

mul = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

mul_with_disable = re.compile(r"(mul\((?P<first_factor>\d{1,3}),(?P<second_factor>\d{1,3})\))|(do\(\))|(don't\(\))")


def main():
    with open("inputs/day3.txt") as f:
        contents = f.read()
    print(f"Part 1: {part1(contents)}")
    print(f"Part 2: {part2(contents)}")


def part1(input: str) -> int:
    acc = 0
    for f in mul.finditer(input):
        acc += int(f.group(1)) * int(f.group(2))
    return acc


def part2(input: str) -> int:
    acc = 0
    enabled = True
    for f in mul_with_disable.finditer(input):
        match f.group():
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _:
                if enabled:
                    d = f.groupdict()
                    acc += int(d['first_factor']) * int(d['second_factor'])
    return acc


if __name__ == "__main__":
    main()
