class Solution:
    @staticmethod
    def _profit_from_index(j, arr) -> int:
        if j >= len(arr): return 0
        prev = arr[j]
        g = 0
        for i in range(j, len(arr)):
            prev = min(prev, arr[i])
            g = max(g, prev - arr[i])
        return g
    def maxProfit(self, arr: list[int]) -> int:
        g = 0
        prev = arr[0]
        for i in range(len(arr)):
            prev = min(prev, arr[i])
            if prev - arr[i] > 0:
                print(prev - arr[i])
                g = max((prev - arr[i] + self._profit_from_index(i + 1, arr)),g )
        return g 
