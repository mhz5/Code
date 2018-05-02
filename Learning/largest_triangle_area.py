class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_area = 0

        num_points = len(points)
        for i in range(num_points):
            for j in range(i + 1, num_points):
                for k in range(j + 1, num_points):
                    area = self.triangle_area(points[i], points[j], points[k])
                    max_area = max(max_area, area)
        return max_area


    def triangle_area(self, p1, p2, p3):
        return abs(p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0] - (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1])) / 2.0