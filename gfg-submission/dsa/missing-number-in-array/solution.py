class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr)+1
        sum = 0
        for i in range(n-1):
            sum = sum+arr[i]
            
        return ((n*(n+1))//2) - sum
