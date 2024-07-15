class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        for r in range(len(nums)):
            
            while l<len(nums)-1 and nums[l]!=0:
                l+=1
            
            if r>l and nums[r]!=0 and nums[l]==0:
                nums[l],nums[r]=nums[r],nums[l]
        return nums
            