from solve import Solver


def test_solve():
    solver = Solver()
    rows = solver.read_input()
    assert len(rows) == 1000

    answer = solver.solve()
    print(f"\nanswer is {answer}")
