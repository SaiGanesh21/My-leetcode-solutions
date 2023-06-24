# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
       
        def good(node,currentsum):
            if node is None:
                return 0
            c=0
            if node.val>=currentsum:
                c+=1
            currentsum=max(currentsum,node.val)
            c+= good(node.left,currentsum)
            c+=good(node.right,currentsum)
            return c
        
        return good(root,float("-inf"))
