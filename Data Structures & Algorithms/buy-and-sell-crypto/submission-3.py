class Solution:

    def maxOfRemaining(self, prices: List[int], startingIndex):
        maxValue = prices[startingIndex]
        for i in range(startingIndex, len(prices)):
            if maxValue <= prices[i]:
                maxValue = prices[i]
        return maxValue

    def maxProfit(self, prices: List[int]) -> int:
        currentProfit = 0
        for i in range(0, len(prices)-1):
            ifIBuyToday = prices[i]
            sellDayValue = self.maxOfRemaining(prices, i + 1)
            currentDiff = sellDayValue - ifIBuyToday
            if currentDiff > currentProfit:
                currentProfit = currentDiff
        
        return currentProfit
        