class Santa:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.pts = set()
        self.pts.add((0, 0))

    def move(self, c: str):
        if c == "^":
            self.y = self.y - 1
        if c == "v":
            self.y = self.y + 1
        if c == ">":
            self.x = self.x + 1
        if c == "<":
            self.x = self.x - 1
        self.pts.add((self.x, self.y))

    def houses_covered(self) -> int:
        return len(self.pts)


def part1(s: str) -> int:
    santa = Santa()

    for c in s:
        santa.move(c)

    return santa.houses_covered()


def part2(s: str) -> int:
    santas = [Santa(), Santa()]

    for i, c in enumerate(s):
        santas[i % 2].move(c)

    return len(santas[0].pts.union(santas[1].pts))


def main():
    with open("inputs/day03.txt", "r") as f:
        s = f.read()

    print(f"Part 1: {part1(s)}")
    print(f"Part 2: {part2(s)}")


if __name__ == "__main__":
    main()
