# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = ListNode(None)
        head = curr
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp = l2
                l2 = l2.next
            curr.next = temp
            curr = curr.next
        while l1 != None:
            temp = l1
            curr.next = temp
            l1 = l1.next
            curr = curr.next
        while l2 != None:
            temp = l2
            curr.next = temp
            l2 = l2.next
            curr = curr.next
        return head.next