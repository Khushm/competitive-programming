from collections import defaultdict

class Solution:
    def findDuplicates(self, arr):
        # code here
        ans = []
        hash_ = defaultdict(int)
        n = len(arr)
        
        for i in range(n):
            hash_[arr[i]] += 1
        for key, val in hash_.items():
            if val > 1:
                ans.append(key)
        return ans
