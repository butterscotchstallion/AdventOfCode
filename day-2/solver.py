def is_safe(levels: list[int]) -> bool:
    c = 0
    num_levels = len(levels)
    max_diff = 3
    min_diff = 1
    is_increasing = False
    is_decreasing = False
    for level in levels:
        if c + 1 < num_levels:
            next_level = levels[c + 1]
            diff = abs(level - next_level)
            min_diff_failed = diff < min_diff
            max_diff_failed = diff > max_diff
            if min_diff_failed or max_diff_failed:
                print(
                    f"diff is {diff}, min_diff_failed {min_diff_failed}, max_diff_failed {max_diff_failed}"
                )
                return False
        c += 1

    return True
