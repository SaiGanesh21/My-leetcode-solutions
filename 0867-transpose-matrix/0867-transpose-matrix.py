class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        l1=[[0]*len(matrix) for i in range(len(matrix[0]))]
        r=len(matrix)
        c=len(matrix[0])
        # print(l1)
        for i in range(r):
            for j in range(c):
                l1[j][i]=matrix[i][j]
        return l1