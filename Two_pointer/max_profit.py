"""""""""""""""""""""
💡 Problem: Best Time to Buy and Sell Stock
📘 Given:
An array prices where prices[i] is the price of a given stock on the i-th day.
🧪 Task:
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve. If no profit is possible, return 0.
"""""""""""""""""""""

prices = [7, 1, 5, 3, 6, 4]
# Output: 5
# Buy at 1, sell at 6 → profit = 6 - 1 = 5

def max_profit(prices):
    max_prof = 0
    min_price = float("inf")
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_prof = max(max_prof, profit)
    return max_prof
print(max_profit(prices))



