#!/usr/bin/python3
""" Rotate 2D Matrix Module """


def rotate_2d_matrix(matrix):
    """Rotated the given n x x 2d matrix 90 degree"""
    n = len(matrix)
    transposed = zip(*matrix)
    reverse_rows = [list(row)[::-1] for row in transposed]
    matrix[:] = reversed_rows
