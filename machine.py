from collections import defaultdict


def get_coins_to_give(coins_inside, sum_to_give: int):
    if sum_to_give <= 0:
        return defaultdict(int)
    if sum_to_give < 0:
        return 0

    nominal = next(
        (k for k, v in coins_inside.items() if v > 0 and sum_to_give - k >= 0),
        0
    )
    if nominal == 0:
        return 0

    coins_inside[nominal] -= 1

    coins_to_give = get_coins_to_give(coins_inside, sum_to_give - nominal)
    if coins_to_give == 0:
        return 0
    coins_to_give[nominal] += 1
    return coins_to_give
