from typing import List


class Solution:
    def printGraph(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        # code here
        ans = [[] for node in range(V)]
        for u, v in edges:
            ans[u].append(v)
            ans[v].append(u)
        return ans
