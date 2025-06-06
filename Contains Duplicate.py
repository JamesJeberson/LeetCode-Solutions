# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        # Brute Force O(n^2)
        # for i in range(len(nums)):
        #     for j in range(0, len(nums)):
        #         if i != j & nums[i] == nums[j]:
        #                 return True   
        # return False

        # Hash set O(n)
        # return len(nums) != len(set(nums))

        # Hash Map O(n)
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                return True
            else:
                hash_map[nums[i]] = 0
        return False

sol = Solution()
nums = [1,2,3,1]
result = sol.hasDuplicate(nums)
print("Result:", result)
