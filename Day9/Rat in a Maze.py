def findPath(mat):
    # code here

    n=len(mat)
    res=[]
    dir={'D':(1,0),'U':(-1,0),'L':(0,-1),'R':(0,1)
        }
    if mat[0][0]==0 or mat[n-1][n-1]==0:
        return res
    def dfs(r,c,cur,visited):
        if r==n-1 and c==n-1:
            res.append(cur)
            return
       
        
        for key,val in dir.items():
            nr,nc=r+val[0],c+val[1]
            if 0<=nr<n and 0<=nc<n and mat[nr][nc]!=0 and (nr,nc) not in visited:
                visited.add((nr,nc))
                dfs(nr,nc,cur+key,visited)
                visited.remove((nr,nc))
    v=set()
    v.add((0,0))       
    dfs(0,0,'',v)  
    return res

mat=[[1, 0, 0, 0],
         [1, 1, 0, 1], 
         [1, 1, 0, 0],
         [0, 1, 1, 1]]
print(findPath(mat))