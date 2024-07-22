class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target=sum(nums)//2
        dp=[False]*(target+1)
        dp[0]=True
        for i in nums:
            temp=dp.copy()
            for j in range(len(dp)):
                if dp[j] and i+j<=target:
                    temp[i+j]=True
            dp=temp 
        # print(dp)
        return dp[-1]

        