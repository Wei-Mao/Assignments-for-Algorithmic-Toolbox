# python3

from itertools import permutations


def max_dot_product_naive(first_sequence, second_sequence):
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product


def max_dot_product(first_sequence, second_sequence):
    """
    Pair the items in the two sequences such that the sum of the products of the
    numbers is maximized.
    Args:
        first_sequence(List[int]):
        second_sequence(List[int]):

    Returns:
        result[int]: the maximum sum of the products.

    Time complexity: O(nlogn)
    """

    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    first_sequence_sorted = sorted(first_sequence, reverse=True)
    second_sequence_sorted = sorted(second_sequence, reverse=True)

    result = 0
    for a, b in zip(first_sequence_sorted, second_sequence_sorted):
        result += a * b

    return result


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
