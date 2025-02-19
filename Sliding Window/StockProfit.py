from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize two pointers: left (buy) and right (sell)
        left = 0
        right = 1
        # Track the maximum profit found
        max_profit = 0

        # Iterate through the prices array
        while right < len(prices):
            # If the current price is higher than the buy price, calculate profit
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                # Update max_profit if the current profit is greater
                max_profit = max(max_profit, profit)
            else:
                # If the current price is lower, move the buy pointer to the current position
                left = right
            # Move the sell pointer to the next day
            right += 1

        # Return the maximum profit found
        return max_profit
    
#Example Usage
solution = Solution()
prices = [8, 1, 9, 2, 10, 7]
print(solution.maxProfit(prices))

