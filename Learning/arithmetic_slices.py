def arithmetic_slices(a):
    num_slices = 0
    cur_diff = None
    cur_count = 0
    for i in range(1, len(a)):
        diff = a[i] - a[i - 1]

        if diff == cur_diff:
            cur_count += 1
        else:
            cur_diff = diff
            if cur_count > 0:
                num_slices += choose_two(cur_count + 1)
                cur_count = 0

    if cur_count > 0:
        num_slices += choose_two(cur_count + 1)

    return num_slices


def choose_two(n):
    return n * (n - 1) / 2




t1 = arithmetic_slices([1,2,3,4,5,10,15,20])
print
print 'Tests'
print t1