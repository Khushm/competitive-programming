class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def check_bounds(r, c):
            return min(r, c) >= 0 and max(r, c) < n
        
        def compute_manh_dist():
            q = deque()
            min_dist = {}

            for r in range(n):
                for c in range(n):
                    if grid[r][c]:
                        q.append([r, c, 0])
                        min_dist[(r, c)] = 0
            # print(min_dist)
            while q:
                r, c, d = q.popleft()
                nei = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for r1, c1 in nei:
                    if check_bounds(r1, c1) and (r1, c1) not in min_dist:
                        q.append([r1, c1, d+1])
                        min_dist[(r1, c1)] = d+1
            # print(min_dist)
            return min_dist
        
        min_dist = compute_manh_dist()
        
        maxHeap = [(-min_dist[(0, 0)], 0, 0)]
        visit = set()
        visit. add((0, 0))

        while maxHeap:
            d, r, c = heapq.heappop(maxHeap)
            d = -d
            if (r, c) == (n-1, n-1):
                return d
            nei = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for r1, c1 in nei:
                if check_bounds(r1, c1) and (r1, c1) not in visit:
                    d1 = min(d, min_dist[(r1, c1)])
                    heapq.heappush(maxHeap, (-d1, r1, c1))
                    visit.add((r1, c1))
        return 0
