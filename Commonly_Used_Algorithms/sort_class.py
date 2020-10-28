from typing import List, Union, NoReturn
import copy
import random
from random import randint
from collections import deque


class Sort:
    """
    Sort in the given list of numbers in ascending order.
    """
    def insertion_sort(self, array: List[Union[float, int]]) -> NoReturn:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1), in place sorting.
        Recall that only mutable object is passed by reference like list, 
        """
        for i in range(1, len(array)):
            j = i - 1
            key = array[i]
            while j >= 0 and array[j] > key:
                # Once we find one element larger than key
                # move it by one position to the right
                array[j + 1] = array[j]
                j -= 1

            # Right the position to insert key in is j + 1
            array[j + 1] = key

    def selection_sort(self, array: List[Union[float, int]]) -> NoReturn:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1) in place sorting.
        """
        list_size = len(array)
        for i in range(list_size):
            # Loop invariant: ith smallest element is placed in the ith position in the list
            # sub_list = array[i:]
            # min_num_idx = min(range(len(sub_list)), key=lambda k: sub_list[k])
            # min_num_idx += i
            _, min_num_idx = self._min(array, i, list_size-1)
            array[i], array[min_num_idx] = array[min_num_idx], array[i]

    def bubble_sort(self, array: List[Union[float, int]]) -> NoReturn:
        """
        O(n^2)  in place sorting.

        Basic Idea: At the ith iteration, push the ith largest tot the end  of list.
        """
        num_of_eles = len(array)
        for i in range(num_of_eles):
            for j in range(num_of_eles - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

    def merge_sort(self, array):
        """
        Time Complexity: O(nlogn) with n as array.length
        Space Complexity: O(n)
        """
        self._merge_sort(array, 0, len(array))

    def partition3(self, array: List[Union[float, int]], left: [int], right: [int]) -> int:
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
        self._swap_in_list(array, left, pivot_idx)

        # loop invariant:
        # array[left, m1-1] < pivot if m1 > left or empty if m1=left
        # array[m1, m2] ==  pivot
        # array[m2+1, i-1] > pivot if i > m2 + 1 or empty
        m1, m2 = left, left
        for i in range(left + 1, right + 1):
            if array[i] < pivot:
                self._swap_in_list(array, i, m1)
                m1 += 1
                m2 += 1
                self._swap_in_list(array, i, m2)
            elif array[i] == pivot:
                m2 += 1
                self._swap_in_list(array, i, m2)
        return m1, m2

    def randomized_quick_sort(self, array, left, right, mode='recursive'):
        """
        Trick: Tail recursion elimination for small stack consumption.
        Time Complexity: O(nlogn) on average  and O(n^2) in the worst case.
        Space Complexity: O(logn) in worst case
        """
        if mode == 'recursive':
            while left < right:
                m1, m2 = self.partition3(array, left, right)
                # array[left, m1-1] < pivot
                # array[m1, m2] == pivot
                # array[m2+1, right] > pivot
                if (m1 - left) < (right - m2):
                    self.randomized_quick_sort(array, left, m1 - 1)
                    left = m2 + 1
                else:
                    self.randomized_quick_sort(array, m2 + 1, right)
                    right = m1 - 1
        else:
            # Iterative version of quick sort.
            stack = deque()  # empty stack
            stack.append(left)
            stack.append(right)
            while stack:
                # Stack implements Last-in First-out logic
                r = stack.pop()
                l = stack.pop()
                m1, m2 = self.partition3(array, l, r)

                if m1 - l > 1:
                    # Add the part to the left of the array[m1, m2] to stack.
                    stack.append(l)
                    stack.append(m1 - 1)

                if r - m2 > 1:
                    # Push the part to the right of the array[m1,m2] to stack.
                    stack.append(m2 + 1)
                    stack.append(r)

    def quick_sort(self, array: List[Union[int, float]]):
        self.randomized_quick_sort(array, 0, len(array) - 1, mode='iterative')

    def heap_sort(self):
        pass

    def _merge_sort(self, A: List[Union[int, float]], left: int, right: int):
        """
        Adopt semi-open interval for the recursive merge_sort.

        Examples:
            [left, right) = {left, left+1,..., right - 1}
            # of numbers in the interval [left, right) = right - left
            [left, right) = [left, middle) U [middle, right)
        """
        # base case depending on how to split the problem.
        if right - left <= 1:
            # right -left could be 0!!!
            return None

        middle = (left + right) // 2  # [a, a+1) results in middle == a
        self._merge_sort(A, left, middle)
        self._merge_sort(A, middle, right)
        self._merge(A, left, middle, right)

    def _merge(self, A: List[Union[int, float]], left: int, middle: int, right: int):
        """
         We use semi-open intervals, which means [left, middle), [middle, right)
         Time Complexity: O(right - left).
         Space Complexity: O(A.length + (right - left))
         """
        sorted_part = []
        left_ptr = left
        right_ptr = middle
        while left_ptr < middle and right_ptr < right:
            # print(left_ptr, right_ptr, len(A))
            if A[left_ptr] < A[right_ptr]:
                # Move A[left_ptr] to the resulting list.
                sorted_part.append(A[left_ptr])
                left_ptr += 1
            else:
                sorted_part.append(A[right_ptr])
                right_ptr += 1

        if left_ptr < middle:
            sorted_part.extend(A[left_ptr:middle])

        if right_ptr < right:
            sorted_part.extend(A[right_ptr:right])

        A[left:right] = sorted_part
        # print(len(A), len(sorted_part))

    def _min(self, A: List[Union[float, int]], start: int, end: int):
        """ Adopt Closed Interval [start, end] """
        min_idx = -1
        min_val = float('inf')
        for idx in range(start, end + 1):
            if A[idx] < min_val:
                min_val = A[idx]
                min_idx = idx

        return min_val,  min_idx

    def _swap_in_list(self, array, a, b):
        array[a], array[b] = array[b], array[a]


if __name__ == "__main__":
    sort_methods = Sort()

    # Stress Testing
    test_state = True
    stat_value = -10000
    end_value = 10000
    num_eles = 1000
    while test_state:
        array = [random.randint(stat_value, end_value) for _ in range(num_eles)]
        array_cp = copy.deepcopy(array)
        sort_methods.selection_sort(array)
        sort_methods.quick_sort(array_cp)
        for a, b in zip(array, array_cp):
            if a != b:
                print("Fail")
                test_state = False
                break
            else:
                print("Success!")
