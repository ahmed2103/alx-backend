#!/usr/bin/env python3
"""Module to paginate iterable to pages then return the start and end index"""


def index_range(page, page_size):
    """Return a tuple of size two containing a start index and end index"""
    return (page - 1) * page_size, page * page_size
