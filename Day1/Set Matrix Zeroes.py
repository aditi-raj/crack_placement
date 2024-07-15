class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros=[]
        m=len(matrix)
        n=len(matrix[0])
        def dfs(R,C):
            dir=[1,-1]
            for k in range(0,max(m,n)):
                if k<n: matrix[R][k]=0
                if k<m: matrix[k][C]=0
            return

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    zeros.append([i,j])
        for r,c in zeros:
            dfs(r,c)
        return matrix