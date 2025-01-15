import time

coints_list = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(rest, coins):
    coints_list = sorted(coins, reverse=True)
    result = {}
    index = 0
    while rest >= 0 and index < len(coints_list):
        if coints_list[index] <= rest:
            rest -= coints_list[index]
            if coints_list[index] in result:
                result[coints_list[index]] += 1
            else:
                result[coints_list[index]] = 1
        else:
            index += 1
    return result


def find_min_coins(rest, coins):
    dyn_prg = [float("inf")] * (rest + 1)
    dyn_prg[0] = 0
    used_coins = [0] * (rest + 1)

    for i in range(1, rest + 1):
        for coin in coins:
            if i >= coin and dyn_prg[i - coin] + 1 < dyn_prg[i]:
                dyn_prg[i] = dyn_prg[i - coin] + 1
                used_coins[i] = coin

    if dyn_prg[rest] == float("inf"):
        return {}

    result = {}
    while rest > 0:
        for coin in coins:
            if rest >= coin and dyn_prg[rest] == dyn_prg[rest - coin] + 1:
                result[coin] = result.get(coin, 0) + 1
                rest -= coin
                break
    return result


def main():
    rest = 50271
    time_start = time.time()
    res_greedy = find_coins_greedy(rest, coints_list)
    time_end = time.time()
    print("Жадібний алгоритм")
    print(f"Результат: {res_greedy}")
    print(f"Час виконання: {time_end - time_start}")
    time_start = time.time()
    res_dp = find_min_coins(rest, coints_list)
    time_end = time.time()
    print("\nДинамічне програмування")
    print(f"Результат: {res_dp}")
    print(f"Час виконання: {time_end - time_start}")


if __name__ == "__main__":
    main()
