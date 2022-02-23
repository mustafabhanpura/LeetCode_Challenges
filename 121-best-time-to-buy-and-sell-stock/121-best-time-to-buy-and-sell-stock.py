class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_stock = 0
        sell_stock = 1
        max_profit = 0
        while sell_stock <len(prices):
            current_profit = prices[sell_stock] - prices[buy_stock]
            
            if prices[buy_stock]<prices[sell_stock]:
                max_profit= max(max_profit,current_profit)
            else:
                buy_stock = sell_stock
            sell_stock +=1
        return max_profit