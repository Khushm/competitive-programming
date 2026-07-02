class Solution:
    def findEquilibrium(self, arr):
        # code here
        total_sum = sum(arr)
        left_sum = 0
        n = len(arr)
        for i in range(n):
            right_sum = total_sum - left_sum - arr[i]
            if left_sum == right_sum:
                return i
            left_sum += arr[i]
        return -1
