import itertools
from collections.abc import Iterator
import graphlib


def parse_rules(rules: list[str]) -> dict[int, list[int]]:
    parsed_vals = [[int(val) for val in rule.split("|")] for rule in rules]
    parsed_vals = sorted(parsed_vals, key=lambda x: x[1])
    return {
        k: [n[0] for n in v] for k, v in itertools.groupby(parsed_vals, lambda x: x[1])
    }


def part1(rule_lines: list[str], orderings: list[list[int]]) -> int:
    rules = parse_rules(rule_lines)
    return sum(
        ordering[len(ordering) // 2]
        for ordering in orderings
        if is_valid_ordering(rules, ordering)
    )


def is_valid_ordering(rules: dict[int, list[int]], ordering: list[int]) -> bool:
    # only pick rules with both pages in the ordering
    active_rules = {
        k: [n for n in v if n in ordering] for k, v in rules.items() if k in ordering
    }
    active_rules = {k: v for k, v in active_rules.items() if len(v) > 0}

    v = list(reversed(ordering))
    for i, val in enumerate(v):
        if val not in active_rules:
            continue
        if i == len(v) - 1:
            return True
        if val not in rules:
            return False
        if any(x not in v[i + 1 :] for x in active_rules[val]):
            return False
    return True


def fix_ordering(rules: dict[int, list[int]], ordering: list[int]) -> bool:
    # only pick rules with both pages in the ordering
    active_rules = {
        k: [n for n in v if n in ordering] for k, v in rules.items() if k in ordering
    }
    active_rules = {k: v for k, v in active_rules.items() if len(v) > 0}
    return list(graphlib.TopologicalSorter(active_rules).static_order())


def part2(rule_lines: list[str], orderings: list[list[int]]) -> int:
    rules = parse_rules(rule_lines)
    bad_orderings = [x for x in orderings if not is_valid_ordering(rules, x)]
    return sum(
        fix_ordering(rules, ordering)[len(ordering) // 2] for ordering in bad_orderings
    )


def main():
    with open("inputs/day5.txt") as f:
        c = f.read()

    c = c.strip()
    rules, orderings = c.split("\n\n")
    rules = rules.split("\n")
    orderings = [
        [int(x) for x in ordering.split(",")] for ordering in orderings.split("\n")
    ]

    print(f"Part 1: {part1(rules, orderings)}")
    print(f"Part 2: {part2(rules, orderings)}")


if __name__ == "__main__":
    main()
