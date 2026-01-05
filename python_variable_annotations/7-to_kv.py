#!/usr/bin/env python3
"""
This script defines a type-annotated function to_kv that returns a tuple
containing a string and the square of a numeric value.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple where the first element is the string `k`,
    and the second element is the square of the numeric value `v`.

    Args:
        k (str): A string value.
        v (Union[int, float]): A numeric value that can be an int or a float.

    Returns:
        Tuple[str, float]: A tuple containing a string and a float.
    """
    return k, float(v**2)
