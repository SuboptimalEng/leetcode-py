class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sol = {}
        tmp = []
        result = []
        self.combinationSumHelper(candidates, target, tmp, sol)
        for key in sol.keys():
            result.append([key])
        return result

    def combinationSumHelper(self, candidates, target, tmp, sol):
        if target < 0:
            return

        if target == 0:
            sol[','.join(map(str, sorted(tmp)))] = 1
            return

        for num in candidates:
            tmp.append(num)
            target -= num
            self.combinationSumHelper(candidates, target, tmp, sol)
            target += num
            tmp.pop()

