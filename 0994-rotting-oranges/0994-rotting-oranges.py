class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit=set()
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        
        for r in range(rows):
              for c in range(cols):
                    if grid[r][c]==2:
                        q.append((r,c))
                    if grid[r][c]==1:
                        visit.add((r,c))
        time=0
        while q and visit:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in [[0,1],[1,0],[0,-1],[-1,0]]:
                    row=r+dr
                    col=c+dc
                    if (row,col) in visit:
                        visit.remove((row,col))
                        q.append((row,col))
            time+=1
        if len(visit)==0:
            return time
        else:
            return -1
            
                
            
        
        
        
        