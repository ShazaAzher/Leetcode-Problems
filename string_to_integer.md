# String to Integer (atoi)

## Problem Description

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

The algorithm for `myAtoi(string s)` is as follows:

1. Whitespace: Ignore any leading whitespace (" ").
2. Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
4. Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
5. Return the integer as the final result.

### Example:

**Input:** `s = "42"`
**Output:** `42`

Explanation:
The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^

(Additional examples and explanations omitted for brevity)

## Constraints

- 0 <= s.length <= 200
- s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

## Pseudocode

```plaintext
Function myAtoi(s: string) -> integer:
    Constants:
        INT_MAX = 2^31 - 1
        INT_MIN = -2^31

    Initialize:
        i = 0             // Initial index for string traversal
        n = length(s)     // Length of the string s
        result = 0        // Initialize the result integer

    1. Ignore leading whitespace characters in s
        While i < n and s[i] is ' ':
            Increment i

    2. Check for empty string or all whitespace
        If i == n:
            Return 0

    3. Determine the sign
        If s[i] is '+' or '-':
            sign = 1 if s[i] is '+' else -1
            Increment i

    4. Convert characters to integer until a non-digit is encountered
        While i < n and s[i] is digit:
            digit = integer value of s[i]
            
            // Check for overflow and underflow
            If result > (INT_MAX - digit) / 10:
                Return INT_MAX if sign is 1 else INT_MIN
            
            // Update the result
            result = result * 10 + digit
            Increment i

    5. Apply the sign to the result
        result = result * sign

    6. Return the result
        Return result

Feel free to adjust the formatting or add any additional information as needed.
