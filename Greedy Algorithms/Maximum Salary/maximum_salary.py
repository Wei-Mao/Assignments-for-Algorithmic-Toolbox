# python3

from itertools import permutations
from functools import cmp_to_key

def largest_number_naive(numbers):
    numbers = list(map(str, numbers))  # list of str

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest

def compare(number, max_number):
    num_max = int(str(number) + str(max_number))
    max_num = int(str(max_number) + str(number))

    if num_max > max_num:
        return 1
    elif num_max < max_num:
        return -1
    else:
        return 0


def largest_number(numbers):
    numbers_sorted = sorted(numbers, key=cmp_to_key(compare), reverse=True)
    largest = list(map(str, numbers_sorted))
    largest = int("".join(largest))
    return largest
if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))  # List[Int]
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
