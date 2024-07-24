import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for i in nums:
            hm[i]=1+hm.get(i,0)
        # print(hm)
        res=list(hm.items())
        min_heap=[]
        for key,count in res:
            heapq.heappush(min_heap,(count,key))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        # print(min_heap)
        t=[]
        for i in range(len(min_heap)-1,-1,-1):
                t.append(min_heap[i][1])
        return t
