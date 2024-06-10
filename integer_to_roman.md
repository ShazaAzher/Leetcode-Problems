### Problem Statement

Given an integer `num`, convert it to a Roman numeral. Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. 

### Example

**Example 1:**

Input:
```
num = 3749
```

Output:
```
"MMMDCCXLIX"
```

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
700 = DCC as 500 (D) + 100 (C) + 100 (C)
40 = XL as 10 (X) less of 50 (L)
9 = IX as 1 (I) less of 10 (X)

**Example 2:**

Input:
```
num = 58
```

Output:
```
"LVIII"
```

Explanation:

50 = L
8 = VIII

**Example 3:**

Input:
```
num = 1994
```

Output:
```
"MCMXCIV"
```

Explanation:

1000 = M
900 = CM
90 = XC
4 = IV

### Algorithm Explanation

To convert the given integer `num` to a Roman numeral, we can iterate through the list of Roman numeral symbols in descending order of value. At each step, we check if the current value of `num` is greater than or equal to the value of the Roman numeral symbol. If it is, we subtract the value of the Roman numeral symbol from `num` and append the corresponding symbol to the result string. We repeat this process until `num` becomes zero.

### Pseudocode

1. Create a dictionary `roman_numerals` mapping integer values to their corresponding Roman numeral symbols.
2. Initialize an empty string `result` to store the Roman numeral representation.
3. Iterate through the Roman numeral symbols in descending order of value.
4. Inside the loop, check if `num` is greater than or equal to the current value of the Roman numeral symbol.
5. If it is, subtract the value of the Roman numeral symbol from `num` and append the corresponding symbol to `result`.
6. Repeat steps 4-5 until `num` becomes zero.
7. Return the resulting Roman numeral string.

### Time and Space Complexity

- Time Complexity: O(1) since the maximum number of iterations in the loop is constant (13 iterations).
- Space Complexity: O(1) since the space used by the dictionary and result string is constant.
