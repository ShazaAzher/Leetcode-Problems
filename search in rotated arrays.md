## Search in Rotated Sorted Array

### Problem Statement

There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

### Example 1

**Input:**
```plaintext
nums = [4,5,6,7,0,1,2], target = 0
```

**Output:**
```plaintext
4
```

### Example 2

**Input:**
```plaintext
nums = [4,5,6,7,0,1,2], target = 3
```

**Output:**
```plaintext
-1
```

### Example 3

**Input:**
```plaintext
nums = [1], target = 0
```

**Output:**
```plaintext
-1
```

### Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are unique.
- `nums` is an ascending array that is possibly rotated.
- `-10^4 <= target <= 10^4`

## Approach

To solve this problem, we need to take advantage of the binary search algorithm, which provides `O(log n)` time complexity. Here's the approach:

1. **Binary Search**:
    - We perform a modified binary search to account for the rotation of the array.
    - We check if the `mid` element is the target.
    - We determine which half of the array (left or right) is sorted.
    - We decide to search the left or right half based on the sorted half and the position of the target.

## Algorithm

1. Initialize `left` to 0 and `right` to `len(nums) - 1`.
2. While `left` is less than or equal to `right`:
    1. Calculate `mid` as `(left + right) // 2`.
    2. If `nums[mid]` is equal to `target`, return `mid`.
    3. If the left half `nums[left]` to `nums[mid]` is sorted:
        1. If `target` is in this range, move `right` to `mid - 1`.
        2. Otherwise, move `left` to `mid + 1`.
    4. Otherwise, the right half `nums[mid]` to `nums[right]` is sorted:
        1. If `target` is in this range, move `left` to `mid + 1`.
        2. Otherwise, move `right` to `mid - 1`.
3. If the loop ends, return `-1` indicating the target is not found.

## Time Complexity

- The time complexity of this algorithm is `O(log n)` due to the binary search.

## Space Complexity

- The space complexity is `O(1)` because we are using a constant amount of extra space.
