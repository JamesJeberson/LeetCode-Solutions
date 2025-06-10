# Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]

# Example 3:
# Input: strs = [""]
# Output: [[""]]

# Constraints:
# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

################################################################################################################333333

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Sorting and Hash Map
        # O(n * k log k)
        # n = number of strings
        # k = maximum length of a string in strs 

        # output = []
        # hash_map = {}

        # for i, s in enumerate(strs):
            
        #     if str(''.join(sorted(s))) in hash_map:
        #         hash_map[str(''.join(sorted(s)))].append(i)
        #     else:
        #         hash_map[str(''.join(sorted(s)))] = [i]

        # for key in hash_map:
        #     anagram = []
        #     for i in hash_map[key]:
        #         anagram.append(strs[i])
        #     output.append(anagram)

        # return output

        #-------------------------------------------------------------

        # Similar to above using collections.defaultdict()

        # anagrams = defaultdict(list)
        # for s in strs:
        #     sorted_s = ''.join(sorted(s))
        #     anagrams[sorted_s].append(s) 

        # return list(anagrams.values())

        #-------------------------------------------------------------

sol = Solution()
strs = ["act","pots","tops","cat","stop","hat"]
print(sol.groupAnagrams(strs))
