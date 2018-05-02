class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        self_div_nums = []
        for x in range(left, right + 1):
            if Solution.is_self_dividing(x):
                self_div_nums.append(x)
        return self_div_nums

    @staticmethod
    def is_self_dividing(x):
        val = x
        while val > 0:
            digit = val % 10
            if digit == 0 or x % digit != 0:
                return False
            val /= 10

        return True


