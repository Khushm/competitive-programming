class Solution:
    def dfs(self, adj):
        n = len(adj)
        
        visit = [False] * n
        ans = []
        
        def helper(node):
            visit[node] = True
            ans.append(node)
            for nei in adj[node]:
                if not visit[nei]:
                    helper(nei)
                
        helper(0)
        return ans
