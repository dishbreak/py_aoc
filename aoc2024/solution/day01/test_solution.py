from solution import part2


def test_part2():
    left = [3, 4, 2, 1, 3, 3]
    right = [4, 3, 5, 3, 9, 3]
    assert 31 == part2([left, right])
