import hashlib


def form_hash(seed: str, num: int) -> str:
    input = f"{seed}{num}"
    return hashlib.md5(input.encode()).hexdigest()


def part1(seed: str) -> int:
    i = 1
    while True:
        hash = form_hash(seed, i)
        if hash.startswith("00000"):
            return i
        i = i + 1


def part2(seed: str) -> int:
    i = 1
    while True:
        hash = form_hash(seed, i)
        if hash.startswith("000000"):
            return i
        i = i + 1


def main():
    with open("inputs/day04.txt") as f:
        seed = f.read().strip()

    print(f"Part 1: {part1(seed)}")
    print(f"Part 2: {part2(seed)}")


if __name__ == "__main__":
    main()
