# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        length = 0
        current = head

        while current:
            length += 1
            current = current.next
        dummy = ListNode(0, head)
        current = dummy

        for _ in range(length - n):
            current = current.next

        current.next = current.next.next

        return dummy.next
