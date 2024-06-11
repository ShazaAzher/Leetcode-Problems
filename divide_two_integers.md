## Problem Statement

Given two integers `dividend` and `divisor`, divide the two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing `dividend` by `divisor`.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.

### Example 1

**Input:**
```plaintext
dividend = 10
divisor = 3
```

**Output:**
```plaintext
3
```

**Explanation:** 
10/3 = 3.33333.. which is truncated to 3.

### Example 2

**Input:**
```plaintext
dividend = 7
divisor = -3
```

**Output:**
```plaintext
-2
```

**Explanation:** 
7/-3 = -2.33333.. which is truncated to -2.

### Constraints

- -2^31 <= dividend, divisor <= 2^31 - 1
- divisor != 0

## Approach

We need to implement integer division without using multiplication, division, or mod operator. The algorithm can be achieved using bitwise operations.

## Algorithm

1. **Handling Edge Cases:**
    - If `dividend` is 0, the quotient is 0.
    - If `divisor` is 1 or -1, return `dividend` or `-dividend` respectively with respect to the bounds.
    
2. **Sign Determination:**
    - Determine the sign of the result based on the signs of `dividend` and `divisor`.

3. **Conversion to Positive:**
    - Work with positive values of `dividend` and `divisor` to simplify the bit manipulation.
    
4. **Bitwise Division:**
    - Use bit manipulation to shift the divisor to the left until it is less than or equal to the dividend.
    - Subtract the shifted divisor from the dividend and keep track of the quotient using bit shifts.

5. **Bounds Checking:**
    - Ensure the quotient is within the 32-bit signed integer range.

## Time Complexity

- The time complexity is O(log N) where N is the absolute value of the dividend. This is due to the bitwise operations.

## Space Complexity

- The space complexity is O(1) as we are using a fixed amount of extra space.
