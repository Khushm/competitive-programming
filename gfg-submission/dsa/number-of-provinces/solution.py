class Solution:
    def countConnected(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * V
        ans = 0
        
        def dfs(node):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)
                    
        for start in range(V):
            if not visited[start]:
                ans += 1
                dfs(start)
        
        return ans
