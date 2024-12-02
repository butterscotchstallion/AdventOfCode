from solver import is_safe


def test_is_safe():
    # Safe because the levels are all decreasing by 1 or 2.
    assert is_safe([7, 6, 4, 2, 1])
    # Unsafe because 2 7 is an increase of 5.
    assert not is_safe([1, 2, 7, 8, 9])
    # Unsafe because 2 7 is an increase of 5.
    assert not is_safe([9, 7, 6, 2, 1])
    # Unsafe because 1 3 is increasing but 3 2 is decreasing.
    assert not is_safe([1, 3, 2, 4, 5])
    # Unsafe because 4 4 is neither an increase or a decrease.
    assert not is_safe([8, 6, 4, 4, 1])
    # Safe because the levels are all increasing by 1, 2, or 3.
    assert is_safe([1, 3, 6, 7, 9])
