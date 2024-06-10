def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # Initialize pointers for the leftmost and rightmost lines
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate the current area
        current_area = min(height[left], height[right]) * (right - left)
        # Update max_area if the current area is greater
        max_area = max(max_area, current_area)
        
        # Move the pointer with the smaller height towards the center
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area
