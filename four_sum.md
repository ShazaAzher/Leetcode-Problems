# Four Sum

## Problem Statement

Given an array `nums` of `n` integers, return an array of all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:

- `0 <= a, b, c, d < n`
- `a, b, c, and d` are distinct.
- `nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in any order.

## Examples

### Example 1:

Input:
```python
nums = [1, 0, -1, 0, -2, 2]
target = 0
```

Output:
```python
[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

### Example 2:

Input:
```python
nums = [2, 2, 2, 2, 2]
target = 8
```

Output:
```python
[[2, 2, 2, 2]]
```

## Constraints

- `1 <= nums.length <= 200`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

## Algorithm Explanation

1. **Sorting**: Sort the input array to facilitate the two-pointer approach.
2. **Iterate through the array**: Use two nested loops to fix the first two numbers of the quadruplet.
3. **Two-pointer technique**: For the remaining part of the array, use the two-pointer technique to find the other two numbers such that the sum is equal to the target.
4. **Skip duplicates**: Skip duplicate elements to avoid duplicate quadruplets.
5. **Store results**: If the sum matches the target, store the quadruplet in the results list.

## Pseudocode

```
function fourSum(nums, target):
    sort(nums)
    results = []
    for i from 0 to length(nums) - 3:
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j from i + 1 to length(nums) - 2:
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left = j + 1
            right = length(nums) - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    append [nums[i], nums[j], nums[left], nums[right]] to results
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                else if total < target:
                    left += 1
                else:
                    right -= 1
    return results
```

## Time Complexity

The time complexity of this approach is `O(n^3)`, where `n` is the length of the array. This is because we have two nested loops and a two-pointer approach inside the inner loop.

## Space Complexity

The space complexity is `O(1)` for the additional space used by the algorithm, excluding the space required to store the output.
