def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    slow = fast = dummy
    dummy.next = head
    while fast.next:
        if n > 0:
            n -= 1
        else:
            slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next