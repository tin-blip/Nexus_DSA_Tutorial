# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        temp = head
        for _ in range(count//2):
            temp = temp.next

        return temp
