def merge_sort(ls):
    if len(ls) <= 1:
        return ls

    mid = int((len(ls) + 1) / 2)
    a = ls[:mid]
    b = ls[mid:]
    return merge(a, b)


def merge(a, b):
    a = merge_sort(a)
    b = merge_sort(b)

    merged = []
    ai = bi = 0
    while ai < len(a) and bi < len(b):
        if a[ai] < b[bi]:
            merged.append(a[ai])
            ai += 1
        else:
            merged.append(b[bi])
            bi += 1

    for i in range(ai, len(a)):
        merged.append(a[i])
    for i in range(bi, len(b)):
        merged.append(b[i])

    return merged


a = [3, 8, 6, 5, 7, 9, 1, 2, 4]
a_sorted = merge_sort(a)
print(a_sorted)
assert a_sorted == sorted(a)
print("Done")
