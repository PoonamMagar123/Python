class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""

        for char in s:
            if char in 'aeiouAEIOU':
                result += char
        
        return result
