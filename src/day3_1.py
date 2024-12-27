import re
from typing import List, Tuple

from day3_0 import COMMAND_STRING, MUL_PATTERN, do_mul

DO_NOT_PATTERN = re.compile(r"don't\(\)")
DO_PATTERN = re.compile(r"do\(\)")


def new_mul_sum(command_string: str):
    muls = parse_mul_heads_vals(command_string)
    do_heads = parse_do_heads(command_string)
    dont_heads = parse_dont_heads(command_string)
    doable_muls = compute_doable_muls(
        muls,
        do_heads,
        dont_heads,
    )
    return sum(do_mul(doable_muls))


def compute_doable_muls(muls, do_heads, dont_heads) -> List[Tuple[int, int]]:
    do_head = do_heads[0]
    dont_head = dont_heads[0]
    doable_muls: List[Tuple[int, int]] = []
    for mul in muls:
        mul_head, mul1, mul2 = mul
        while True:
            do_head = do_heads[0]
            if len(do_heads) == 1:
                break
            if do_heads[1] > mul_head:
                break
            do_heads.pop(0)
        while True:
            dont_head = dont_heads[0]
            if len(dont_heads) == 1:
                break
            if dont_heads[1] > mul_head:
                break
            dont_heads.pop(0)
        if do_head > mul_head and dont_head > mul_head:
            doable_muls.append((mul1, mul2))
        elif dont_head > mul_head:
            doable_muls.append((mul1, mul2))
        elif dont_head < mul_head and do_head < mul_head and do_head > dont_head:
            doable_muls.append((mul1, mul2))
    return doable_muls


def parse_do_heads(command_string):
    do_heads: List[int] = []
    for do in DO_PATTERN.finditer(command_string):
        do_heads.append(do.start())
    return do_heads


def parse_dont_heads(command_string):
    dont_heads: List[int] = []
    for dont in DO_NOT_PATTERN.finditer(command_string):
        dont_heads.append(dont.start())
    return dont_heads


def parse_mul_heads_vals(command_string: str) -> List[Tuple[int, int, int]]:
    muls: List[Tuple[int, int, int]] = []
    for mul_match in MUL_PATTERN.finditer(command_string):
        mul_head = mul_match.start()
        val1 = mul_match.group(1)
        val2 = mul_match.group(2)
        muls.append((mul_head, int(val1), int(val2)))
    return muls


def main():
    return new_mul_sum(COMMAND_STRING)


if __name__ == "__main__":
    print(main())
