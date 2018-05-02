def two_sum(nums, target):
    num_dict = {}

    for i, x in enumerate(nums):
        num_dict[x] = i

    for i, x in enumerate(nums):
        if target - x in num_dict and num_dict[target - x] != i:
            return [num_dict[target - x], i]

    return []