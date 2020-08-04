# python3


def fibonacci_number_naive(n):
    # Exponential Time !
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    # base case
    if n == 0 or n == 1:
        return n

    prev = 0
    curruent = 1
    for k in range(2, n+1):
        temp = curruent
        curruent = curruent + prev
        prev = temp
    return curruent

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
