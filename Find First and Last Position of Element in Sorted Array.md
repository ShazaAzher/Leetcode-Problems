## Problem Statement

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given target value.

If the target is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

### Example 1

**Input:**
```plaintext
nums = [5,7,7,8,8,10], target = 8
```

**Output:**
```plaintext
[3,4]
```

### Example 2

**Input:**
```plaintext
nums = [5,7,7,8,8,10], target = 6
```

**Output:**
```plaintext
[-1, -1]
```

### Example 3

**Input:**
```plaintext
nums = [], target = 0
```

**Output:**
```plaintext
[-1, -1]
```

### Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array.
- `-10^9 <= target <= 10^9`

## Approach

To solve this problem, we can use a binary search approach to maintain the `O(log n)` runtime complexity. We'll perform two binary searches:
1. One to find the first occurrence of the target.
2. Another to find the last occurrence of the target.

## Algorithm

1. **Binary Search for the First Occurrence**:
    - Initialize `left` to 0 and `right` to `len(nums) - 1`.
    - While `left` is less than or equal to `right`:
        - Calculate `mid` as `(left + right) // 2`.
        - If `nums[mid]` is greater than or equal to `target`, move `right` to `mid - 1`.
        - If `nums[mid]` is less than `target`, move `left` to `mid + 1`.
        - If `nums[mid]` equals `target`, store `mid` as a potential start and continue searching in the left half.
    - If `nums[left]` equals `target`, return `left` as the start index.

2. **Binary Search for the Last Occurrence**:
    - Initialize `left` to 0 and `right` to `len(nums) - 1`.
    - While `left` is less than or equal to `right`:
        - Calculate `mid` as `(left + right) // 2`.
        - If `nums[mid]` is less than or equal to `target`, move `left` to `mid + 1`.
        - If `nums[mid]` is greater than `target`, move `right` to `mid - 1`.
        - If `nums[mid]` equals `target`, store `mid` as a potential end and continue searching in the right half.
    - If `nums[right]` equals `target`, return `right` as the end index.

3. Return the start and end indices found. If the target is not found, return `[-1, -1]`.

## Time Complexity

- The time complexity of this algorithm is `O(log n)` due to the binary search operations.

## Space Complexity

- The space complexity is `O(1)` as we are using a constant amount of extra space.
