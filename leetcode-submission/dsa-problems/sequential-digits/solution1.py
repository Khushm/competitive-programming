class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        ans = []
        low_len = len(str(low))
        hig_len = len(str(high)) + 1
        for width in range(low_len, hig_len):
            for start in range(10 - width):
                num = int(s[start:start+width])
                if num >= low and num <= high:
                    ans.append(num)
        return ans
