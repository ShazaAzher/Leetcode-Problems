def letterCombinations(digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        # Mapping of digits to corresponding letters
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # Helper function to perform backtracking
        def backtrack(index, path):
            # If the path is complete, add it to the combinations list
            if index == len(digits):
                combinations.append(''.join(path))
                return
            
            # Get the letters that the current digit maps to, and recurse
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()  # Backtrack

        combinations = []
        backtrack(0, [])
        return combinations
