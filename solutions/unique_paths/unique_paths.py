class Solution(object):
  def uniquePaths(self, m, n):
    matrix = [[1 for i in range(m)] for j in range(n)]
    for i in range(1, n):
      for j in range(1, m):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    return matrix[n-1][m-1]

s = Solution()
print(s.uniquePaths(2, 3))
print(s.uniquePaths(3, 2))
print(s.uniquePaths(1, 5))