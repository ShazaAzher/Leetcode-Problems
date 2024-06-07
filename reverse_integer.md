# Reverse Integer - LeetCode Problem

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

## Example

Input: x = 123
Output: 321

## Approach

We can solve this problem by repeatedly popping the last digit of the input number and appending it to the reversed number. We need to handle overflow and underflow conditions while performing the reversal.

### Pseudocode

1. Initialize variables to store the maximum and minimum integer values allowed.
2. Determine the sign of the input number.
3. Take the absolute value of the input number.
4. Initialize a variable to store the reversed number.
5. Iterate until the input number becomes zero:
    - Extract the last digit of the input number.
    - Update the input number by removing the last digit.
    - Check for overflow and underflow conditions.
    - Append the extracted digit to the reversed number.
6. Return the reversed number with the appropriate sign.

## Time Complexity

- The time complexity of this solution is O(log(x)), where x is the input number. This is because we repeatedly divide the input number by 10 in each iteration until it becomes zero.

## Space Complexity

- The space complexity of this solution is O(1) since we only use a constant amount of extra space regardless of the input.
