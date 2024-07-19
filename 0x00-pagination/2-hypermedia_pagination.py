#!/usr/bin/env python3
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """eturn a tuple of size two containing a start index and end index"""
    return (page - 1) * page_size, page * page_size


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
        """Returns a list of `pages` lists"""
        assert (isinstance(page, int) and isinstance(page_size, int)
                and page > 0 and page_size > 0)
        start, end = index_range(page, page_size)
        self.dataset()
        length = len(self.dataset())
        if start >= length:
            return list()
        if end > length:
            end = length
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary of data with hypermedia values"""
        start, end = index_range(page, page_size)
        length = len(self.dataset())
        data = self.get_page(page, page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if end <= length else None,
            'prev_page': page - 1 if start != 0 else None,
            'total_pages': math.ceil(length / page_size)
        }
