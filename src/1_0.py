from pathlib import Path
from typing import Tuple

from utils import get_file_lines

lines = get_file_lines(Path("ref/1.input"))


def parse_numbers(line: str) -> Tuple[int, int]:
    line = line.strip("\n")
    num1, num2 = line.split("   ", 1)
    return (int(num1), int(num2))


left: Tuple[int, ...]
right: Tuple[int, ...]
left, right = zip(*map(parse_numbers, lines))
left_sorted = sorted(left)
right_sorted = sorted(right)
diffs = [abs(l_val - r_val) for (l_val, r_val) in zip(left_sorted, right_sorted)]
print(sum(diffs))
