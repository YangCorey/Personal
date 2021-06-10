
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import time
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        prev = [None]
        next_stack = [root]

        p_found = False
        q_found = False
        t1 = time.time()
        while next_stack and not (p_found and q_found):
            next_node = next_stack.pop()
            next_node.prev = prev.pop()
            if next_node == p:
                p_found = True
            elif next_node == q:
                q_found = True
            
            if next_node.left is not None:
                prev.append(next_node)
                next_stack.append(next_node.left)
            if next_node.right is not None:
                prev.append(next_node)
                next_stack.append(next_node.right)

        res = root.val
        hist = set()
        while p is not None:
            hist.add(p)
            p = p.prev
        while q not in hist:
            q = q.prev
        return  q


