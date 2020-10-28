# python3

from sys import stdin


def maximum_loot_value(capacity: int, weights: int, prices: int) -> float:
    """
    Fractional Knapsack Problem using Greedy Algorithm
    Args:
        capacity(int): The capacity of the knapsack.
        weights(List[int]): The weights for the items.
        prices(List[int]): The values for the items.

    Returns:
        V(float): The maximum possible value of the items fitting
            into the knapsack.

    """
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    # Sort the indices in descending order of the value per unit of weight
    n = len(weights)
    sorted_idx = sorted(range(n), key=lambda k: prices[k] / weights[k], reverse=True)

    V = 0  # total value in the kanpsack
    # A = [0]*n
    for i in sorted_idx:
        if capacity == 0:
            # Knapsack is full.
            return V

        # Use as much of the item with max. value per unit of weight as possible
        a = min(weights[i], capacity)
        V += a * float(prices[i]) / float(weights[i])
        capacity -= a
        # A[i] = a
    # All items are fitted into the knapsack
    return V


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
