# Container With Most Water

## Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

**Example:**

Input:
```
height = [1,8,6,2,5,4,8,3,7]
```

Output:
```
49
```

Explanation: The above vertical lines are represented by the array `[1,8,6,2,5,4,8,3,7]`. In this case, the max area of water (blue section) the container can contain is 49.

**Constraints:**

- `n == height.length`
- `2 <= n <= 105`
- `0 <= height[i] <= 104`

## Algorithm Used

This problem can be solved using a two-pointer approach. We initialize two pointers, `left` and `right`, at the beginning and end of the array, respectively. We then move the pointers towards each other while calculating the area between the lines formed by the two pointers at each step. We update the maximum area found so far and continue until the pointers meet.

## Pseudocode

```
maxArea(height):
    left = 0
    right = length(height) - 1
    max_area = 0
    
    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area
```

## Time and Space Complexity

- Time Complexity: O(n)
  - The algorithm performs a single pass through the array.
- Space Complexity: O(1)
  - The algorithm uses only a constant amount of extra space.
  
