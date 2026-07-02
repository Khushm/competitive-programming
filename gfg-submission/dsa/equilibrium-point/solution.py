class Solution:
    def findEquilibrium(self, arr):
        # code here
        n = len(arr)
        prefix = [0] * n
        suffix = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] + arr[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] + arr[i+1]
        for i in range(n):
            if prefix[i] == suffix[i]:
                return i
        return -1
