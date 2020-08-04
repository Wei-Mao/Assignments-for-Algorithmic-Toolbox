# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10

def fibonacci_number_fast(n, m):
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

def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    last_digit_of_Fn = fibonacci_number_fast(n, 10)
    last_digit_of_Fn_plus_1 = fibonacci_number_fast(n + 1, 10)

    return (last_digit_of_Fn * last_digit_of_Fn_plus_1) % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
