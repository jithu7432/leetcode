class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = res = len(arr)
        dp = [n] * (n+1)
        i = 0
        c = 0
        for j in range(len(arr)):
            c += arr[j]
            while c > target:
                c -= arr[i]
                i += 1
            dp[j+1] = dp[j]
            if c == target:
                res = min(res, dp[i] + j-i+1)
                dp[j+1] = min(dp[j], j-i+1)
        # print(dp, res)
        return res if res != n else -1
