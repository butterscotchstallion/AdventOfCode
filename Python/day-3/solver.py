import logging
import re

logger = logging.getLogger(__name__)


def get_total_from_pairs(instructions: str) -> int:
    # pattern = re.compile(r"mul\((\d+,\d+)\)")
    pattern = re.compile(r"(do|don't)*mul\(\d+,\s*\d+\)")
    matches = pattern.findall(instructions)
    total = 0

    logger.debug(f"{len(matches)} matches: {matches}")

    for operands in matches:
        digits = operands.split(",")
        total += int(digits[0]) * int(digits[1])

    return total
