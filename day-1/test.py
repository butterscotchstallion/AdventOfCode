import pytest

from solve import Solver

solver = Solver()


@pytest.fixture(autouse=True, scope="session")
def input_fixture() -> list[list[int]]:
    rows = solver.read_input()
    assert len(rows) == 1000
    return rows


def test_solve():
    answer = solver.solve()
    print(f"\nanswer is {answer}")


def test_get_similarity_score(input_fixture: list[list[int]]):
    # rows = solver.read_input("example.txt")
    rows = solver.read_input()
    similarity_score = solver.get_similarity_score(rows)
    # assert similarity_score == 31
    print(f"similarity_score is {similarity_score}")
