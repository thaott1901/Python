class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    num1 = 0
    pow = 0
    for i in l1:
        num1 += i * (10 ** pow)
        pow += 1
    num2 = 0
    pow = 0
    for i in l2:
        num2 += i * (10 ** pow)
        pow += 1
    sum = num1 + num2
    result = []
    while sum > 0:
        digit = sum % 10
        result.append(digit)
        sum = sum // 10
    return result

    ## This part is for LinkedList
    # curr_node = ListNode(None)
    # head_node = curr_node
    #
    # carry = 0
    # while l1 or l2:
    #     sum_temp = carry
    #     if l1 != None:
    #         sum_temp += l1.val
    #         l1 = l1.next
    #     if l2 != None:
    #         sum_temp += l2.val
    #         l2 = l2.next
    #
    #     carry = sum_temp // 10
    #     curr_node.next = ListNode(sum_temp % 10)
    #     curr_node = curr_node.next
    #
    # if carry == 1:
    #     curr_node.next = ListNode(carry)
    #
    # return head_node.next


l1 = [2, 4, 3]
l2 = [5, 6, 4]

a, b, c, res = addTwoNumbers(l1, l2)
print(a, " + ", b, " = ", c)
print(res)
