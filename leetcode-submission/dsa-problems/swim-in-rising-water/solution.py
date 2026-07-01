class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def check_bounds(r, c):
            return min(r, c) >= 0 and max(r, c) < n
        
        maxHeap = [(grid[0][0], 0, 0)]
        visit = set()
        visit.add((0, 0))
        while maxHeap:
            dist, row, col = heapq.heappop(maxHeap)
            if (row, col) == (n-1, n-1):
                return dist

            nei = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
            for row1, col1 in nei:
                if check_bounds(row1, col1) and (row1, col1) not in visit:
                    dist1 = max(dist, grid[row1][col1])
                    heapq.heappush(maxHeap, (dist1, row1, col1))
                    visit.add((row1, col1))
        return 0
