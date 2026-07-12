class Solution:
    def maxAmount(self, arr, k):
        MOD = 10**9 + 7
        n = len(arr)
        pq = [-x for x in arr]
        heapq.heapify(pq)
        ans = 0
        while k and pq:
            num = heapq.heappop(pq)
            #print(num)
            num = -num
            ans += num
            if num > 0:
                heapq.heappush(pq, (-(num-1)))
            k-=1
        return ans % MOD
