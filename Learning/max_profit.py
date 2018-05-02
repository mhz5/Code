def max_profit(prices):
    if not prices:
        return 0
    buy = -123123123123
    cd = 0
    sell = 0

    for p in prices:
        buy = max(buy, cd - p)
        cd = max(sell, cd)
        sell = buy + p

    return max(sell, cd)


print max_profit([1, 2, 3, 0, 2])