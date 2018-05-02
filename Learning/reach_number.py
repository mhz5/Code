def reach_number(target):
    s = 0
    i = 0
    while s < target:
        i += 1
        s += i
    while (s - target) % 2 != 0:
        i += 1
        s += i

    return i

# def reach_helper(target, candidates, iteration):
#     iteration += 1
#
#     new_candidates = set()
#     for c in candidates:
#         c1 = c + iteration
#         c2 = abs(c - iteration)
#         if c1 == target or c2 == target:
#             return iteration
#         new_candidates.add(c1)
#         new_candidates.add(c2)
#
#     return reach_helper(target, new_candidates, iteration)


print(reach_number(15))

