# python3

from collections import namedtuple
from sys import stdin
from typing import List

Segment = namedtuple('Segment', ['start', 'end'])


def is_point_in_seg(point: int, seg: Segment) -> bool:
    return seg.start <= point <= seg.end


def compute_optimal_points(segments: Segment) -> List[Segment]:
    """
    Time Complexity:
        O(nlogn) with n as the number of line segments.
    """
    sorted_segs = sorted(segments, key=lambda s: s.end)
    current_point = sorted_segs[0].end
    # num_of_points = 1
    point_set = [current_point]

    for seg in sorted_segs[1:]:
        if not is_point_in_seg(current_point, seg):
            current_point = seg.end
            # num_of_points += 1
            point_set.append(current_point)

    return point_set


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
