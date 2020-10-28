# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search_recur(array, left, right, key):
    # base case 1: not found
    if left > right:
        return -1

    mid = (left + right) // 2
    # print("mid", mid)
    if array[mid] == key:
        return mid
    elif key > array[mid]:
        return binary_search_recur(array, mid + 1, right, key)
    else:
        return binary_search_recur(array, left, mid - 1, key)
def timer(func):
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        return end_time - start_time

    return wrapper_timer



def binary_search(keys, query, mode='recursive'):
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4
    if mode == 'recursive':
        return binary_search_recur(keys, 0, len(keys) - 1, query)
    else:
        left, right = 0, len(keys) - 1
        while left <= right:
            mid = (left + right) // 2
            if keys[mid] == query:
                return mid
            elif query > keys[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

import time
def timer(func):
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        return end_time - start_time

    return wrapper_timer


if __name__ == '__main__':
    # input_keys = list(map(int, input().split()))[1:]
    # input_queries = list(map(int, input().split()))[1:]
    #
    # for q in input_queries:
    #     print(binary_search(input_keys, q), end=' ')

    import random, time
    input_keys = [2 * k + 1 for k in range(10000)]
    input_query = input_keys[100]
    binary_search_timer = timer(binary_search)
    print("Recursive time: ", binary_search_timer(input_keys, input_query, mode='recursive'))
    print("Iterative time: ", binary_search_timer(input_keys, input_query, mode='iterative'))