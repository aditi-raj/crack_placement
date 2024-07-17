from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        #defaultdict -from collections module ,parameter:returns that when key is not found
        graph=defaultdict(list)
        for u,v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        root=None
        for key,val in graph.items():
            if len(val)==1:
                root=key
                break
        def dfs(root,prev,res):
            res.append(root)
            for neigh in graph[root]:
                if neigh!=prev:
                    dfs(neigh,root,res)
            return res
        return dfs(root,float('inf'),[])





