# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

def majority_recur(array, left, right):
    """
    Use semi-open intervals.
    Time Complexity: O(nlogn)
    """
    if left == right:
        return 0
    if right - left == 1:
        return array[left]

    mid = left + (right - left) // 2   # half + 1

    left_elem = majority_recur(array, left, mid)
    right_elem = majority_recur(array, mid, right)

    l_cout = 0
    for i in range(left, right):
        if array[i] == left_elem:
            l_cout += 1
    if l_cout > (right - left)//2:
        return left_elem

    r_cout = 0
    for i in range(left, right):
        if array[i] == right_elem:
            r_cout += 1
    if r_cout > (right - left) // 2:
        return right_elem

    return 0

def majority_element(elements):
    assert len(elements) <= 10 ** 5
    # return bool(majority_recur(elements, 0, len(elements)))
    dict_eles = {}
    for ele in elements:
        dict_eles[ele] = 0

    for ele in elements:
        dict_eles[ele] += 1

    for count in dict_eles.values():
        if count > len(elements) // 2:
            return 1
    return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
