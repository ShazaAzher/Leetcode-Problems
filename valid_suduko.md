## Sudoku Validator

This repository contains a Python solution to determine if a 9 x 9 Sudoku board is valid based on the following criteria:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

### Problem Statement

Given a 9 x 9 Sudoku board, validate the board based on the rules mentioned above. The board is considered valid if all the filled cells follow these rules. Note that a valid Sudoku board does not necessarily have to be solvable.

### Examples

#### Example 1

**Input:**
```python
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
```

**Output:**
```python
True
```

#### Example 2

**Input:**
```python
board = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
```

**Output:**
```python
False
```

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

### Constraints

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit 1-9 or `'.'`.

### Solution

The provided Python solution checks the validity of the Sudoku board by verifying each row, each column, and each 3 x 3 sub-box.

### Functions

- `is_valid_sudoku(board)`: Main function to check if the board is valid.
- `is_valid_unit(unit)`: Helper function to check if a row, column, or box contains unique digits.
- `is_valid_row(board)`: Helper function to check all rows.
- `is_valid_column(board)`: Helper function to check all columns.
- `is_valid_box(board)`: Helper function to check all 3 x 3 sub-boxes.

### Usage

To use the solution, simply call the `is_valid_sudoku` function with a 9 x 9 Sudoku board as input.

```python
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(is_valid_sudoku(board))  # Output: True
```

### Time Complexity

The time complexity of this solution is \(O(1)\). Since the Sudoku board is always a fixed size of 9x9, the number of operations needed to check the board is constant. Each validation (rows, columns, and 3x3 sub-boxes) involves a fixed number of checks.

### Space Complexity

The space complexity of this solution is also \(O(1)\). We only use a constant amount of extra space to store the sets needed to verify the uniqueness of the digits in rows, columns, and sub-boxes.
