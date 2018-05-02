def subarray_sum(nums, k):
    cum_sum = 0
    for i, x in enumerate(nums):
        cum_sum += x
        nums[i] = cum_sum

    sum_dict = {0: 1}
    num_subarrays = 0

    for s in nums:
        if s - k in sum_dict:
            num_subarrays += sum_dict[s - k]

        if s not in sum_dict:
            sum_dict[s] = 1
        else:
            sum_dict[s] += 1

    return num_subarrays


print subarray_sum([1,1,1], 2)
