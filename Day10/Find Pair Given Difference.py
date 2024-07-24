
from typing import List


class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        # code here
        #1 2 7 10
        #x=8
        # 8+1=9
        arr.sort()
        s=set()
        for i in arr:
            if i in s:
                return 1
            else:
                s.add(x+i)
        return -1