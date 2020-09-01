# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        return self.addTwoNumbersHelper(l1, l2, carry)

    # Need to pass in carry to helper.
    def addTwoNumbersHelper(self, l1, l2, carry):

        # Main base case.
        if l1 is None and l2 is None:
            if carry == 1:
                return ListNode(carry)
            else:
                return

        # Setup variables.
        currentCarry = 0
        currentVal = carry
        currentVal += 0 if l1 is None else l1.val
        currentVal += 0 if l2 is None else l2.val
        if currentVal >= 10:
            currentVal -= 10
            currentCarry = 1

        # Secondary base cases.
        if l1 is None:
            l2.val = currentVal
            l2.next = self.addTwoNumbersHelper(l1, l2.next, currentCarry)
            print(linked_list_str(l2))
            return l2
        if l2 is None:
            l1.val = currentVal
            l1.next = self.addTwoNumbersHelper(l1.next, l2, currentCarry)
            print(linked_list_str(l1))
            return l1

        # Final case.
        l1.val = currentVal
        l1.next = self.addTwoNumbersHelper(l1.next, l2.next, currentCarry)
        print(linked_list_str(l1))
        return l1

# Recursively print linked list
def linked_list_str(l):
    if l is None:
        return ''
    return str(l.val) + '->' + linked_list_str(l.next)

# print

# # Make first linked list.
# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
# print(linked_list_str(l1))

# # Make second linked list.
# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)
# print(linked_list_str(l2))

# print ''

# # Add linked lists.
# s = Solution()
# l3 = s.addTwoNumbers(l1, l2)

# print ''
# print(linked_list_str(l3))

print

# Make first linked list.
l1 = ListNode(1)
print(linked_list_str(l1))

# Make second linked list.
l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
print(linked_list_str(l2))

print ''

# Add linked lists.
s = Solution()
l3 = s.addTwoNumbers(l1, l2)

print ''
print(linked_list_str(l3))