# python3


def edit_distance(first_string, second_string):
    m, n = len(first_string), len(second_string)
    D = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for j in range(n+1):
        D[0][j] = j + 1
    for i in range(m+1):
        D[i][0] = i + 1

    for i in range(1, m+1):
        for j in range(1, n+1):
            deletion = D[i -1][j] + 1
            insertion = D[i][ j- 1] + 1
            diff = 0 if first_string[i - 1] == second_string[j - 1] else 1
            match_mis = D[i - 1][j - 1] + diff
            D[i][j] = min(deletion, insertion, match_mis)

    return D[m][n] - 1




if __name__ == "__main__":
    print(edit_distance(input(), input()))
