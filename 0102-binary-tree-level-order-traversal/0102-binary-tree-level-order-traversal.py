# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q=[root]
        nxtq=[]
        level=[]
        result=[]
        while q!=[]:
            for node in q:
                level.append(node.val)
                if node.left:
                    nxtq.append(node.left)
                if node.right:
                    nxtq.append(node.right)
            result.append(level)
            level=[]
            q=nxtq
            nxtq=[]
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if root is None:
#             return []
#         q=[root]
#         nxtq=[]
#         level=[]
#         result=[]
#         while q!=[]:
#             for root in q:
#                 level.append(root.val)
#                 if root.left is not None:
#                     nxtq.append(root.left)
#                 if root.right is not None:
#                     nxtq.append(root.right)
#             result.append(level)
#             q=nxtq
#             nxtq=[]
#             level=[]
#         return result
      
            
            

        
        
    