class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea=0
        n=len(height)
        width=n-1
        l,r=0,n-1
        while width>0:
            if height[l]<height[r]:
                
                maxArea=max(maxArea,width*height[l])
                l+=1
            else:
                
                maxArea=max(maxArea,width*height[r])
                r-=1
            width-=1
        return maxArea