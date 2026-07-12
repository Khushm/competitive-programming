class Solution:
    def bfs(self, adj):
        # code here
        queue = deque()
        queue.append(0)
        
        visited = set()
        visited.add(0)
        
        ans = []
        
        while queue:
            node = queue.popleft()
            ans.append(node)
            for nei in adj[node]:
                if nei not in visited:
                    queue.append(nei)
                    visited.add(nei)
        
        return ans
 
        
