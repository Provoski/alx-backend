#!/usr/bin/env python3
"""1-simple_pagination module"""
import csv
import math
from typing import List, Tuple, Dict, Union


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
    current_index_tracker: int = 0
    previous_index_tracker: int = 0
    page_num_tracker: int = 0

    for page_num_tracker in range(0, page):
        previous_index_tracker = current_index_tracker
        for size_per_page in range(0, page_size):
            current_index_tracker += 1
    return (previous_index_tracker, current_index_tracker)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """create pagination according to page and page_size"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data: List[List] = self.dataset()
        start_index: int = 0
        end_index: int = 0
        page_list: List[List]

        start_index, end_index = index_range(page, page_size)
        page_list = data[start_index:end_index]

        return page_list

    def get_hyper(
            self, page: int = 1,
            page_size: int = 10) -> Dict[str, Union[int, str]]:
        """returns dictionary with extra information about a page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        page_dict: Dict[str, Union[int, str]] = {}
        data: List[List] = self.get_page(page, page_size)
        total_pages: int = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        page_dict["page_size"] = len(data)
        page_dict["page"] = page
        page_dict["data"] = self.get_page(page, page_size)
        page_dict["next_page"] = next_page
        page_dict["prev_page"] = prev_page
        page_dict["total_pages"] = total_pages

        return page_dict
