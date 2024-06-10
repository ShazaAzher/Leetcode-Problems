# Problem Statement

Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.

## Examples

Example 1:

Input: 
```python
nums = [-1, 2, 1, -4], target = 1
```

Output: 
```
2
```

Explanation: 
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: 
```python
nums = [0, 0, 0], target = 1
```

Output: 
```
0
```

Explanation: 
The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

# Pseudocode

1. Sort the input array `nums`.
2. Initialize `closest_sum` to a large value.
3. Iterate through the array `nums` from index 0 to `n - 2`.
4. Within this loop, set two pointers `left` and `right` at indices `i + 1` and `n - 1` respectively.
5. While `left < right`, calculate the current sum as `nums[i] + nums[left] + nums[right]`.
6. Update `closest_sum` to the current sum if its absolute difference with `target` is smaller than the absolute difference between `closest_sum` and `target`.
7. If the current sum is less than `target`, increment `left`, else decrement `right`.
8. Repeat steps 5-7 until `left >= right`.
9. Return `closest_sum` as the result.

# Time Complexity

The time complexity of the solution is O(n^2), where n is the length of the input array `nums`. This complexity arises due to the nested iteration through the array to find the closest sum to the target.

# Space Complexity

The space complexity of the solution is O(1), as it only uses a constant amount of extra space for variables regardless of the input size.
