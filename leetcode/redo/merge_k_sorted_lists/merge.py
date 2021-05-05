from typing import List
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return "[val: {0}, next:{1}]".format(self.val, self.next)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = None
        prev = None
        lists = [list_temp for list_temp in lists if list_temp is not None]
        while len(lists) > 0:
            min_val = None
            #Find the next minimum value
            for node in lists:
                min_val = node.val if min_val is None or node.val < min_val else min_val

            #Remove index will indicate any lists that has reached the end and should be removed from lists
            remove_index = []
            for i, node in enumerate(lists):
                #If this node has the minimum value, add next to result
                if min_val == node.val:
                    if prev is not None:
                        prev.next = node
                        prev = node
                    else:
                        root = ListNode(val = node.val, next = None) 
                        prev = root
                    if lists[i].next is not None:
                        lists[i] = lists[i].next
                    else:
                        remove_index.append(i)

            lists = [list_temp for i, list_temp in enumerate(lists) if i not in remove_index]
        return root

a = ListNode(val = 1, next = ListNode(val = 4, next = ListNode(val = 5)))
b = ListNode(val = 1, next = ListNode(val = 3, next = ListNode(val = 4)))
c = ListNode(val = 2, next = ListNode(val = 6 ))

lists = [a,b,c]
sol = Solution()
print(sol.mergeKLists(lists = lists))
