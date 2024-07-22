class Solution:
    def knightDialer(self, n: int) -> int:
        hash={0:[4,6],1:[6,8],2:[7,9],3:[4,8],4:[0,3,9],5:[],6:[0,1,7],7:[2,6],8:[1,3],9:[2,4]}
        @cache
        def dfs(i,times):
            if times==0:
                return 1
        
            temp=0
            for next in hash[i]:
                temp=temp+dfs(next,times-1)
            return temp
        res=0
        for i in range(10):
            res+=dfs(i,n-1)
        return res%((10**9)+7)
