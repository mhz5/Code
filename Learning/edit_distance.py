def edit_distance(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    arr = [[0] * (l2 + 1) for _ in range(l1 + 1)]

    for i in range(l1 + 1):
        arr[i][0] = i
    for i in range(l2 + 1):
        arr[0][i] = i

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                arr[i][j] = arr[i - 1][j - 1]
            else:
                arr[i][j] = min(arr[i][j - 1], arr[i - 1][j], arr[i - 1][j - 1]) + 1
    return arr[l1][l2]


print edit_distance("horse", "ros")