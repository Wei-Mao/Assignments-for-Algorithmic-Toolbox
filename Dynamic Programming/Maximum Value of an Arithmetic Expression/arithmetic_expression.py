# python3
def arithmetic(a, b, ops):
    if ops == '+':
        return a + b

    if ops == '-':
        return a - b

    if ops == '*':
        return a * b


def min_and_max(dataset, i, j, m, M):
    min_val = float('inf')
    max_val = float('-inf')
    for k in range(i, j):
        a = arithmetic(M[i][k], M[k+1][j], dataset[2*k+1])
        b = arithmetic(M[i][k], m[k+1][j], dataset[2*k+1])
        c = arithmetic(m[i][k], M[k+1][j], dataset[2*k+1])
        d = arithmetic(m[i][k], m[k+1][j], dataset[2*k+1])
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val

def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29
    n = len(dataset) // 2 + 1
    m = [[0 for _ in range(n)] for _ in range(n)]
    M = [[0 for _ in range(n)] for _ in range(n)]
    # print(len(dataset))
    for i in range(n):
        # print(i)
        m[i][i] = int(dataset[2*i])
        M[i][i] = int(dataset[2*i])

    # diff = j - i, j > i
    # j =  i + diff < n
    # 0<= i < n - diff
    for diff in range(1, n):
        for i in range(0, n - diff):
            j = i + diff
            m[i][j], M[i][j] = min_and_max(dataset, i, j, m, M)
    print(M)
    return M[0][n-1]


if __name__ == "__main__":
    # print(find_maximum_value(input()))
    ins = "1+2"
    print(find_maximum_value(ins))
