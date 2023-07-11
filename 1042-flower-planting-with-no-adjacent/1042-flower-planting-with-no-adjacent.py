class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        neigbh=defaultdict(list)
        for a,b in paths:
            neigbh[a].append(b)
            neigbh[b].append(a)
            
        res=[0]*n
        
        for i in range(1,n+1):
            avaia={1,2,3,4}
            for neigh in neigbh[i]:
                if res[neigh-1] in avaia:
                    avaia.remove(res[neigh-1])
            res[i-1]=avaia.pop()
        return res
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # neighbors = defaultdict(set)
        # for a, b in paths:
        #     neighbors[a].add(b)
        #     neighbors[b].add(a)
        # ans = [0] * n
        # for i in range(1, n + 1):
        #     available = {1, 2, 3, 4}
        #     for neighbor in neighbors[i]:
        #         if ans[neighbor] in available:
        #             available.remove(ans[neighbor])
        #     ans[i - 1] = available.pop()
        # return ans