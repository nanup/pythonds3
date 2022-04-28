def make_change(coin_value_list, change, min_coins, coins_used):
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_value_list if c <= cents]:
            if 1 + min_coins[cents - j] < coin_count:
                coin_count = 1 + min_coins[cents - j]
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[change]

def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin, end=" ")
        coin = coin - this_coin
    print()

def main():
    coin_value_list = [1, 5, 10, 25]
    change = 11
    coins_used = [0] * (change + 1)
    min_coins = [0] * (change + 1)
    

    print(f"Making change for {change} requires the following {make_change(coin_value_list, change, min_coins, coins_used)} coins", end = " ")

    print_coins(coins_used, change)
    print("The used list is as follows:")
    print(coins_used)

main()