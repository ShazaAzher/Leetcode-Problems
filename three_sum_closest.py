
def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()  # Step 1: Sort the input array nums
    closest_sum = float('inf')  # Step 2: Initialize closest_sum with positive infinity
    
    # Step 3: Iterate through the array nums with index i up to n - 2
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1  # Initialize left and right pointers
        
        # Use a while loop with conditions left < right
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]  # Calculate current sum
            
            # Update closest_sum if the absolute difference is smaller
            if abs(curr_sum - target) < abs(closest_sum - target):
                closest_sum = curr_sum
            
            # Move pointers based on the current sum
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return target  # If current sum equals target, return target
        
    return closest_sum  # Return the closest sum found
        
