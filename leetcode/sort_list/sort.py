#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def next_node(curr_in, steps):
            curr = curr_in
            for i in range(steps):
                if curr is not None and curr.next is not None:
                    curr = curr.next
                else:
                    return None
            return curr

        def print_node(head):
            print("start")
            while head is not None:
                print(head.val)
                head = head.next


        step = 1
        dummy = ListNode(val = 0)

        while True:
            curr = dummy
            l = dummy.next if dummy.next is not None else head
            r = next_node(l, step)
            if r is None:
                return dummy.next if dummy.next is not None else head

            l_ct = step
            r_ct = step

            while l is not None:
                while l_ct > 0 or r_ct > 0:
                    l_val = l.val if l_ct > 0 else r.val + 1
                    r_val = r.val if r_ct > 0 else l.val + 1
                    if l_val < r_val:
                        curr.next = l
                        curr = curr.next
                        l = l.next
                        l_ct = l_ct - 1 if l is not None else 0
                    else:
                        curr.next = r
                        curr = curr.next
                        r = r.next
                        r_ct = r_ct - 1 if r is not None else 0
                l = r
                r = next_node(l,step)
                l_ct = step if l is not None else 0
                r_ct = step if r is not None else 0

            curr.next = None
            step *= 2



n5 = ListNode(val = 3)
#n4 = ListNode(val = 5, next = n5)
n3 = ListNode(val = 1, next = n5)
n2 = ListNode(val = 2, next = n3)
head = ListNode(val = 4, next = n2)

sol = Solution()
ans = sol.sortList(head)
while ans is not None:
    print(ans.val)
    ans = ans.next

n5 = ListNode(val = 0)
n4 = ListNode(val = 4, next = n5)
n3 = ListNode(val = 3, next = n4)
n2 = ListNode(val = 5, next = n3)
head = ListNode(val = -1, next = n2)
sol = Solution()
ans = sol.sortList(head)
while ans is not None:
    print(ans.val)
    ans = ans.next
head = ListNode(val = 1)

sol = Solution()
ans = sol.sortList(head)
while ans is not None:
    print(ans.val)
    ans = ans.next
