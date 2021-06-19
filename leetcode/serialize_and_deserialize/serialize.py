# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    #Creating a depth first search string representation of tree
    def serialize_help(self, node):
        if node is None:
            self.serialize.append("None")
            return
        self.serialize.append(str(node.val))
        self.serialize_help(node.left)
        self.serialize_help(node.right)
        
        
    def serialize(self, root):
        self.serialize = []
        self.serialize_help(root)
        return ",".join(self.serialize)
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
    #Creating a tree using depth first serach algorithm
    def deserialize_help(self): 
        self.ind += 1
        if self.deserialize[self.ind] == "None":
            return None
        node = TreeNode(int(self.deserialize[self.ind]))
        
        node.left = self.deserialize_help()
        node.right = self.deserialize_help()
        return node
        
    def deserialize(self, data):
        self.deserialize = data.split(",")
        self.ind = -1
        return self.deserialize_help()
        
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
