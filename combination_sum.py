def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    def backtrack(start, current_combination, current_sum):
        if current_sum == target:
            result.append(list(current_combination))
            return
        if current_sum > target:
            return

        for i in range(start, len(candidates)):
            current_combination.append(candidates[i])
            backtrack(i, current_combination, current_sum + candidates[i])
            current_combination.pop()

    result = []
    backtrack(0, [], 0)
    return result
