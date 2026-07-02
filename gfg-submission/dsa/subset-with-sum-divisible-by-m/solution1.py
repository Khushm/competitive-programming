class Solution:
    def divisibleByK(self, arr, k):
        ans = set()
        n = len(arr)
        for i in range(n):
            rem = set()
            rem.add(arr[i] % k)
            for each in ans:
                rem.add((arr[i]+each)%k)
            if 0 in rem:
                return True
            ans |= rem
        return False
                
            
