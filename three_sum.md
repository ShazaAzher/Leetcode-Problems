### Three Sum Problem

#### Problem Statement
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

#### Example
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
```

#### Algorithm Explanation
1. Sort the input array `nums`.
2. Iterate through the array `nums` with index `i` up to `n - 2`:
   - Skip duplicates to avoid duplicate triplets.
   - Initialize two pointers `left` and `right`, where `left = i + 1` and `right = n - 1`.
   - Use a while loop with conditions `left < right`:
      - Calculate the total sum of elements at indices `i`, `left`, and `right`.
      - If the total is zero:
         - Add the triplet `[nums[i], nums[left], nums[right]]` to the result list.
         - Skip duplicates of `left` and `right`.
         - Move `left` and `right` pointers towards each other.
      - If the total is less than zero, increment `left`.
      - If the total is greater than zero, decrement `right`.
3. Return the list of triplets.

#### Time Complexity
The time complexity of this algorithm is O(n^2), where n is the length of the input array `nums`. This is because we iterate through the array once, and for each element, we use a two-pointer approach that takes O(n) time.

#### Space Complexity
The space complexity of this algorithm is O(1), as we only use a constant amount of extra space for storing variables and the output list of triplets.
