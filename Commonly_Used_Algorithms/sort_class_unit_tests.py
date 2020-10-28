import unittest
import random
import copy
from sort_class import Sort

class TestSortClass_QuickSort(unittest.TestCase):
    def test_quick_sort(self):
        sort_methods = Sort()
        # Stress Testing
        test_state = True
        stat_value = -100
        end_value = 100
        num_eles = 20
        max_iter = 1000000
        iter = 0
        while iter < max_iter:
            array = [random.randint(stat_value, end_value) for _ in range(num_eles)]
            array_cp = copy.deepcopy(array)
            sort_methods.selection_sort(array)
            sort_methods.quick_sort(array_cp)
            for a, b in zip(array, array_cp):
                self.assertEqual(a, b)
            iter += 1

if __name__ == "__main__" :
    unittest.main()