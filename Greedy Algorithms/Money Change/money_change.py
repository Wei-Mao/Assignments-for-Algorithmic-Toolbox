# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    denominations = [10, 5, 1]
    num_coins = 0
    while money:
        # extract the max possible value
        for coin in denominations:
            if coin <= money:
                num_coins += 1
                money -= coin
                break
    return num_coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
