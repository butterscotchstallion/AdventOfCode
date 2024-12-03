from pathlib import Path


def is_safe(levels: list[int]) -> bool:
    num_levels = len(levels)
    max_diff = 3
    min_diff = 1
    num_increases = 0
    num_decreases = 0
    for c, level in enumerate(levels):
        if c + 1 < num_levels:
            next_level = levels[c + 1]
            diff = abs(level - next_level)
            min_diff_failed = diff < min_diff
            max_diff_failed = diff > max_diff
            if min_diff_failed or max_diff_failed:
                """
                print(
                    f"diff is {diff}, min_diff_failed {min_diff_failed}, max_diff_failed {max_diff_failed}"
                )
                """
                return False

            if c > 0:
                if level > levels[c - 1]:
                    num_increases += 1
                else:
                    num_decreases += 1

                is_decreasing = level < levels[c - 1]
                is_increasing = level > levels[c - 1]
                if is_increasing and num_decreases > 0:
                    return False
                if is_decreasing and num_increases > 0:
                    return False

                # No change
                is_last_level = c == num_levels - 1
                if is_last_level and num_decreases == 0 and num_increases == 0:
                    return False

    # Results in 0
    all_increasing = num_increases == num_levels
    all_decreasing = num_decreases == num_levels

    if all_increasing or all_decreasing:
        return True

    # Account for some increases and no decreases
    if num_increases > 0 and num_decreases == 0:
        return True

    # Account for some decreases and no increases
    if num_decreases > 0 and num_increases == 0:
        return True

    return False


def get_safe_reports_count() -> int:
    reports = Path("input.txt").read_text().splitlines()
    assert len(reports) == 1000, "Unexpected number of reports"
    num_safe_reports = 0

    for report in reports:
        levels = [int(l) for l in report.split()]
        if is_safe(levels):
            num_safe_reports += 1

    return num_safe_reports
