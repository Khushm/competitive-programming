class Solution:
    def getCount(self, n):
        # x = (n - k(k-1)/2) / k
        ans = 0
        k = 2
        while k * (k - 1) // 2 < n:
            num = n - k * (k - 1) / 2
            if num % k == 0:
                ans += 1
            k+= 1
        return ans
