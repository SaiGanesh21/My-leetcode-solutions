"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visit={}
        q=deque()
        q.append(node)
        
        visit[node]=Node(node.val)
        while q:
            n=q.popleft()
            for nei in n.neighbors:
                if nei not in visit:
                    visit[nei]=Node(nei.val)
                    q.append(nei)
                visit[n].neighbors.append(visit[nei])
        return visit[node]
            