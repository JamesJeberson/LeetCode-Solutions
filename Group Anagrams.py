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
