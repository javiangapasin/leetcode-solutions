# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        ans = 0
        while head is not None:
            #Just add the values from start to beginning
            #Remember that when we shift left / move right in binary, we multiply by 2
            #Then just add the current value that we're at, the other values wouldve been multplied
            ans = ans * 2 + head.val
            head = head.next

        return ans