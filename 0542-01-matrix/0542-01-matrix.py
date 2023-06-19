class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
        visit=set()
        q=[]
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==0:
                    visit.add((r,c))
                    q.append((r,c))
        while q:
            r,c=q.pop(0)
            for dr,dc in [[0,1],[1,0],[0,-1],[-1,0]]:
                row=r+dr
                col=c+dc
                if 0<=row<rows and 0<=col<cols and (row,col) not in visit:
                    mat[row][col]=mat[r][c]+1
                    visit.add((row,col))
                    q.append((row,col))
        return mat
            
            