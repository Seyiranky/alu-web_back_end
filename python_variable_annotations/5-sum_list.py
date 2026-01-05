#!/usr/bin/env python3
"""
This script defines a function to sum up a list of floating-point numbers.

Functions:
    sum_list(input_list): Returns the sum of all elements in a list of floats.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Computes the sum of all elements in a list of floating-point numbers.

    Args:
        input_list (List[float]): A list of floating-point numbers to sum.

    Returns:
        float: The sum of all elements in the input list.
    """
    float_sum = sum(input_list)
    return float_sum
