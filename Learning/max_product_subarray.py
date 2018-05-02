def max_product(nums):
    max_prod = big = small = nums[0]

    for n in nums[1:]:
        big, small = max(n, n * big, n * small), min(n, n * big, n * small)
        max_prod = max(max_prod, big)

    return max_prod
