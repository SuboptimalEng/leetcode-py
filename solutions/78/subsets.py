class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol = []
        self.helper(nums, sol, [], 0)
        return sol

    def helper(self, nums, sol, curr, index):
        sol.append(list(curr))
        for i in range(index, len(nums)):
            curr.append(nums[i])
            self.helper(nums, sol, curr, i + 1)
            curr.pop()
