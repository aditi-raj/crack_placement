#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        q=[0]
        res=[0]
        visited=set()
        visited.add(0)
        while q:
            cur=q.pop(0)
            for neigh in adj[cur]:
                if neigh not in visited:
                    visited.add(neigh)
                    res.append(neigh)
                    q.append(neigh)
        # print(res)
        return res