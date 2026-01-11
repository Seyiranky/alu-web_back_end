#!/usr/bin/env python3
"""
Function to create a task for wait_random coroutine.
"""

import asyncio
import importlib

wait_random = importlib.import_module("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task that wraps the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay to be passed to the
        wait_random coroutine.

    Returns:
        asyncio.Task: A task that runs the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
