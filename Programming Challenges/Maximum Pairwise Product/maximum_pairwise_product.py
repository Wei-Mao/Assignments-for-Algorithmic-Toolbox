# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    max_idx = 0
    max_num = 0
    for idx, number in enumerate(numbers):
        if(number > max_num):
            max_num = number
            max_idx = idx

    max_idx_next = 0
    max_num_next = 0
    for idx, number in enumerate(numbers):
        if(number > max_num_next and idx != max_idx):
            max_num_next = number
            max_idx_next = idx

    print(max_idx_next, max_idx)


    return numbers[max_idx] * numbers[max_idx_next]






if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
