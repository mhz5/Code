def longest(s):
    start = max_len = 0
    seen = {}

    for i, c in enumerate(s):
        if c in seen and start <= seen[c]:
            start = seen[c] + 1
        else:
            seen[c] = i
        max_len = max(max_len, i - start)

    return max_len
