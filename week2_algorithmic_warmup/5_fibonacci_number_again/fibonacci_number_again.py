# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    # base case
    if n <= 1:
        return n

    previous = 0
    current = 1
    list_rem = [] # store the remanders
    list_rem.append(0)
    list_rem.append(1)

    # We only care about Fn mod m
    # The claim: (a + b) mod m = ((a mod m) + (b mod m))mod m
    # n-1 iterations leads to the Fn

    period = 0
    for i in range(1, n):
        temp_prev = previous
        previous = current
        current = (temp_prev + current) % m
        list_rem.append(current)

        if previous == 0 and current == 1:
            # Arrival of the period
            period = i;
            break;

    # Consider the case that the answer is present in the inital period
    if period > 0:
        rem = n % period
        return list_rem[rem]
    else:
        return list_rem[n]



if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
