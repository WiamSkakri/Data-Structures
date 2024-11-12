class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # This is using brute force:
        # constant space complexity 
        # time complexity of O(n^2)

        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                res = max(res, sell - buy)
        return res
    
    
        # Now let us use two pointers:
    def maxProfit(self, prices: List[int]) -> int:
        # This has a constant space complexity
        # This has a linar time complexity
        l, r = 0, 1
        maxP = 0

        while (r < len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
    
    
    
    def maxProfit(self, prices: List[int]) -> int:
        # This is using dynamic programing
        # This has a constant space complexity
        # This has a linear space complexity
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP