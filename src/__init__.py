import importlib
from pathlib import Path

import pytest


def main():
    pytest.main()

    row_format = " " * 1 + "│{:^7}│{:^8}│ {:<15} │"
    divisor = f"{" " * 1}┼{"─" * 7}┼{"─" * 8}┼{"─" * 17}┼"
    print("\n")
    print(divisor)
    print(row_format.format("Day", "Puzzle", "Answer"))
    print(divisor)
    for solution_module_path in Path(__file__).parent.glob("day*.py"):
        solution_name = solution_module_path.stem
        day = int(solution_name[3])
        puzzle = int(solution_name[-1]) + 1
        module = importlib.import_module(solution_name)
        row = row_format.format(day, puzzle, module.main())
        print(row)
        print(divisor)
    print("\n")


if __name__ == "__main__":
    main()
