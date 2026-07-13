from math import ceil
class Solution:
    def find(self, arr):
        need = 1
        
        for i in range(len(arr)-1, -1, -1):
            old = ceil((need + arr[i])/2)
            need = old
        return need
