import logging
from pathlib import Path

from solver import get_total_from_pairs

logger = logging.getLogger(__name__)


def test_solver_example():
    example_input = (
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    )
    actual = get_total_from_pairs(example_input)

    assert actual == 161


def test_solver_example_2():
    example_input = (
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    )
    actual = get_total_from_pairs(example_input)

    assert actual == 48


def test_solver():
    instructions = Path("input.txt").read_text().splitlines()
    total = 0
    for instruction in instructions:
        total += get_total_from_pairs(instruction)

    logger.info(f"Total: {total}")
