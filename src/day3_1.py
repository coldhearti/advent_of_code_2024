import re
from typing import List, Tuple

from day3_0 import COMMAND_STRING, MUL_PATTERN, do_mul

DO_NOT_PATTERN = re.compile(r"don't\(\)")
DO_PATTERN = re.compile(r"do\(\)")


def new_mul_sum(command_string: str):
    muls: List[Tuple[int, int, int]] = []
    do_starts: List[int] = []
    dont_starts: List[int] = []
    for mul_match in MUL_PATTERN.finditer(command_string):
        mul_head = mul_match.start()
        val1 = mul_match.group(1)
        val2 = mul_match.group(2)
        muls.append((mul_head, int(val1), int(val2)))
    for do in DO_PATTERN.finditer(command_string):
        do_starts.append(do.start())
    for dont in DO_NOT_PATTERN.finditer(command_string):
        dont_starts.append(dont.start())
    do_head = do_starts[0]
    dont_head = dont_starts[0]
    do_muls: List[Tuple[int, int]] = []
    for mul in muls:
        mul_head, mul1, mul2 = mul
        while True:
            do_head = do_starts[0]
            if len(do_starts) == 1:
                break
            if do_starts[1] > mul_head:
                break
            do_starts.pop(0)
        while True:
            dont_head = dont_starts[0]
            if len(dont_starts) == 1:
                break
            if dont_starts[1] > mul_head:
                break
            dont_starts.pop(0)
        if do_head > mul_head and dont_head > mul_head:
            do_muls.append((mul1, mul2))
        elif dont_head > mul_head:
            do_muls.append((mul1, mul2))
        elif dont_head < mul_head and do_head < mul_head and do_head > dont_head:
            do_muls.append((mul1, mul2))

    return sum(do_mul(do_muls))


def main():
    return new_mul_sum(COMMAND_STRING)


if __name__ == "__main__":
    print(main())
