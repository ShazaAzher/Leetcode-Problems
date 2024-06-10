# Swap Nodes in Pairs

## Problem Statement

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

## Examples

### Example 1

Input:
```python
head = [1, 2, 3, 4]
```

Output:
```python
[2, 1, 4, 3]
```

### Example 2

Input:
```python
head = []
```

Output:
```python
[]
```

### Example 3

Input:
```python
head = [1]
```

Output:
```python
[1]
```

## Constraints

- The number of nodes in the list is in the range [0, 100].
- `0 <= Node.val <= 100`

## Algorithm Explanation

1. **Dummy Node**: Create a dummy node and set its next pointer to the head of the list. This helps handle edge cases where the head might be swapped.
2. **Iteration**: Use a while loop to iterate through the list. At each step, consider two nodes, `first` and `second`, that need to be swapped.
3. **Swap Operation**: Adjust the pointers to swap the two nodes.
4. **Move to Next Pair**: Move to the next pair of nodes to be swapped.
5. **Return Head**: Return the next node of the dummy node as the new head of the list.

## Pseudocode

```
1. Create a dummy node and set dummy.next to head.
2. Initialize a pointer prev to the dummy node.
3. While prev.next and prev.next.next are not None:
   a. Set first to prev.next and second to prev.next.next.
   b. Swap the nodes first and second by adjusting pointers.
   c. Move prev to the next pair of nodes.
4. Return dummy.next as the new head.
```

## Time Complexity

The time complexity of this approach is `O(n)`, where `n` is the number of nodes in the linked list. We traverse the list once.

## Space Complexity

The space complexity is `O(1)` since we use only a few extra pointers and no additional data structures.
