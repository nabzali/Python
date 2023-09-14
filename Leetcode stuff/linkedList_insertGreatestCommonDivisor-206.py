# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def highestCommonDivisor(a, b):
            for i in range(min(a, b), 0, -1):
                if a % i == 0 and b % i == 0:
                    return i
        
        current = head
        vals = []
        newVals = []
        while current:
            vals.append(current.val)
            current = current.next

        for i in range(1, len(vals)):
            newVals.append(highestCommonDivisor(vals[i], vals[i-1]))

        current = head
        while current.next:
            temp = current.next
            current.next = ListNode(newVals[0], temp)
            del newVals[0]
            current = current.next.next

        return head