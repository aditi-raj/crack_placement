class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def helper(open,close,s):
            if open==0 and close==0:
                res.append(s)
                return
            elif open==close:
                helper(open-1,close,s+'(')
            elif open<close and open>0:
                helper(open-1,close,s+'(')
                helper(open,close-1,s+')')
            else:
                helper(open,close-1,s+')')
        helper(n,n,'')
        return res