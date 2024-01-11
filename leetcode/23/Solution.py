
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def selectMin(self, lists):
        minVals = [x.val for x in lists if x is not None]
        if not minVals:
            return None 
        return min(minVals)

    def resolveLists(self, lists, currNode):
        minVal = self.selectMin(lists)
        if minVal == None: 
            return 
        newLists = []
        for l in lists:
            if l.val == minVal:
                if l.next != None:
                    newLists.append(l.next) 
                currNode.next = l
                currNode = l
            else:
                newLists.append(l)
        self.resolveLists(newLists, currNode)

    def mergeKLists(self, lists):
        minVal = self.selectMin(lists)
        if minVal == None:
            return None
        firstNode = None
        currNode = None
        newLists = []
        for l in lists:
            if not l :
                continue
            if l.val == minVal:
                if firstNode == None:
                    firstNode = l
                if l.next != None:
                    newLists.append(l.next) 
                if currNode == None:
                    currNode = l
                else: 
                    currNode.next = l
                    currNode = l
            else:
                newLists.append(l)
        self.resolveLists(newLists, currNode)
        return firstNode
        
        