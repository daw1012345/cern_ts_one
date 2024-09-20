#!/usr/bin/env python3
from collections import Counter
from typing import Hashable, List


def detect_duplicates(inpt: List[Hashable]) -> List[Hashable]:
    """Given a list of objects, returns a list that contains only those that are duplicated,
      in the order that they appeared for the first time in the original list.

    Arguments:
        inpt -- A list of `Hashable` items parse

    Returns:
        List[Hashable]: A list that contains only items that are duplicated,
         in the order that they appeared for the first time in the original list.
    """
    occurrences = Counter(inpt)

    # count == 0 -> item DNE, count == 1 -> only one occurrence
    output = [element for element, count in occurrences.items() if count > 1]
    # Very important note: since python3.7, Counter explicitly remembers insertion order
    # https://docs.python.org/3/library/collections.html#counter-objects

    return output
