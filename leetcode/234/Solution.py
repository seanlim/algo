# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if not head.next:
            return True
        if not head.next.next:
            return head.val == head.next.val
        fast = slow = head
        while fast.next:
            if not fast.next.next:
                break
            fast = fast.next.next
            slow = slow.next
        if fast.next:
            fast = fast.next
            slow = slow.next

        # reverse 2nd half
        curr = slow
        prev = None
        next = curr.next
        while curr:
            curr.next = prev
            prev = curr
            curr = next
            if next:
                next = next.next

        # check with head
        while prev and head:
            if prev.val == head.val:
                prev = prev.next
                head = head.next
            else:
                return False
        return True
