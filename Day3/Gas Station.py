class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1

        total=0
        diff=[]
        start=0
        for i,j in zip(gas,cost):
            diff.append(i-j)
        for i in range(len(diff)):
            total+=diff[i]
            if total<0:
                total=0
                start=i+1
        return start