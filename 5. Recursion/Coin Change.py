def coin_change(coin_value_list, change, known_results):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [ch for ch in coin_value_list if ch <= change]:
            num_coins = 1 + coin_change(coin_value_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
            known_results[change] = min_coins
    return min_coins
    
print(coin_change([1, 5, 10, 25], 63, [0] * 64))