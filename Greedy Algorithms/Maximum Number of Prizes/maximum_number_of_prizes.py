# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    last_int, l, r = 0, 0, 0
    while True:
        l = last_int + 1
        r = n - l
        if l < r:
            summands.append(l)
            n = r
            last_int = l
        else:
            summands.append(n)
            break

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
