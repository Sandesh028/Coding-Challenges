# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest
# substring
# without repeating characters.

 
class Solution:
    def lengthOfLongestSubstring(self, s):
        charMap = {}
        left = 0
        maxLen = 0
        
        for right in range(len(s)):
            if s[right] in charMap and charMap[s[right]] >= left:
                left = charMap[s[right]] + 1
            charMap[s[right]] = right
            maxLen = max(maxLen, right - left + 1)
        return maxLen
                

