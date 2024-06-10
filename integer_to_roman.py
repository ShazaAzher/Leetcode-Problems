def int_to_roman(num: int) -> str:
    # Create a dictionary mapping integer values to Roman numeral symbols
    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    
    # Initialize an empty string to store the Roman numeral representation
    result = ''
    
    # Iterate through the Roman numeral symbols in descending order of value
    for value, symbol in sorted(roman_numerals.items(), reverse=True):
        # Check if num is greater than or equal to the current value of the Roman numeral symbol
        while num >= value:
            # Subtract the value of the Roman numeral symbol from num and append the corresponding symbol to result
            result += symbol
            num -= value
    
    return result
