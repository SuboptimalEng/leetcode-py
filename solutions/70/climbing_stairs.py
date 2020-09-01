class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 0):
            return 0
        if (n == 1):
            return 1
        if (n == 2):
            return 2

        d = {1: 1, 2: 2}

        for i in range(3, n):
            curr = d[i-1] + d[i-2]
            d[i] = curr

        return d[n-1] + d[n-2]


