#!/usr/bin/env python3
"""
Simple helper function for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of start and end index for pagination."""
    assert isinstance(page, int) and isinstance(page_size, int)
    assert page > 0 and page_size > 0

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
