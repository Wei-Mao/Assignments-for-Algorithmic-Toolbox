# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt
from random import randint

Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def get_strip(points, idx_by_y, lb, ub):
    strip_idx = []
    for i in idx_by_y:
        if lb <= points[i].x <= ub:
            strip_idx.append(i)
    return strip_idx


def closet_pair(points, strip_idx, dlr):
    dmin = dlr
    for i in range(len(strip_idx)):
        j = i + 1
        while j <= i + 7 and j < len(strip_idx):
            dmin = min(dmin, distance_squared(points[strip_idx[i]],
                                              points[strip_idx[j]]))
            j += 1

    return dmin


def min_dist(points, idx_by_x, idx_by_y, start, end):
    # semi-open interval points[idx_x[start:end]]
    n = end - start
    if n <= 3:
        points_small = []
        for i in range(start, end):
            points_small.append(points[idx_by_x[i]])
        return minimum_distance_squared_naive(points_small)

    assert end >= start + 4
    mid = (start + end) // 2 + 1
    assert mid >= start + 2

    dl = min_dist(points, idx_by_x, idx_by_y, start, mid)
    dr = min_dist(points, idx_by_x, idx_by_y, mid, end)
    dlr = min(dl, dr)

    lb = points[idx_by_x[mid]].x - dlr
    ub = points[idx_by_x[mid]].x + dlr
    strip_idx = get_strip(points, idx_by_y, lb, ub)
    return closet_pair(points, strip_idx, dlr)


def minimum_distance_squared(points):
    idx_by_x = sorted(range(len(points)), key=lambda i: points[i].x)
    idx_by_y = sorted(range(len(points)), key=lambda i: points[i].y)
    return min_dist(points, idx_by_x, idx_by_y, 0, len(idx_by_x))


if __name__ == '__main__':
    # input_n = int(input())
    # input_points = []
    # for _ in range(input_n):
    #     x, y = map(int, input().split())
    #     input_point = Point(x, y)
    #     input_points.append(input_point)
    #
    # print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
    for n in [2, 5, 10, 100]:
        for max_value in [1, 2, 3, 1000]:
            points = []
            for _ in range(n):
                x = randint(-max_value, max_value)
                y = randint(-max_value, max_value)
                points.append(Point(x, y))
            if not minimum_distance_squared(points) ==\
                  minimum_distance_squared_naive(points):
                print(points)
                break
            else:
                print("Success!")