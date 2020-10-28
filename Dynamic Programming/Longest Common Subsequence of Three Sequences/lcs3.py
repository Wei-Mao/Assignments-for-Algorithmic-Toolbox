# python3
import numpy as np
def lcs3(self, s1: str, s2: str, s3: str) -> int:
    if not s1 or not s2 or not s3:
        return 0
    m, n, p = len(s1), len(s2), len(s3)
    # prepend a 0 to the each of the string.
    # Note the index difference by 1
    # D[i, j, k] corresponds to s1[0,..., i-1], s2[0,...j-1]
    # and s3[0,...,k-1]
    D = np.zeros((m + 1, n + 1, p + 1), dtype=np.int)
    D[0, :, :] = 0
    D[:, 0, :] = 0
    D[:, :, 0] = 0

    for i in range(1,  m + 1):
        for j in range(1, n + 1):
            for k in range(1, p + 1):
                insdel1 = max(D[i-1, j, k], D[i, j-1, k], D[i, j, k-1])
                insder2 = max(D[i-1, j-1, k], D[i-1, j, k-1], D[i, j-1, k-1])
                match = D[i-1, j-1, k-1] + 1
                mismatch = D[i-1, j-1, k-1]
                if s1[i-1] == s2[j-1] and s2[j-1] == s3[k-1]:
                    D[i, j, k] = max([insdel1, insder2, match])
                else:
                    D[i, j, k] = max([insdel1, insder2, mismatch])
    return D[m, n, p]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
