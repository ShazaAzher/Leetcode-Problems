# Longest Palindromic Substring - LeetCode Problem

## Problem Statement

Given a string `s`, return the longest palindromic substring in `s`.

### Example

Input:
- s = "babad"

Output:
- "bab"

Explanation:
- "aba" is also a valid answer.

## Approach

We can solve this problem using dynamic programming. We'll create a 2D array `dp`, where `dp[i][j]` represents whether the substring from index `i` to index `j` in the string `s` is a palindrome. We'll initialize the diagonal of `dp` with `True` because single characters are always palindromes. Then, we'll iterate over the string `s` and mark substrings as palindromes based on their characters. After filling the `dp` array, we'll find the longest palindromic substring by iterating over it and keeping track of the maximum length and the corresponding indices. Finally, we'll return the substring using the indices.

### Pseudocode

1. Initialize a 2D array `dp` of size `n x n`, where `n` is the length of the string `s`. Initialize all elements of `dp` to `False`.
2. Initialize variables `start` and `max_length` to store the starting index and maximum length of the longest palindromic substring, respectively.
3. Iterate over the string `s` with two pointers `i` and `j`:
   - If `s[i]` is equal to `s[j]` and either `j - i <= 2` or the substring from index `i + 1` to index `j - 1` is a palindrome (i.e., `dp[i + 1][j - 1]` is `True`), mark `dp[i][j]` as `True`.
   - If `dp[i][j]` is `True` and `j - i + 1` is greater than `max_length`, update `start` and `max_length`.
4. Return the substring of `s` from index `start` to index `start + max_length`.

## Time Complexity

- The time complexity of this solution is O(n^2), where n is the length of the input string `s`. This is because we iterate over the 2D array `dp` of size `n x n`.

## Space Complexity

- The space complexity of this solution is O(n^2), where n is the length of the input string `s`. This is because we use a 2D array `dp` of size `n x n` to store the results of the dynamic programming approach.
