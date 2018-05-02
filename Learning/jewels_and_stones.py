class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        num_jewels = 0
        for c in S:
            if c in J:
                num_jewels += 1

        return num_jewels

