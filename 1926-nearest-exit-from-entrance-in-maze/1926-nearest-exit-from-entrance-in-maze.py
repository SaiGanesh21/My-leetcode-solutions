class Solution:
    def nearestExit(self, grid: List[List[str]], entrance: List[int]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dist=0
        q=[]
        q.append(tuple(entrance))
        visit=set()
        visit.add(tuple(entrance))
        directions=[[1,0],[0,1],[0,-1],[-1,0]]
        while q!=[]:
            for i in range(len(q)):
                r,c=q.pop(0)
                if [r,c]!=entrance and (r==0 or c==0 or r==rows-1 or c==cols-1):
                    return dist
                for dr,dc in directions:
                    row=dr+r
                    col=dc+c
                    if 0<=row<rows and 0<=col<cols and (row,col) not in visit and grid[row][col]==".":      
                            
                            visit.add((row,col))
                            q.append((row,col))
            dist+=1
        return -1
                