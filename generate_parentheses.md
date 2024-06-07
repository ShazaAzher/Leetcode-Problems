# Generate Parentheses

## Description

This Python solution generates all combinations of well-formed parentheses for a given integer `n`.

## Explanation

The solution utilizes backtracking to systematically build valid parentheses combinations. Here's how it works:

1. The `generateParenthesis` function initializes an empty list `result` to store the valid combinations of parentheses.

2. It defines an inner function `backtrack` to generate the combinations recursively. This function takes three parameters:
   - `s`: the current combination of parentheses being constructed.
   - `left`: the count of left parentheses already added.
   - `right`: the count of right parentheses already added.

3. Inside the `backtrack` function:
   - If the length of the string `s` is equal to `2 * n`, it means we have formed a complete valid combination of parentheses. In this case, we append `s` to the `result` list and return.
   - If the count of left parentheses `left` is less than `n`, we recursively call the `backtrack` function with an additional left parenthesis added to `s` and increment the `left` count.
   - If the count of right parentheses `right` is less than `left`, we recursively call the `backtrack` function with an additional right parenthesis added to `s` and increment the `right` count.

4. Finally, the `generateParenthesis` function calls the `backtrack` function with default parameters to start the recursion and returns the `result` list containing all valid combinations of parentheses.

## Time Complexity

The time complexity of this solution is O(4^n / √n). This complexity arises from the fact that for each of the 2n positions in the output sequence, we have two choices: to put a '(' or ')', resulting in 2^(2n) possible combinations. However, not all these combinations are valid, and the number of valid combinations is given by the nth Catalan number, which is O(4^n / √n).

## Space Complexity

The space complexity of this solution is O(4^n / √n), as it requires storing all valid combinations of parentheses generated during the backtracking process. The maximum number of valid combinations is given by the nth Catalan number. Therefore, the space required grows exponentially with `n`, but is proportional to O(4^n / √n).

