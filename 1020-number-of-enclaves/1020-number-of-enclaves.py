class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        def dfs(r,c):
            if 0<=r<rows and 0<=c<cols and (r,c) not in visit and grid[r][c]==1:
                visit.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)
        for c in range(1,cols):
            dfs(0,c)
            dfs(rows-1,c)
        res=0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c]==1:
                    res+=1
        return res