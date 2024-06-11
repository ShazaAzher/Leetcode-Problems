## Next Permutation

### Problem Statement

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for `arr = [1,2,3]`, the following are all the permutations of `arr`: `[1,2,3]`, `[1,3,2]`, `[2,1,3]`, `[2,3,1]`, `[3,1,2]`, `[3,2,1]`.

The next permutation of an array of integers is the next lexicographically greater permutation of its integers. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of `arr = [1,2,3]` is `[1,3,2]`. Similarly, the next permutation of `arr = [2,3,1]` is `[3,1,2]`. While the next permutation of `arr = [3,2,1]` is `[1,2,3]` because `[3,2,1]` does not have a lexicographical larger rearrangement.

Given an array of integers `nums`, find the next permutation of `nums`.

The replacement must be in place and use only constant extra memory.

### Example 1

**Input:**
```plaintext
nums = [1,2,3]
```

**Output:**
```plaintext
[1,3,2]
```

### Example 2

**Input:**
```plaintext
nums = [3,2,1]
```

**Output:**
```plaintext
[1,2,3]
```

### Example 3

**Input:**
```plaintext
nums = [1,1,5]
```

**Output:**
```plaintext
[1,5,1]
```

### Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

## Approach

To find the next permutation of the given array of integers, we can follow these steps:

1. **Find the Largest Index**:
    - Traverse the array from the end and find the largest index `i` such that `nums[i] < nums[i + 1]`. If no such index exists, reverse the array and return as it is the last permutation.
    
2. **Find the Largest Index `j`**:
    - Find the largest index `j` greater than `i` such that `nums[i] < nums[j]`.
    
3. **Swap the Elements**:
    - Swap the elements at indices `i` and `j`.
    
4. **Reverse the Subarray**:
    - Reverse the subarray starting from index `i + 1` to the end of the array.

## Algorithm

1. Traverse the array from the end and find the first decreasing element.
2. Find the element just larger than the found element.
3. Swap these two elements.
4. Reverse the array from the next element of the initially found element to the end of the array.

## Time Complexity

- The time complexity of this algorithm is O(n) where n is the length of the array. This is because we are traversing the array a few times.

## Space Complexity

- The space complexity is O(1) because we are modifying the array in place without using extra space.
