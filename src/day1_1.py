from typing import Dict

from day1_0 import sorted_number_lists


def main():
    left_sorted, right_sorted = sorted_number_lists()
    val_frequencies: Dict[int, int] = {}

    val = right_sorted[0]
    freq = val_frequencies.setdefault(val, val)
    for right_val in right_sorted[1:]:
        if right_val == val:
            freq += val
        else:
            val_frequencies[val] = freq
            val = right_val
            freq = val_frequencies.setdefault(val, val)
    freq_sum = 0
    for left_val in left_sorted:
        if left_val in val_frequencies:
            freq_sum += val_frequencies[left_val]
    return freq_sum


if __name__ == "__main__":
    print(main())
