#!/usr/bin/env python3
"""
This script uses Union to create a list containing two different data types.
"""

from typing import List, Union

# Define a type that allows both floats and ints
ElementType = Union[int, float]


def sum_mixed_list(mxd_lst: List[ElementType]) -> float:
    """
    Computes the sum of integers and floating-point numbers.

    Args:
        mxd_list : A list of integers and floating-point numbers to sum.

    Returns:
        float: The sum of all elements in the mixed list.
    """
    sum_list = sum(mxd_lst)
    return sum_list
