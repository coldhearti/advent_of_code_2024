from day3_0 import mul_sum


def test_answer():
    assert (
        mul_sum("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
        == 2 * 4 + 5 * 5 + 11 * 8 + 8 * 5
    )
