# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy
    
    # Move first so that it is n+1 nodes ahead of second
    for _ in range(n + 1):
        first = first.next

    # Move both pointers until first reaches the end
    while first is not None:
        first = first.next
        second = second.next
    
    # Remove the nth node from the end
    second.next = second.next.next
    
    return dummy.next
