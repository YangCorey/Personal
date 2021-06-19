"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def help(self, curr, prev):
        if self.first_node is None:
            self.first_node = curr
        if curr.left is not None:
            curr.left.next = curr.right
            if prev is not None:
                prev.next = curr.left
            prev = curr.right
            if curr.next is not None:
                self.help(curr.next, prev)
            else:
                if self.first_node.left is not None:
                    temp_next = self.first_node.left
                    self.first_node = None
                    self.help(temp_next, None)
        
    def connect(self, root: 'Node') -> 'Node':
        self.first_node = None
        if root is not None:
            self.help(root, None)
        return root

        
        
