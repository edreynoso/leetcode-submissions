class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        
        dp = [0] * n

        dp[n-1] = prices[n-1]

        for i in range(n-2, -1, -1):

            dp[i] = max(dp[i+1], prices[i])

        profit = 0

        for i in range(n):

            profit = max(profit, dp[i] - prices[i])

        return profit


