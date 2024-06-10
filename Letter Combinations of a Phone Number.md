# Letter Combinations of a Phone Number

## Problem Statement

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

## Examples

Example 1:

Input:
```python
digits = "23"
```

Output:
```python
["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

Example 2:

Input:
```python
digits = ""
```

Output:
```python
[]
```

Example 3:

Input:
```python
digits = "2"
```

Output:
```python
["a","b","c"]
```

## Constraints

- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

## Algorithm Explanation

1. **Base Case**: If the input `digits` is empty, return an empty list.
2. **Mapping**: Create a dictionary `phone_map` to map each digit to its corresponding letters.
3. **Backtracking**:
    - Define a helper function `backtrack(index, path)` to build the combinations.
    - If `index` equals the length of `digits`, a complete combination has been formed, so add it to the results.
    - For the current digit, get the possible letters and recurse with each letter added to the current path.
    - Backtrack by removing the last letter and trying the next possible letter.

## Time Complexity

The time complexity is O(3^n * 4^m), where n is the number of digits in the input that map to 3 letters (digits 2, 3, 4, 5, 6, 8) and m is the number of digits that map to 4 letters (digits 7, 9). This is because each digit generates a branching factor of 3 or 4 in the recursion tree.

## Space Complexity

The space complexity is O(3^n * 4^m) for the output list and the recursion stack. In the worst case, the recursion stack will have a depth equal to the length of the input `digits`.
