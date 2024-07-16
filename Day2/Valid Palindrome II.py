class Solution:
    def validPalindrome(self, s: str) -> bool:
        n=len(s)
        l,r=0,n-1
        cnt=0
        while l<=r :
            if s[l]==s[r]:
                l+=1
                r-=1
            elif cnt==0:
                l+=1
                cnt=1
            else:
                break
        if l==r or l>r:
            return True

        l,r=0,n-1
        cnt=0
        while l<=r :
            if s[l]==s[r]:
                l+=1
                r-=1
            elif cnt==0:
                r-=1
                cnt=1
            else:
                return False
        return True