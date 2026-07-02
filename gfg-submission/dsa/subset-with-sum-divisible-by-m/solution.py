from functools import lru_cache


class Solution:
    def divisibleByK(self, arr, k):

        dp = [False] * k

        for num in arr:
            nxt = dp[:]

            nxt[num % k] = True

            for rem in range(k):
                if dp[rem]:
                    nxt[(rem + num) % k] = True

            dp = nxt

            if dp[0]:
                return True

        return False
