def maximumToys(prices, k):
    # Write your code here
    bought = 0
    prices = sorted(prices)
    for price in prices:
        if price < k:
            k -= price
            bought += 1
    return bought