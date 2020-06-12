#! /usr/bin/python3
# Integers in Python 3 are of unlimited size. Hence no integer overflow problem

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0

    # max_product = max(max_product,
    # numbers[first] * numbers[second])





    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
