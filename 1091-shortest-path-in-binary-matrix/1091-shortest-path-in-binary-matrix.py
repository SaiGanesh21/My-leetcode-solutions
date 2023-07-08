class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        if grid[0][0] or grid[rows-1][cols-1]:
            return -1
        q=[]
        q.append([0,0,1])
        visit=set()
        visit.add((0,0))
        directions=[[1,0],[0,1],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

        while q!=[]:
                # print(q)
                r,c,dist=q.pop(0)
                if r==rows-1 and c==cols-1:
                    return dist
                for dr,dc in directions:
                    row=dr+r
                    col=dc+c
                    if 0<=row<rows and 0<=col<cols and (row,col) not in visit and grid[row][col]==0:
                            visit.add((row,col))
                            q.append([row,col,dist+1])
        return -1
                
                
            
        