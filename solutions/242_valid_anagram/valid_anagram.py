class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        h = {}
        for ch in s:
            if ch not in h:
                h[ch] = 0
            h[ch] += 1

        for ch in t:
            if ch not in h:
                h[ch] = 0
            h[ch] -= 1

        for key in h.keys():
            if h[key] != 0:
                return False

        return True

