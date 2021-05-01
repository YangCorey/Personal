# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addListNode(self, l1, l2, carry_over_prev = 0):
        val_1 = l1.val if l1 is not None else 0
        val_2 = l2.val if l2 is not None else 0

        l1_next = l1.next if l1 is not None else None
        l2_next = l2.next if l2 is not None else None

        sum_val = val_1 + val_2 + carry_over_prev
        new_link = ListNode(val = sum_val%10)
        carry_over = int(sum_val/10)
        return new_link, l1_next, l2_next, carry_over


    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        res, l1_next, l2_next, carry_over = self.addListNode(l1,l2)
        prev_res = res

        while not(l1_next is None and l2_next is None):
            res_temp, l1_next, l2_next, carry_over = self.addListNode(l1 = l1_next, l2 = l2_next, carry_over_prev = carry_over)
            prev_res.next = res_temp
            prev_res = res_temp
        if carry_over > 0:
            prev_res.next, _, _, _ = self.addListNode(l1_next, l2_next, carry_over_prev = carry_over)

        return res

def createListNode(lst):
    first_node = ListNode(val = lst[0])
    prev_node = first_node
    for i in range(1, len(lst)):
        node_temp = ListNode(val = lst[i])
        prev_node.next = node_temp
        prev_node = node_temp
    return first_node

def printNode(lst):
    while lst is not None:
        print(lst.val)
        lst = lst.next

l1 = createListNode([9,9,9,9,9,9,9])
l2 = createListNode([9,9,9,9])

sol = Solution()
sol_val = sol.addTwoNumbers(l1,l2)
printNode(sol_val)
