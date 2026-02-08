#!/usr/bin/env python3
"""
Measure the average execution time of the wait_n coroutine.
"""

import asyncio
import time
import importlib
from typing import Callable

wait_n = importlib.import_module("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average time taken to execute wait_n(n, max_delay).

    This function runs the wait_n coroutine n times and measures the total
    time taken. It returns the average time taken per task.

    Args:
        n (int): The number of tasks to run.
        max_delay (int): The maximum delay for each task.

    Returns:
        float: The average time taken per task.
    """
    start_time = time.time()  # Record the start time

    # Run the wait_n coroutine to measure execution time
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()  # Record the end time

    total_time = end_time - start_time
    return total_time / n
