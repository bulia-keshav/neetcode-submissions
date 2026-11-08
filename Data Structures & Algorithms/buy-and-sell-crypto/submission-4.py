class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        l,r=0,0
        max_sf = prices[0]
        min_sf = prices[0]

        while r< len(prices):
            if max_sf < prices[r]: 
                max_sf = prices[r]
                profit = max_sf - min_sf
                if profit > max_profit: max_profit= profit
            if  prices[r]    < min_sf:
                l = r
                min_sf = prices[r]
                max_sf = prices[r]

            r+=1
        return max_profit