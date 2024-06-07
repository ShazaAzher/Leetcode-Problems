# Add Two Numbers - LeetCode Problem

## Problem Statement

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Example

Input: 
- l1 = [2,4,3]
- l2 = [5,6,4]

Output: 
- [7,0,8]

Explanation: 
- 342 + 465 = 807.

## Approach

We can solve this problem by iterating through both linked lists simultaneously, adding the corresponding digits along with any carry-over from the previous sum. We'll initialize a dummy node to keep track of the result linked list. We'll iterate through both input linked lists, adding the values of the nodes along with the carry-over. The result will be stored in a new linked list, with each node containing a digit of the sum.

### Pseudocode

1. Initialize a dummy node to store the head of the result linked list.
2. Initialize a carry variable to track any overflow from the previous sum.
3. Iterate through both input linked lists simultaneously.
4. Add the values of the current nodes along with the carry-over.
5. Update the carry-over and create a new node for the result linked list.
6. Move to the next nodes in the input linked lists.
7. Repeat steps 4-6 until both input linked lists are exhausted.
8. Return the head of the result linked list.

## Time Complexity

- The time complexity of this solution is O(max(m, n)), where m and n are the lengths of the two input linked lists. This is because we iterate through both lists once.

## Space Complexity

- The space complexity of this solution is O(max(m, n)), where m and n are the lengths of the two input linked lists. This is because we create a new linked list to store the result.
