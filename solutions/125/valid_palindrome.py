class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphaNumStr = ''
        for ch in s:
            if ch.isalnum():
                alphaNumStr += ch.lower()
        reversedAlphaNumStr = alphaNumStr[::-1]
        print (reversedAlphaNumStr, alphaNumStr)
        if alphaNumStr == reversedAlphaNumStr:
            return True
        return False
