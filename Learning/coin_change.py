import sys

def coin_change(coins, amount):
    return cc_helper(coins, amount, 0)


def cc_helper(coins, amount, num_coins):
    if amount == 0:
        return num_coins
    if amount < 0:
        return -1

    max_coins = sys.maxsize
    min_coins = max_coins
    for c in coins:
        if amount - c < 0:
            continue
        x_coins = cc_helper(coins, amount - c, num_coins + 1)
        if x_coins < 0:
            continue
        min_coins = min(min_coins, x_coins)
        print min_coins, x_coins, max_coins

    return min_coins if min_coins < max_coins else -1


# def coin_change(coins, amount):
#     max_val = amount + 1
#     arr = [max_val for _ in range(max_val)]
#     arr[0] = 0
#     for i in range(0, max_val):
#         val = arr[i]
#         for c in coins:
#             idx = i + c
#             if idx > amount:
#                 continue
#             arr[idx] = min(val + 1, arr[idx])
#
#     res = arr[amount]
#     return res if res < max_val else -1


# t1 = coin_change([1,2,5], 11)
# print(t1)

t2 = coin_change([1], 2)
print(t2)




