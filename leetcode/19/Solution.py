# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return None
        fast = slow = head
        h_len = 1
        while fast:
            if fast.next != None and fast.next.next != None:
                h_len += 1
                fast = fast.next.next
                slow = slow.next
            else:
                break
        # calculate length
        len = h_len * 2
        if fast.next != None:
            len += 1
        # set our delete index
        delete_index = len - n
        slow = prev = head
        if delete_index <= 1:
            # delete current node
            return slow.next
        # walk and then delete
        for _ in range(delete_index-1):
            prev = slow
            slow = slow.next
        prev.next = slow.next
        return head
