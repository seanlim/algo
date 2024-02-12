# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        res = head
        while head:
            next_node = head.next
            while next_node and next_node.val == val:
                next_node = next_node.next
            if head.val == val:
                res = next_node
                head = next_node
                continue
            head.next = next_node
            head = head.next
        return res
