from pathlib import Path


class Solver:
    """
    - Pair up the smallest number in the left list with the smallest number in the right list
    - then the second-smallest left number with the second-smallest right number, and so on.
    - Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances.
    """

    def read_input(self) -> list[list[int]]:
        lines = Path("input.txt").read_text().splitlines()
        rows: list[list[int]] = []
        for line in lines:
            line_parts: list[str] = line.split()
            assert len(line_parts) == 2, f"Unexpected parts length: {len(line_parts)}"

            cols = [int(float(n)) for n in line_parts]
            rows.append(cols)
        return rows

    def get_cols_sorted(self, rows: list, col: int) -> list[int]:
        return sorted([r[col] for r in rows])

    def solve(self):
        rows = self.read_input()
        col_1 = self.get_cols_sorted(rows, 0)
        col_2 = self.get_cols_sorted(rows, 1)

        distances = []
        counter = 0
        for left in col_1:
            right = col_2[counter]
            distance = abs(left - right)
            distances.append(distance)
            counter = counter + 1

        answer = sum(distances)

        return answer
