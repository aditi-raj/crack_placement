class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax=1
        currmin=1
        res=nums[0]
        for num in nums:
            if num==0:
                currmax,currmin=1,1
            temp=currmax
            currmax=max(num,currmin*num,currmax*num)
            currmin=min(currmin*num,num,temp*num)
            res=max(currmax,res)
        return res