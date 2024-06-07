# Zigzag Conversion - LeetCode Problem

## Problem Statement

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
      P A H N
      A P L S I I G
      Y I R


And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows.

### Example

Input:
- s = "PAYPALISHIRING"
- numRows = 3

Output:
- "PAHNAPLSIIGYIR"

## Approach

We can solve this problem by simulating the zigzag pattern and iterating through the input string `s`. We'll initialize a list `result` with `numRows` empty strings, each representing a row in the zigzag pattern. Then, we'll iterate through each character in `s`, appending it to the appropriate row in `result`. Finally, we'll join the strings in `result` to form the final zigzag pattern string.

### Pseudocode

1. Initialize a list `result` with `numRows` empty strings.
2. Initialize variables `row` and `direction`.
3. Iterate through each character `char` in the input string `s`:
   - Append `char` to the `result` list at index `row`.
   - Update the `direction` based on whether we have reached the top or bottom row.
   - Update the `row` based on the current direction.
4. Join the strings in the `result` list to form the final zigzag pattern string.
5. Return the final zigzag pattern string.

## Time Complexity

- The time complexity of this solution is O(n), where n is the length of the input string `s`. We iterate through each character of the string once.

## Space Complexity

- The space complexity of this solution is O(n), where n is the length of the input string `s`. We use additional space to store the `result` list.



