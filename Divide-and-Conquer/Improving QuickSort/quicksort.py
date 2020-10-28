# python3

from random import randint
from typing import List, Union

def swap_in_list(array, a, b):
    array[a], array[b] = array[b], array[a]

def partition3(array: List[Union[float, int]] , left: [int], right: [int]) -> int:
    """
    Partition the subarray array[left,right] into three parts such that:
    array[left, m1-1] < pivot
    array[m1, m2] == pivot
    array[m2+1, right] > pivot
    The above is also the loop invariant, which should hold prior to the loop and
    from iteration to iteration to ensure the correctness of the algorithm.(right
    is replaced by the loop variable i - 1)

    Args:
        array(List[Union[float, int]]): Reference to the original array.
        left(int): Left index of the subarray.
        right(int): Right index of the subarray.

    Returns:
        m1[int], m2[int]: array[m1,..., m2] == pivot and in their final positions.

    Time Complexity: O(right - left)
    Space Complexity: O(1)
    """
    pivot_idx = randint(left, right)
    pivot = array[pivot_idx]
    # print(pivot)
    # Move the pivot to the start of the subarray.
    swap_in_list(array, left, pivot_idx)

    # loop invariant:
    # array[left, m1-1] < pivot if m1 > left or empty if m1=left
    # array[m1, m2] ==  pivot
    # array[m2+1, i-1] > pivot if i > m2 + 1 or empty
    m1, m2 = left, left
    for i in range(left + 1, right + 1):
        if array[i] < pivot:
            swap_in_list(array, i, m1)
            m1 += 1
            m2 += 1
            swap_in_list(array, i, m2)
        elif array[i] == pivot:
            m2 += 1
            swap_in_list(array, i, m2)
    return m1, m2

def randomized_quick_sort(array, left, right):
    """
    Time Complexity: O(nlogn) on average  and O(n^2) in the worst case.
    Space Complexity: O(logn) in worst case
    """
    while left < right:
        m1, m2 = partition3(array, left, right)
        # array[left, m1-1] < pivot
        # array[m1, m2] == pivot
        # array[m2+1, right] > pivot
        if (m1 - left) < (right - m2):
            randomized_quick_sort(array, left, m1-1)
            left = m2 + 1
        else:
            randomized_quick_sort(array, m2+1, right)
            right = m1 - 1



if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
    # input_array = [randint(-10, 10) for _ in range(6)]
    # input_array.append(input_array[0])
    # print(input_array)
    # m1, m2 = partition3(input_array, 0, 6)
    # print(input_array)
    # print(f"m1 {m1} and m2 {m2}")
