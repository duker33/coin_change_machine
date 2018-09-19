from machine import get_coins_to_give

input_ = """4
5 10
3 2
2 12
1 3
16"""

input_4 = """2
5 1000
1"""

input_3 = """1
1 0
0"""


def input():
    _, *pairs, sum_to_give = input_.split('\n')
    coins_inside = dict(tuple(iter(map(int, p.split(' ')))) for p in pairs)
    return coins_inside, int(sum_to_give)


def output(coins_to_give):
    if isinstance(coins_to_give, dict) and bool(coins_to_give):
        result = '\n'.join(
            f'{nominal} {count}'
            for nominal, count in sorted(coins_to_give.items(), reverse=True)
        )
        print(result)
    else:
        print('0')


def run():
    coins_inside, sum_to_give = input()
    coins_to_give = get_coins_to_give(coins_inside, sum_to_give)
    output(coins_to_give)


run()
