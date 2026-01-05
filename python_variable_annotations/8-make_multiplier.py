#!/usr/bin/env python3
"""
This script defines a type-annotated function make_multiplier that returns
a function to multiply a float by a given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the specified multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that returns the product of
        the float and the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplies the given value by the multiplier.

        Args:
            value (float): The value to be multiplied.

        Returns:
            float: The product of the value and the multiplier.
        """
        return value * multiplier

    return multiplier_function
