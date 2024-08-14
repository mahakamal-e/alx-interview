## Rotate 2D Matrix - 90 Degrees Clockwise

## Task Overview

The goal of this task is to rotate a given `n x n` 2D matrix 90 degrees clockwise, in place, meaning you should modify the original matrix without creating a new one.

### Requirements

- The matrix will have 2 dimensions (i.e., it will always be square).
- The matrix will not be empty.

### Prototype

```python
def rotate_2d_matrix(matrix):
    """
    Rotates the matrix 90 degrees clockwise in place.

    Args:
    matrix (list of list of int): The 2D matrix to rotate.

    Returns:
    None: The matrix is modified in place.
    """
### Approach
To rotate the matrix 90 degrees clockwise:

#### Transpose the Matrix:
Swap the rows with the columns. This is done by converting the rows into columns.
#### Reverse Each Row:
After transposing the matrix, reverse the order of elements in each row.
### Implementation Details
Transpose: Involves swapping matrix elements across the diagonal. The element at position [i][j] swaps with the element at position [j][i].
Reverse Each Row: Reverse the elements in each row of the transposed matrix.
