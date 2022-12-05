# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        countNode = head
        numNodes = 0
        while countNode is not None:
            countNode = countNode.next
            numNodes += 1

        k = numNodes - n
        prev = None
        ptr = head
        while k != 0:
            prev = ptr
            ptr = ptr.next
            k -= 1

        if prev is None:
            return head.next
        else:
            prev.next = ptr.next
            ptr.next = None
            return head