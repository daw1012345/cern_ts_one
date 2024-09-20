import string
from collections import Counter

from tsa_one.duplicate import detect_duplicates


def test_assignment_example():
    inpt = ["b", "a", "c", "c", "e", "a", "c", "d", "c", "d"]
    expected = ["a", "c", "d"]

    assert detect_duplicates(inpt) == expected


def test_ensure_nonduplicates_dne():
    inpt = ["a", "b", "c", "b", "d", "d"]
    ocrs = Counter(inpt)

    result = detect_duplicates(inpt)

    for element, cnt in ocrs.items():
        if cnt > 1:
            continue
        assert element not in result


def test_no_duplicates_in_result():
    inpt = ["a", "a", "a", "a", "a", "b", "b", "b", "c", "c"]
    result = detect_duplicates(inpt)

    assert len(set(result)) == len(result)


def test_order():
    inpt = ["y", "x", "y", "x", "a", "a", "b", "b"]
    expected = ["y", "x", "a", "b"]

    assert detect_duplicates(inpt) == expected


def test_empty_list():
    input = []
    expected = []

    assert detect_duplicates(input) == expected


def test_no_duplicates():
    inpt = list(string.ascii_lowercase)
    expected = []

    assert detect_duplicates(inpt) == expected
