from day2_1 import new_safety_predicate


def test_answer():
    assert new_safety_predicate([7, 6, 4, 2, 1])
    assert not new_safety_predicate([1, 2, 7, 8, 9])
    assert not new_safety_predicate([9, 7, 6, 2, 1])
    assert new_safety_predicate([1, 3, 2, 4, 5])
    assert new_safety_predicate([8, 6, 4, 4, 1])
    assert new_safety_predicate([1, 3, 6, 7, 9])


test_answer()
