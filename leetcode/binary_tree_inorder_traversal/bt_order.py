#Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversalHelp(self, node: TreeNode) -> List[int]:
        if node == None:
            return []
        res = self.inorderTraversalHelp(node.left)
        res += [node.val]
        res += self.inorderTraversalHelp(node.right)

        return res



    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        next_node = root
        #Tracks next node to process
        node_stack = []
        #If this is true then automatically add current val to list
        instant_add = False
        
        #iterate through the tree in order
        while next_node is not None:
            if instant_add:
                res.append(next_node.val)
                instant_add = next_node.right is None
                if next_node.right is None:
                    next_node = node_stack.pop() if len(node_stack) > 0 else None
                else:
                    next_node = next_node.right
                continue

            if next_node.left is not None:
                node_stack.append(next_node)
                next_node = next_node.left
            else:
                res.append(next_node.val)
                instant_add = next_node.right is None
                if next_node.right is None:
                    next_node = node_stack.pop() if len(node_stack) > 0 else None
                else:
                    next_node = next_node.right

        return res

sol = Solution()


