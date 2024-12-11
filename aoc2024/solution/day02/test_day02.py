import pytest
from day02 import is_safe_report, is_safe_enough_report


@pytest.mark.parametrize(
    "report,result",
    [
        ["7 6 4 2 1", True],
        ["1 2 7 8 9", False],
        ["9 7 6 2 1", False],
        ["1 3 2 4 5", False],
        ["8 6 4 4 1", False],
        ["1 3 6 7 9", True],
    ],
)
def test_is_safe_report(report, result):
    vals = list(map(int, report.split(" ")))
    assert result == is_safe_report(vals)


@pytest.mark.parametrize(
    "report,result",
    [
        ["7 6 4 2 1", True],
        ["1 2 7 8 9", False],
        ["9 7 6 2 1", False],
        ["1 3 2 4 5", True],
        ["8 6 4 4 1", True],
        ["1 3 6 7 9", True],
    ],
)
def test_is_safe_enough_report(report, result):
    vals = list(map(int, report.split(" ")))
    assert result == is_safe_enough_report(vals)
