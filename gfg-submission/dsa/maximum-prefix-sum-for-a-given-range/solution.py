class Solution:
    def maxPrefixes(self, arr, leftIndex, rightIndex):
        # code here.
        ans = [0] * len(leftIndex)
        for i in range(len(leftIndex)):
            max_ = float('-inf')
            summ = 0
            for j in range(leftIndex[i], rightIndex[i]+1):
                summ += arr[j]
                max_ = max(summ, max_)
            ans[i] = max_
        return ans
