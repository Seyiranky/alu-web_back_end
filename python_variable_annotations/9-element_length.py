#!/usr/bin/env python3
"""
This script defines a type-annotated function element_length that calculates
the length of elements in an iterable of sequences.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each element in an iterable of sequences.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, containing a sequence
        and its length.
    """
    return [(i, len(i)) for i in lst]
