def parse(s: str):
    pts = s.split("x")
    return [int(p) for p in pts]


def get_wrapping_paper(s: str) -> int:
    dims = parse(s)
    length, width, height = dims[0], dims[1], dims[2]
    sides = [length * width, length * height, width * height]
    slack = min(sides)
    return 2 * sum(sides) + slack


def get_bow_length(s: str) -> int:
    dims = parse(s)
    dims = sorted(dims)
    vol = dims[0] * dims[1] * dims[2]
    return 2 * (dims[0] + dims[1]) + vol


def part1(s: list[str]) -> int:
    acc = 0
    for line in s:
        acc = acc + get_wrapping_paper(line)
    return acc


def part2(s: list[str]) -> int:
    acc = 0
    for line in s:
        acc = acc + get_bow_length(line)
    return acc


def main():
    with open("inputs/day02.txt", "r") as f:
        s = f.readlines()

    print(f"Part 1: {part1(s)}")
    print(f"Part 2: {part2(s)}")


if __name__ == "__main__":
    main()
