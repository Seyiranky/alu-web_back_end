#!/usr/bin/env python3
"""
This script defines a function to compute the floor of a floating-point number.

Functions:
    floor(n): Returns the largest integer less than or equal to the set number.
"""

import math


def floor(n: float) -> int:
    """
    Computes the floor of a floating-point number.

    Args:
        n (float): The number to compute the floor of.

    Returns:
        float: The largest integer less than or equal to the given number.
    """
    return math.floor(n)
