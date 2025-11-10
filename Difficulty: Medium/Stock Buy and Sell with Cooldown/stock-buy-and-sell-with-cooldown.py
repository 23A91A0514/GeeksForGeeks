class Solution:
    def maxProfit(self, arr):
        # code here
        n = len(arr)
        dp = [[0]*4 for _ in range(n)]
        # 4 states: buy, sell, with-stock-donothing, without-stock-donothing
        dp[0][0] = -arr[0]          # buy
        dp[0][1] = float('-inf')    # sell
        dp[0][2] = 0                # without-stock-donothing
        dp[0][3] = float('-inf')    # with-stock-donothing
        
        for i in range(1, n):
            # buy
            dp[i][0] = dp[i-1][2] - arr[i]
            # sell
            dp[i][1] = max(dp[i-1][0], dp[i-1][3]) + arr[i]
            # no socks in hand, do nothing in this step
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
            # with stock in hand,  do nothing in this step
            dp[i][3] = max(dp[i-1][3], dp[i-1][0])
        
        return max(dp[-1])