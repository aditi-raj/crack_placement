class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        power=1
        for i in range(1,n+1):
            if power*2==i:
                power=power*2
            dp[i]=1+dp[i-power]
        return dp