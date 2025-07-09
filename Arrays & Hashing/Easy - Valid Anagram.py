# Valid Anagram

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

# Constraints:
# s and t consist of lowercase English letters.

########################################################################################################################################333

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Sorting O(nlogn+mlogm)
        # if len(s) != len(t):
        #     return False

        # return sorted(s) == sorted(t)

        # Hash Map O(n+m)
        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        return count_s == count_t

sol = Solution()
s = 'racecar'
t = 'carrace'

print(sol.isAnagram(s,t))
