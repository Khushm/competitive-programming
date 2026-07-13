class Solution:
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        visited = [[False for j in range(m)] for i in range(n)]
        ans = 0
        
        def is_safe(n1, m1):
            return min(m1, n1) >= 0 and n1 < n and m1 < m
        
        def is_land(n1, m1):
            return grid[n1][m1] == 'L'
        
        def is_not_visited(n1, m1):
            return not visited[n1][m1]
        
        def dfs(row, col):
            visited[row][col] = True
            nei = [(row+1, col), (row-1, col), (row, col+1), (row, col-1), (row+1, col+1), (row-1, col-1), (row+1, col-1), (row-1, col+1)]
            for n1, m1 in nei:
                if is_safe(n1, m1) and is_land(n1, m1) and is_not_visited(n1, m1):
                    dfs(n1, m1)
        
        for row in range(n):
            for col in range(m):
                if is_land(row, col) and is_not_visited(row, col):
                    ans += 1
                    dfs(row, col)
        
        return ans
