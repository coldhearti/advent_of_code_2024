from typing import List

from utils import REF_FOLDER_PATH, get_file_lines

LINES = get_file_lines(REF_FOLDER_PATH.joinpath("2.input"))


def safety_predicate(levels: List[int]) -> bool:
    direction = levels[0] < levels[1]
    for i in range(len(levels) - 1):
        curr_level = levels[i]
        next_level = levels[i + 1]
        diff = abs(curr_level - next_level)
        step_predicate = 1 <= diff <= 3
        direction_predicate = (curr_level < next_level) == direction
        if not (direction_predicate and step_predicate):
            return False
    return True


def parse_levels() -> List[List[int]]:
    return [list(map(lambda val: int(val), line.split(" "))) for line in LINES]


def main():
    levels = parse_levels()
    return len(list(filter(safety_predicate, levels)))


if __name__ == "__main__":
    print(main())
