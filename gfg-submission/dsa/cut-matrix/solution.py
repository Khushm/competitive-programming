from functools import lru_cache, cache

class Solution:
    def findWays(self, matrix, k):
        MOD = 10**9 + 7
        n = len(matrix)
        m = len(matrix[0])
        
        total = 0
        suf = [[0] * m for _ in range(n)]
        
        # print(suffix)
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                bottom = suf[i+1][j] if i+1 < n else 0
                right = suf[i][j+1] if j+1 < m else 0
                diagonal = suf[i+1][j+1] if i+1 < n and j+1 < m else 0
                
                suf[i][j] = matrix[i][j] + bottom + right - diagonal
                
        # mem = [[[-1] * (k+1) for _ in range(m)] for __ in range(n)]
        @cache
        def dp(r, c, cuts):
            # base
            if cuts == 0:
                return 1 if suf[r][c] > 0 else 0
            if suf[r][c] == 0:
                return 0
            ways = 0
            #if mem[r][c][cuts] != -1:
            #    return mem[r][c][cuts]
                
            # horizontal
            for i in range(r+1, n):
                # top_has_one = suf[r][c] - suf[i][c] > 0
                if suf[r][c] > suf[i][c]:
                    ways = (ways + dp(i, c, cuts-1)) % MOD
            
            # vertical
            for j in range(c+1, m):
                # left_has_one = suf[r][c] - suf[r][j] > 0
                if suf[r][c] > suf[r][j]:
                    ways = (ways + dp(r, j, cuts-1)) % MOD
            #mem[r][c][cuts] = ways
            return ways
       
        return dp(0, 0, k-1)
