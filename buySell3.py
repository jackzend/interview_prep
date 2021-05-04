prices = [0,1,3,2,4]

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    k = 2
    if not prices:
        return 0

    K = k + 1
    n = len(prices)
    dp = [[0] * n for _ in range(K)]

    for k in range(1, K):
        min_p = prices[0]
        for i in range(1, n):
            min_p = min(min_p, prices[i] - dp[k - 1][i - 1])
            dp[k][i] = max(dp[k][i - 1], prices[i] - min_p)
    return dp[-1][-1]


print(maxProfit(prices))