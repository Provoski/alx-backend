#!/usr/bin/env python3
"""0-simple_helper_function module"""


def index_range(page: int, page_size: int) -> tuple:
    """
    index_range:
        takes two integer arguments page and page_size
    args:
        page - number of pages
        page_size - size ot pages
    return:
        return a tuple of size two containing a start index
        and an end index corresponding to the range of
        indexes to return in a list for those particular
        pagination parameters
    """
    current_index_tracker = 0
    previous_index_tracker = 0
    page_num_tracker = 0

    for page_num_tracker in range(0, page):
        previous_index_tracker = current_index_tracker
        for size_per_page in range(0, page_size):
            current_index_tracker += 1
    return (previous_index_tracker, current_index_tracker)
