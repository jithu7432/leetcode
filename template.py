class Solution:
    def minFallingPathSum(self, arr: list[list[int]]) -> int:
        m, n = len(arr), len(arr[0])
        for i in range(1, m):
            for j in range(n):
                arr[i][j] += min(arr[i - 1][max(0, j - 1): j + 2])

        return min(arr[-1])
