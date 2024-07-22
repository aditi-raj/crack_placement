class Solution:
    def simplifyPath(self, path: str) -> str:
        n=len(path)
        stack=[]
        i=0
        while i<n:
            if path[i].isalnum() or path[i]=='.':
                temp=''
                while i<n and path[i]!='/':
                    temp+=path[i]
                    i+=1
                
                if temp=='.':
                    continue
                elif temp=='..' and len(stack)>0:
                    stack.pop()
                elif temp!='..':
                    stack.append(temp)
            i+=1
        res=''
        if not stack:
            return '/'
        while stack:
            res+='/'+stack.pop(0)
        return res