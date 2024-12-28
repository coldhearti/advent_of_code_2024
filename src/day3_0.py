import re
from typing import List, Tuple

from utils import REF_FOLDER_PATH, get_file_lines

LINES = get_file_lines(REF_FOLDER_PATH.joinpath("3.input"))
COMMAND_STRING = "".join(LINES)
MUL_PATTERN = re.compile(r"mul\(([0-9]*),([0-9]*)\)")


def mul_values(command_string: str) -> List[Tuple[int, int]]:
    return list(map(lambda val: (int(val[0]), int(val[1])), MUL_PATTERN.findall(command_string)))


def do_mul(mul_values: List[Tuple[int, int]]) -> List[int]:
    return list(map(lambda val: val[0] * val[1], mul_values))


def mul_sum(command_string: str):
    mul_vals = mul_values(command_string)
    mul_res = do_mul(mul_vals)
    res = sum(mul_res)
    return res


def main():
    return mul_sum(COMMAND_STRING)


if __name__ == "__main__":
    print(main())
