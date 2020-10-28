# python3

from itertools import combinations
from typing import List, Union


def compute_inversions_naive(a):
    number_of_inversions = 0
    num_elements = len(a)
    for i in range(num_elements):
        for j in range(i + 1, num_elements):
            if a[i] > a[j]:
                number_of_inversions += 1
    return number_of_inversions


def _merge_sort(A: List[Union[int, float]], left: int, right: int):
    """
    Adopt semi-open interval for the recursive merge_sort.

    Examples:
        [left, right) = {left, left+1,..., right - 1}
        # of numbers in the interval [left, right) = right - left
        [left, right) = [left, middle) U [middle, right)
    """
    # base case depending on how to split the problem.
    # Like all binary searches, base case means 0 or 1 element left.
    if right - left <= 1:
        # right -left could be 0!!!
        return 0

    middle = (left + right) // 2  # [a, a+1) results in middle == a
    num_inv_left = _merge_sort(A, left, middle)
    num_inv_right = _merge_sort(A, middle, right)
    num_inv_btw = _merge(A, left, middle, right)
    return num_inv_left + num_inv_right + num_inv_btw


def _merge(A: List[Union[int, float]], left: int, middle: int, right: int):
    """
     We use semi-open intervals, which means [left, middle), [middle, right)
     Time Complexity: O(right - left).
     Space Complexity: O(A.length + (right - left))
     """
    sorted_part = []
    left_ptr = left
    right_ptr = middle
    num_inv = 0
    while left_ptr < middle and right_ptr < right:
        # print(left_ptr, right_ptr, len(A))
        if A[left_ptr] <= A[right_ptr]:
            # Move A[left_ptr] to the resulting list.
            sorted_part.append(A[left_ptr])
            left_ptr += 1
        else:
            num_inv += (middle - left_ptr)
            sorted_part.append(A[right_ptr])
            right_ptr += 1

    if left_ptr < middle:
        sorted_part.extend(A[left_ptr:middle])

    if right_ptr < right:
        sorted_part.extend(A[right_ptr:right])

    A[left:right] = sorted_part
    return num_inv


def compute_inversions(a):
    num_inv = _merge_sort(a, 0, len(a))
    return num_inv

if __name__ == '__main__':
    # input_n = int(input())
    # elements = list(map(int, input().split()))
    elements = [3, 2, 1]
    # assert len(elements) == input_n
    print(compute_inversions(elements))
    print(elements[1:1])
    print(list(range(1,1)))
