# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        if not (list1 and list2):
            if list1:
                # list2 empty, we return list1
                return list1
            elif list2:
                # list1 empty, we return list2
                return list2
            # both lists empty
            return None

        # track start node
        start = None
        # track tail of our linkedlist
        tail = None

        while list1 and list2:
            # pick from either
            if list1.val < list2.val:
                if start == None:
                    start = list1
                if tail != None:
                    # point current tail to new tail
                    tail.next = list1
                # set new tail
                tail = list1
                # move ptr forward
                list1 = list1.next
            else:
                # mirror case
                if start == None:
                    start = list2
                if tail != None:
                    tail.next = list2
                tail = list2
                list2 = list2.next

        # if either lists are empty, we simply point tail to them (sorted lists)
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return start
