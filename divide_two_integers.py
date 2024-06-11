def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    # Constants for the 32-bit signed integer range
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    # Handle edge cases
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero")
    
    if dividend == 0:
        return 0
    
    if divisor == 1:
        return min(max(dividend, INT_MIN), INT_MAX)
    
    if divisor == -1:
        return min(max(-dividend, INT_MIN), INT_MAX)
    
    # Determine the sign of the quotient
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    
    # Work with positive values
    dividend = abs(dividend)
    divisor = abs(divisor)
    
    quotient = 0
    # Perform bitwise division
    while dividend >= divisor:
        temp_divisor = divisor
        multiple = 1
        while dividend >= (temp_divisor << 1):
            temp_divisor <<= 1
            multiple <<= 1
        dividend -= temp_divisor
        quotient += multiple
    
    quotient = quotient if sign > 0 else -quotient
    
    # Ensure the quotient is within the 32-bit signed integer range
    return min(max(quotient, INT_MIN), INT_MAX)
    
