def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    curr = head
    while head.next:
        if (head.next).val == head.val:
            head.next = head.next.next
        else:
            head = head.next
    return curr