# python3

from sys import stdin


def maximum_gold(capacity, weights):
    """
    Sub-problem:
    max_weight(c, i) is the maximum weight using first i weights. 0<= i <=i

    Guess:
    itn Golden Bar is used or not

    Recurrence:
    max_weight(c, i) = max {max_weight(c, i-1),  max_weight(c - weight[i], i-1) + weight[i]}
    for c in [0, capacity] and i in [0, len(weights)]

    Base case:
    max_weight[0, i] = 0, max_weight[i, 0] = 0
    weight of 0th item is infinite.
    Note the index offset between weights and max_weight
    """
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)
    n = len(weights)
    max_weight = [[0 for _ in range(n+1)] for _ in range(capacity + 1)]

    for c in range(1, capacity + 1):
        for i in range(1, n+1):
            max_weight[c][i] = max_weight[c][i-1]
            if weights[i-1] <= c:
                val = max_weight[c - weights[i-1]][i-1] + weights[i-1]
                if val > max_weight[c][i]:
                    max_weight[c][i] = val

    # Construct the solution.
    c , i= capacity + 1, n + 1
    selected = []
    while i:
        if max_weight[c][i] == max_weight[c][i-1]:
            i = i -1
        elif max_weight[c][i] == max_weight[c - weights[i-1]][i-1] + weights[i-1]:
            selected.append(i-1)
            c -= weights[i-1][i-1]
            i -= 1

    # print(max_weight)
    return max_weight[capacity][n]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
