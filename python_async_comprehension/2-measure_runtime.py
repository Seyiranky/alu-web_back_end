#!/usr/bin/env python3
"""
Measures runtime of async_comprehension executed in parallel.
"""

import asyncio
import time
import importlib

async_comprehension = importlib.import_module(
    "1-async_comprehension"
).async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel
    and measures the total runtime.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.perf_counter()

    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    end_time = time.perf_counter()

    total_time = end_time - start_time

    return total_time
