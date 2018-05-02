# https://leetcode.com/problems/zigzag-conversion/description/

class Solution(object):
    def convert2(self, s, num_rows):
        if num_rows == 1:
            return s

        arr = ['' for _ in range(num_rows)]
        row_idx = 0
        is_reverse = False
        for _, c in enumerate(s):
            arr[row_idx] += c
            if row_idx == num_rows - 1:
                is_reverse = True
            if row_idx == 0:
                is_reverse = False

            if is_reverse:
                row_idx -= 1
            else:
                row_idx += 1

        return "".join(arr)



    def convert(self, s, num_rows):
        """
        :type s: str
        :type num_rows: int
        :rtype: str
        """
        if num_rows == 1:
            return s

        num_cols = int(len(s) / (num_rows - 1)) + 1

        arr = []
        for i in range(num_cols):
            start = (num_rows - 1) * i
            end = start + (num_rows - 1) + 1
            row = [j for j in range(start, end)]
            row[0] = -1
            if i % 2 == 1:
                row.reverse()
            arr.append(row)

        res = s[0]
        for row in range(num_rows):
            for col in range(num_cols):
                idx = arr[col][row]
                if 0 <= idx < len(s):
                    res += s[idx]

        return res


s = 'PAYPALISHIRING'
sol = Solution()
converted_s = sol.convert2(s, 3)
print(converted_s)
