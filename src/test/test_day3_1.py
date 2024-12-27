from day3_0 import main as old_main
from day3_1 import main, new_mul_sum


def test_answer():
    assert (
        new_mul_sum(
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
        )
        == 2 * 4 + 8 * 5
    )
    assert main() <= old_main()


test_answer()
