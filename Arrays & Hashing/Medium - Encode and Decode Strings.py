# Encode and Decode Strings
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
# Please implement encode and decode

# Example 1:
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]

# Example 2:
# Input: ["we","say",":","yes"]
# Output: ["we","say",":","yes"]

# Constraints:
# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.

################################################################################################################################

# O(n)

from typing import List
  
class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded_strs = ""
        for s in strs:
            encoded_strs += str(len(s))+ ':' + s

        return encoded_strs


    def decode(self, s: str) -> List[str]:
        
        decoded_str = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != ':':
                j += 1
            length = int(s[i:j])
            decoded_str.append(s[ j+1 : j+length+1])
            i = j + length + 1

        return decoded_str    


strs = ["neet","code","love","you"]
sol = Solution()
encoded = sol.encode(strs)
decoded = sol.decode(encoded)
print("Encoded:", encoded)
print("Decoded:", decoded)
