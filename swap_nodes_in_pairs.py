# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # Create a dummy node to simplify edge cases
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while head and head.next:
        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping the nodes
        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        # Repositioning prev and head for the next swap
        prev = first_node
        head = first_node.next

    # Return the new head
    return dummy.next
