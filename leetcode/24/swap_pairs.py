# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head, prev=None):
        if head == None:
            if prev != None:
                return prev
            return head
        # at the end
        if head.next == None:
            if prev != None:
                prev.next = None
            head.next = prev
            return head
        # start
        if prev == None:
            return self.swapPairs(head.next, head)
        # swap
        n = head.next
        head.next = prev
        prev.next = self.swapPairs(n.next, n)
        return head
