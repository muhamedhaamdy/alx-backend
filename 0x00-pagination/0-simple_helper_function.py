#!/usr/bin/env python3
'''Simple helper function'''


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns the start and end index for a given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end index for the given page.

    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
