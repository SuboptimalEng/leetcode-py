class Solution(object):
  def longestCommonPrefix(self, strs):
    if len(strs) == 0:
      return ""
    first_str = strs[0]
    for s in strs:
      print(s)
      while s.find(first_str) != 0:
        print(first_str)
        first_str = first_str[:-1]
      print(first_str)
      print('')
    return first_str

print('')
s = Solution()
strs = ["flower","flow","flight"]
print('answer: ' + s.longestCommonPrefix(strs))
print('')