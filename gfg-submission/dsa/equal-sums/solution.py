class Solution:
    def equalSum(self, arr ):
        total_sum = sum(arr)
        left_sum = 0
        n = len(arr)
        ans = [float('inf'), -1, 1]
        for i in range(n):
            left_sum = left_sum + arr[i]
            right_sum = total_sum - left_sum
            diff = left_sum - right_sum
            # print(total_sum, left_sum, right_sum, diff)
            if abs(diff) < ans[0]:
                # print(abs(diff), ans[0])
                if diff < 0:
                    ans = [abs(diff), i+2, 1]
                else:
                    ans = [abs(diff), i+2, 2]
        # print(ans)
        return ans

# t = 26
# l = 3, r = 22   -> 19
# l = 5, r = 21   -> 16
# l = 6, r = 20   -> 14
# l = 11, r = 15   -> 4
# l = 18,r = 8    -> 10
# l = 26,r = 0    -> 26
