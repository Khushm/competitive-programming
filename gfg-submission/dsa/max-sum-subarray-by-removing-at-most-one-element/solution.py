class Solution:
    def maxSumSubarray(self, arr):
        keep = arr[0]
        dele = float('-inf')
        ans = arr[0]
        n = len(arr)
        
        for i in range(1, n):
            prev_ = keep
            
            # keep
            keep = max(keep+arr[i], arr[i])
            
            # dont keep
            dele = max(dele+arr[i], prev_)
            
            ans = max(dele, keep, ans)
        return ans
