class Solution:
    def minMaxCandy(self, prices, k):
        prices.sort()
        n = len(prices)
        
        min_cost = 0
        i = 0
        j = n - 1
        while i <= j:
            min_cost += prices[i]
            i += 1
            j -= k

        max_cost = 0
        i = n - 1
        j = 0
        while i >= j:
            max_cost += prices[i]
            i -= 1
            j += k

        return [min_cost, max_cost]
