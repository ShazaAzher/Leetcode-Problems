# Longest Substring Without Repeating Characters - LeetCode Problem

## Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

### Example

Input: 
- `s = "abcabcbb"`

Output: 
- `3`

Explanation: 
- The answer is "abc", with the length of 3.

## Approach

To solve this problem, we can use the sliding window technique. We'll maintain two pointers, `left` and `right`, to define the current substring. We'll also use a set to keep track of the characters in the current substring. As we iterate through the string, we'll expand the window by moving the `right` pointer to the right and add the characters to the set. If we encounter a character that's already in the set, it means we've found a repeating character. In this case, we'll shrink the window by moving the `left` pointer to the right until the repeating character is no longer in the set. We'll keep track of the maximum length of the substring without repeating characters.

### Pseudocode

1. Initialize `left` and `right` pointers to 0.
2. Initialize an empty set `char_set` to store characters in the current substring.
3. Initialize `max_length` to 0.
4. Iterate through the string:
   - If the character at `right` is not in `char_set`, add it to the set, update `max_length` if needed, and move `right` pointer to the right.
   - If the character at `right` is in `char_set`, remove the character at `left` from `char_set` and move `left` pointer to the right.
5. Return `max_length`.

## Time Complexity

- The time complexity of this solution is O(n), where n is the length of the input string `s`. We iterate through the string once.

## Space Complexity

- The space complexity of this solution is O(min(m, n)), where m is the size of the character set (i.e., the number of unique characters in the input string). In the worst case, the size of the character set can be equal to the length of the input string, leading to O(n) space complexity.
