# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple

def gcd_fast(a, b):
    if a < b:
        temp = a
        a = b
        b = temp

    if b == 0:
        return a
    a = a % b
    return gcd_fast(a, b)

def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    gcd = gcd_fast(a, b)
    prd = a * b
    return prd / gcd


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
