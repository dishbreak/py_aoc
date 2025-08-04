from solution.day05 import is_valid_ordering, parse_rules, fix_ordering

import pytest


@pytest.fixture
def rule_lines():
    return [
        "47|53",
        "97|13",
        "97|61",
        "97|47",
        "75|29",
        "61|13",
        "75|53",
        "29|13",
        "97|29",
        "53|29",
        "61|53",
        "97|53",
        "61|29",
        "47|13",
        "75|47",
        "97|75",
        "47|61",
        "75|61",
        "47|29",
        "75|13",
        "53|13",
    ]


@pytest.fixture
def parsed_rules(rule_lines):
    return parse_rules(rule_lines)


@pytest.mark.parametrize(
    "ordering,result",
    [
        [
            [75, 47, 61, 53, 29],
            True,
        ],
        [
            [97, 61, 53, 29, 13],
            True,
        ],
        [
            [75, 29, 13],
            True,
        ],
        [
            [75, 97, 47, 61, 53],
            False,
        ],
        [
            [61, 13, 29],
            False,
        ],
        [
            [97, 13, 75, 29, 47],
            False,
        ],
    ],
)
def test_is_valid_order(parsed_rules, ordering, result):
    assert is_valid_ordering(parsed_rules, ordering) == result


@pytest.mark.parametrize(
    "ordering,result",
    [
        [[75, 97, 47, 61, 53], [97, 75, 47, 61, 53]],
        [[61, 13, 29], [61, 29, 13]],
        [[97, 13, 75, 29, 47], [97, 75, 47, 29, 13]],
    ],
)
def test_fix_ordering(parsed_rules, ordering, result):
    assert fix_ordering(parsed_rules, ordering) == result
