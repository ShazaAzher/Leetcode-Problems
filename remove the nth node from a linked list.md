# Remove N-th Node From End of List

## Problem Statement

Given the head of a linked list, remove the nth node from the end of the list and return its head.

## Examples

### Example 1

Input:
```python
head = [1, 2, 3, 4, 5]
n = 2
```

Output:
```python
[1, 2, 3, 5]
```

### Example 2

Input:
```python
head = [1]
n = 1
```

Output:
```python
[]
```

### Example 3

Input:
```python
head = [1, 2]
n = 1
```

Output:
```python
[1]
```

## Constraints

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

## Algorithm Explanation

1. **Dummy Node**: Create a dummy node that points to the head of the list. This helps in edge cases where the head might be removed.
2. **Two Pointers**: Use two pointers, `first` and `second`. Initialize both to the dummy node.
3. **Advance First Pointer**: Move the `first` pointer `n + 1` steps ahead so that there is a gap of `n` nodes between `first` and `second`.
4. **Move Both Pointers**: Move both pointers one step at a time until the `first` pointer reaches the end of the list. At this point, the `second` pointer will be just before the node that needs to be removed.
5. **Remove Node**: Adjust the `next` pointer of the `second` pointer to skip the node that needs to be removed.
6. **Return Head**: Return the next node of the dummy node as the new head of the list.

## Pseudocode

```
1. Create a dummy node and set dummy.next to head.
2. Initialize two pointers, first and second, to the dummy node.
3. Move first pointer n + 1 steps forward.
4. While first is not None:
   a. Move first one step forward.
   b. Move second one step forward.
5. Adjust second.next to skip the target node.
6. Return dummy.next as the new head.
```

## Time Complexity

The time complexity of this approach is `O(L)`, where `L` is the length of the linked list. This is because we traverse the list a few times, but each traversal is linear in time.

## Space Complexity

The space complexity is `O(1)` since we only use a few extra pointers and no additional data structures.
