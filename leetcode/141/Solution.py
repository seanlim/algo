# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
            # use floyd's cycle detection
            slow = fast = head
            while fast:
                slow = slow.next
                if not fast.next or not fast.next.next:
                    # cyclic lists should not have an end
                    return False
                fast = fast.next.next
                if slow == fast:
                    return True
            return False
