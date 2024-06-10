def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """

    # Constants for the 32-bit signed integer range
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    # Initial index and length of the string
    i, n = 0, len(s)
    
    # Ignore leading whitespaces
    while i < n and s[i] == ' ':
        i += 1
    
    # Check if the string is empty after removing whitespaces
    if i == n:
        return 0
    
    # Determine the sign
    sign = 1
    if s[i] == '+':
        i += 1
    elif s[i] == '-':
        sign = -1
        i += 1
    
    # Initialize the result
    result = 0
    
    # Convert characters to integer until a non-digit is encountered
    while i < n and s[i].isdigit():
        digit = int(s[i])
        
        # Check for overflow and underflow
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        
        result = result * 10 + digit
        i += 1
    
    # Apply the sign to the result
    result *= sign
    
    return result
