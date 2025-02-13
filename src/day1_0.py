from typing import List, Tuple

from utils import REF_FOLDER_PATH, get_file_lines

LINES = get_file_lines(REF_FOLDER_PATH.joinpath("1.input"))


def parse_numbers(line: str) -> Tuple[int, int]:
    line = line.strip("\n")
    num1, num2 = line.split("   ", 1)
    return (int(num1), int(num2))


def sorted_number_lists() -> Tuple[List[int], List[int]]:
    left: Tuple[int, ...]
    right: Tuple[int, ...]
    left, right = zip(*map(parse_numbers, LINES))
    left_sorted = sorted(left)
    right_sorted = sorted(right)
    return left_sorted, right_sorted


def main() -> int:
    left_sorted, right_sorted = sorted_number_lists()
    diffs = [abs(l_val - r_val) for (l_val, r_val) in zip(left_sorted, right_sorted)]
    return sum(diffs)


if __name__ == "__main__":
    print(main())
