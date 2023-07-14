# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        if root is not None:
            root.left,root.right=root.right,root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
        
        q=[root]
        nxtq=[]
        l=[]
        result=[]
        while q:
            for node in q:
                    l.append(node)
                    if node.left:
                        nxtq.append(node.left.val)
                    if node.right:
                        nxtq.append(node.right.val)
            q=nxtq
            nxtq=[]
            l=l[::-1]
        return l
                