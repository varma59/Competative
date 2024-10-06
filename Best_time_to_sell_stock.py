def maxProfit(prices):
    if len(prices) < 2:
        return 0
        
    min_price = float('inf') # Initializes the minimum price as infinity, so any price encountered will be lower than this and update the minimum.
    max_price = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_price = max(max_price, price - min_price)
    return max_price
    
prices_list = [
    [],  # Empty list
    [5],  # Single element
    [7, 6, 4, 3, 1],  # Decreasing prices
    [3, 3, 3, 3],  # All prices the same
    [7, 1, 5, 3, 6, 4],  # Normal case with profit
    [2, 4, 1],  # Another normal case
]

for prices in prices_list:
    print(f"Prices: {prices} -> Maximum Profit: {maxProfit(prices)}")
