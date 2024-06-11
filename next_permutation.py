def nextPermutation(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if n <= 1:
        return
    
    # Step 1: Find the first decreasing element from the end
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    # If there is no such element, reverse the array
    if i == -1:
        nums.reverse()
        return
    
    # Step 2: Find the element just larger than nums[i]
    j = n - 1
    while nums[j] <= nums[i]:
        j -= 1
    
    # Step 3: Swap elements at i and j
    nums[i], nums[j] = nums[j], nums[i]
    
    # Step 4: Reverse the array from i+1 to the end
    nums[i + 1:] = reversed(nums[i + 1:])
        
