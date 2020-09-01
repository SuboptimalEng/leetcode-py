class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1

        hashmap = {}
        for i in range(len(s)):
            ch = s[i]
            result = ch
            if ch in hashmap:
                hashmap[ch] = float("inf")
            else:
                hashmap[ch] = i

        for key in hashmap.keys():
            if hashmap[key] < hashmap[result]:
                result = key

        if hashmap[result] == float("inf"):
            return -1
        else:
            return hashmap[result]

