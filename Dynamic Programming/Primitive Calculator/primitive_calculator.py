# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    min_num_ops = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        min_num_ops[i] = min_num_ops[i - 1] + 1
        if i % 2 == 0:
            val = min_num_ops[i // 2] + 1
            if val < min_num_ops[i]:
                min_num_ops[i] = val

        if i % 3 == 0:
            val = min_num_ops[i//3] + 1
            if val < min_num_ops[i]:
                min_num_ops[i] = val

    # construct the sols
    inter_res = [n]
    i = n
    while i > 1:
        if min_num_ops[i] == min_num_ops[i - 1] + 1:
            inter_res.append(i-1)
            i -= 1
        elif i % 2 == 0 and min_num_ops[i] == \
            min_num_ops[i // 2] + 1:
            inter_res.append(i//2)
            i = i // 2
        elif i % 3 == 0 and min_num_ops[i] == \
            min_num_ops[i // 3] + 1:
            inter_res.append(i//3)
            i = i // 3

    return inter_res[::-1]

if __name__ == '__main__':
    # input_n = int(input())
    input_n = 96234
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
