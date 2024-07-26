#!/usr/bin/python3
"""
Module to determine if a given data set represents a valid UTF-8 encoding.
"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    A valid UTF-8 encoding can have characters of lengths 1 to 4 bytes. This
    function checks if the given list of integers represents such a valid
    encoding. Each integer in the list represents a single byte of data.

    Args:
        data (List[int]): A list of integers, where each integer is a byte
                          (0 <= byte <= 255).

    Returns:
        bool: True if the data set represents a valid UTF-8 encoding,
        False otherwise.
    """
    remaining_bytes = 0

    for byte in data:
        binary_rep = format(byte, '#010b')[-8:]

        if remaining_bytes == 0:
            if binary_rep[0] == '0':
                continue
            elif binary_rep.startswith('110'):
                remaining_bytes = 1
            elif binary_rep.startswith('1110'):
                remaining_bytes = 2
            elif binary_rep.startswith('11110'):
                remaining_bytes = 3
            else:
                return False
        else:
            if not binary_rep.startswith('10'):
                return False
            remaining_bytes -= 1

    return remaining_bytes == 0
