class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        n = len(s)

        dp = [0] * (n+1)

        for i in range(n -1):

            dp[i + 1] = dp[i] + (s[i] == "*")

        next_candle = [-1] * n
        last = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                last = i
            next_candle[i] = last

        prev_candle = [-1] * n
        last = -1
        for i in range(n):
            if s[i] == '|':
                last = i
            prev_candle[i] = last

        res = []
        for l, r in queries:
            left = next_candle[l]
            right = prev_candle[r]
            if left == -1 or right == -1 or left >= right:
                res.append(0)
            else:
                res.append(dp[right] - dp[left])

        return res
            
            
                
