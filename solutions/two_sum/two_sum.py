class Solution:
  def two_sum(self, nums, target):
    compliments = {}
    result = []
    for index, num in enumerate(nums):
      if compliments.get(num) is None:
        compliments[target-num] = index
      else:
        result = [compliments[num], index]
    return result

l = Solution()
print(l.two_sum([], 27))              # []
print(l.two_sum([5, 6], 7))           # []
print(l.two_sum([5, 6], 11))          # [0, 1]
print(l.two_sum([2, 7, 11, 15], 9))   # [0, 1]
print(l.two_sum([2, 7, 11, 15], 27))  # []

print(l.two_sum([2, 7, 11, 15], 26))  # [2, 3]
'''
Example walkthrough...
compliments = {24: 0, 19: 1, 15: 2}
compliments[15] = 2, 3
results = [2, 3]
'''
