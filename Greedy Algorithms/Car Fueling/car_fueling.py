# python3

def compute_min_number_of_refills(d: int, m: int, stops: list):
    """
    O(n) with n as the number of the gas stations.
    """
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d
    n = len(stops)
    stops_dest = stops.copy()
    stops_dest.append(d)
    stops_dest.insert(0, 0)
    num_refills = 0
    current_refill = 0
    last_refill = 0
    while current_refill <= n:
        while (current_refill <= n and
               stops_dest[current_refill + 1] - stops_dest[last_refill] <= m):
            current_refill += 1
        if current_refill == last_refill:
            # The next gas stations is unreachable.
            return -1
        # Not arrive the destination yet.
        # if current_refill <= n:
            num_refills += 1
        last_refill = current_refill
    return num_refills

if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
