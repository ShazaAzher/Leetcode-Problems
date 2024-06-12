## Combination Sum

### Problem Statement

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of candidates where the chosen numbers sum to `target`. The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

### Examples

#### Example 1

**Input:**

```plaintext
candidates = [2,3,6,7], target = 7
```

**Output:**

```plaintext
[[2,2,3],[7]]
```

#### Example 2

**Input:**

```plaintext
candidates = [2,3,5], target = 8
```

**Output:**

```plaintext
[[2,2,2,2],[2,3,3],[3,5]]
```

#### Example 3

**Input:**

```plaintext
candidates = [2], target = 1
```

**Output:**

```plaintext
[]
```

### Constraints

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of `candidates` are distinct.
- `1 <= target <= 40`

### Solution

The provided Python solution uses a backtracking approach to find all unique combinations of candidates that sum up to the target. The algorithm recursively explores all possible combinations and includes them in the result if they meet the criteria.

### Time Complexity

The time complexity of this solution is `O(2^t)` where `t` is the target value. This is because, in the worst case, the algorithm explores all possible combinations of the candidates that sum up to the target.

### Space Complexity

The space complexity of this solution is `O(t)` where `t` is the target value. This is due to the space used by the recursion stack and the current combination being constructed.
