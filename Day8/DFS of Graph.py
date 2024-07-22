#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited=set()
        res=[]
        def dfs(root):
            res.append(root)
            visited.add(root)
            for neighbor in adj[root]:
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(0)
        return res
        # code here