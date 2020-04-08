class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        
        diff = 0
        j = 0
        for i, price in enumerate(prices[1:], start=1):
            
            if prices[i] - prices[i - 1] > 0:
                diff = prices[i] - prices[j]
            else:
                profit += diff
                j = i
                diff = 0
                
        return profit + diff    
            
class Solution {
    public int maxProfit(int[] prices) {
        int maxprofit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1])
                maxprofit += prices[i] - prices[i - 1];
        }
        return maxprofit;
    }
}
        
