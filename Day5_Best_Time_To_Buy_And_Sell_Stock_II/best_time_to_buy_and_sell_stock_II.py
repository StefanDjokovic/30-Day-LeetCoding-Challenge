# Could be probably a bit cleaner tbh

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0

        size_prices = len(prices)
        stonks = 0
        curr_low = prices[0]
        curr_low_bought = True

        for index, i in enumerate(prices):
            if index < size_prices - 1:
                if curr_low_bought:
                    if i > prices[index + 1]:
                        # print(f"Sold {curr_low} for {i}")     # fStrings are so nice to use
                        stonks += i - curr_low
                        curr_low_bought = False
                else:
                    if i < prices[index + 1]:
                        curr_low = i
                        curr_low_bought = True
            else:
                if curr_low_bought:
                    stonks += i - curr_low

        return stonks
