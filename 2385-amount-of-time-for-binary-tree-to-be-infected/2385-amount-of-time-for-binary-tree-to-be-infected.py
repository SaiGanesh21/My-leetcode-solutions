# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
            q=[root]
            adjacency_list=defaultdict(list)

            while q:
                node=q.pop(0)
                if node.left:
                    q.append(node.left)
                    adjacency_list[node.left.val].append(node.val)
                    adjacency_list[node.val].append(node.left.val)
                if node.right:
                    q.append(node.right)
                    adjacency_list[node.right.val].append(node.val)
                    adjacency_list[node.val].append(node.right.val)



            q=[(start,0)]
            visited=set()
            visited.add(start)
            while q:
                node,time=q.pop(0)
                for neigbhour in adjacency_list[node]:
                    if neigbhour not in visited:
                        visited.add(neigbhour)
                        q.append((neigbhour,time+1))

            return time

        