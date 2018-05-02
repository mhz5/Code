from copy import copy

def four_sum(nums, target):
    nums = sorted(nums, reverse=True)
    return four_sum_helper(nums, target, [])


def four_sum_helper(nums, target, tup):
    if len(tup) == 4:
        if target == 0:
            return [tup]
        return None

    seen = set()
    quads = []
    for i in range(len(nums)):
        n = nums[i]
        if n in seen:
            continue
        seen.add(n)
        new_tup = copy(tup)
        new_tup.append(n)
        new_quads = four_sum_helper(nums[i + 1:], target - n, new_tup)
        if new_quads:
            quads.extend(new_quads)

    return quads


# t1 = four_sum([1, 0, -1, 0, -2, 2], 0)
# print(t1)
t2 = four_sum([-3,-2,-1,0,0,1,2,3], 0)
print(t2)
