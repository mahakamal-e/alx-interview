#!/usr/bin/python3
"""
Module that defines a validUTF8 function.
"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): A list of integers representing the data set.
                          Each integer represents 1 byte of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    remaining_bytes = 0

    for byte in data:
        if remaining_bytes == 0:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 0b110:
                remaining_bytes = 1
            elif byte >> 4 == 0b1110:
                remaining_bytes = 2
            elif byte >> 3 == 0b11110:
                remaining_bytes = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            remaining_bytes -= 1

    return remaining_bytes == 0
