from typing import List

from day2_0 import base_safety_predicate, parse_levels, safety_predicate


def new_safety_predicate(levels: List[int]) -> bool:
    direction = levels[0] < levels[1]
    for i in range(len(levels) - 1):
        curr_level = levels[i]
        next_level = levels[i + 1]
        if not base_safety_predicate(
            curr_level,
            next_level,
            direction,
        ):
            if i > 0:
                new_levels = levels.copy()
                new_levels.pop(i - 1)
                if safety_predicate(new_levels):
                    return True

            new_levels = levels.copy()
            new_levels.pop(i + 1)
            if safety_predicate(new_levels):
                return True

            new_levels = levels.copy()
            new_levels.pop(i)
            return safety_predicate(new_levels)
    return True


def main():
    levels = parse_levels()
    return len(list(filter(new_safety_predicate, levels)))


if __name__ == "__main__":
    print(main())
