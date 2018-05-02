def longest_substring(s1, s2):
    arr = [[0 for _ in range(len(s2) + 1)]
           for _ in range(len(s1) + 1)]

    max_len = 0
    longest_ss = ''
    for x, cx in enumerate(s1):
        for y, cy in enumerate(s2):
            if cx == cy:
                suffix_len = arr[x][y] + 1
                if suffix_len > max_len:
                    max_len = suffix_len
                    longest_ss = s1[x - suffix_len + 1:x + 1]
                arr[x + 1][y + 1] = suffix_len

    return longest_ss


a = "htnsaoeintht"
b = "aoeihtnsaoei"

assert longest_substring(a, b) == "htnsaoei"
print("Done")
