class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])

        def check_bounds(row, col):
            return min(row, col) >= 0 and row < m and col < n

        visit = set()
        visit.add((0,0))
        maxHeap = [(-(health-grid[0][0]), 0, 0)]

        while maxHeap:
            heal, row, col = heapq.heappop(maxHeap)
            heal = -heal
            if not heal:
                continue
            if (row, col) == (m-1, n-1) and heal: 
                return True
            nei = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
            for row1, col1 in nei:
                if check_bounds(row1, col1) and (row1, col1) not in visit:
                    heapq.heappush(maxHeap, (-(heal-grid[row1][col1]), row1, col1))
                    visit.add((row1, col1))
        return False
