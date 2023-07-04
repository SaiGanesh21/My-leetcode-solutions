# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # if root not root.left and not right
        
        
#          q=[root]
#          nxtq=[]
        
#          while q:
#             for node in q:
#                 if node.left:
#                     nxtq.append(node.left)
#                 if node.right:
#                     nxtq.append(node.right)
                
                    
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        s=0
        if root is None:
            return None
        q=[root]
        while q!=[]:
            node=q.pop(0)
            if node.left and not node.left.left and not node.left.right:
                s+=node.left.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return s
    
        # res = 0
        # stack = [root]
        # while stack:
        #     temp = stack.pop()
        #     if temp.left and (not temp.left.left) and (not temp.left.right):
        #         res += temp.left.val
        #     if temp.left != None:
        #         stack.append(temp.left)
        #     if temp.right != None:
        #         stack.append(temp.right)   
        # return res
     
        
  