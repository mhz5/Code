# def three_sum(nums, target):
#     nums.sort()
#     solutions = []
#     dfs(nums, target, 0, [], solutions)
#     return solutions
#
#
# def dfs(nums, target, idx, subset, solutions):
#     if len(subset) == 3:
#         if sum(subset) == target:
#             solutions.append(subset)
#         return
#     for i in range(idx, len(nums)):
#         dfs(nums, target, i + 1, subset + [nums[i]], solutions)

# def three_sum(nums):
#     nums.sort()
#     d = {}
#     for i, x in enumerate(nums):
#         if x in d:
#             d[x].add(i)
#         else:
#             d[x] = {i}
#
#     triplets = set()
#     for i, x in enumerate(nums):
#         for j in range(i + 1, len(nums)):
#             y = nums[j]
#             z = -(x + y)
#             if z in d and len(d[z] - {i, j}) > 0:
#                 triplets.add(tuple(sorted([x, y, z])))
#
#     return [list(t) for t in triplets]

def three_sum(nums, target):
    nums.sort()
    triplets = []
    prev_num = None

    for i in range(len(nums)):
        if nums[i] == prev_num:
            continue
        prev_num = nums[i]
        j = i + 1
        k = len(nums) - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s <= target:
                if s == target:
                    triplets.append([nums[i], nums[j], nums[k]])
                cur_num = nums[j]
                while j < k and nums[j] == cur_num:
                    j += 1
            else:
                cur_num = nums[k]
                while j < k and nums[k] == cur_num:
                    k -= 1

    return triplets

nums = [-1, 0, 1, 2, -1, -4]
print three_sum(nums, 0)



