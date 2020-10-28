# python3

def lcs2(s1: str, s2: str) -> int:
    """
   Time Complexity: O(mn)
   Space Complexity: O(mn)
   Viewed as Edit Distance Problem.
   """
    if not s1 or not s2:
        return 0

    m, n = len(s1), len(s2)
    # Prepend a zero to the both of the two strings for good start.
    # D = np.zeros((m + 1, n + 1), dtype=np.int)
    D = [[0 for _ in range(n+1)] for _ in range(m+1)]
    # D[0][0:] = 0
    # D[0:][0] = 0
    # This DP start from [0, 0].

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            insertion = D[i - 1][j]
            deletion = D[i][j - 1]
            match = D[i - 1][j - 1] + 1
            mismatch = D[i - 1][j - 1]
            if s1[i - 1] == s2[j - 1]:
                D[i][j] = max(max(insertion, deletion), match)
            else:
                D[i][j] = max(max(insertion, deletion), mismatch)

    return D[m][n]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
