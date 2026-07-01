class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        
        def check_bounds(r, c):
            return min(r, c) >= 0 and r < m and c < n
        
        q = deque()
        min_dist = {}

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    q.append([row, col, 0])
                    min_dist[(row, col)] = 0
        
        while q:
            row, col, dist = q.popleft()
            neigh = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
            for row2, col2 in neigh:
                if check_bounds(row2, col2) and (row2, col2) not in min_dist and grid[row2][col2] > 0:
                    min_dist[(row2, col2)] = dist+1
                    q.append([row2, col2, dist+1])
                    grid[row2][col2] = dist+1

        