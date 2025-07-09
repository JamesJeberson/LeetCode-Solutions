# Products of Array Except Self
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in O(n) time without using the division operation?

# Example 1:
# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]

# Example 2:
# Input: nums = [-1,0,1,2,3]
# Output: [0,-6,0,0,0]

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Brute Force - O(n^2)
        
        # n = len(nums)
        # result = [0]*n

        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if j == i:
        #             continue
        #         prod *= nums[j]

        #     result[i] = prod

        # return result

        ########################################################

        # Division - O(n)

        # prod = 1
        # zero_count = 0

        # for num in nums:
        #     if num:
        #         prod *= nums
        #     else:
        #         zero_count += 1

        # if zero_count > 1:
        #     return [0]*len(nums)

        # result = [0]*len(nums)

        # for i, num in enumerate(nums):
        #     if zero_count:
        #         result[i] = 0 if num else prod
        #     else:
        #         result[i] = prod // num

        # return result
            
        
        ########################################################
        
        # Prefix and Suffix - O(n)
        
        n = len(nums)
        result = [0]*n
        prefix = [0]*n
        suffix = [0]*n

        prefix[0] = suffix[-1] = 1

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result

        ########################################################

        

nums = [1,2,4,6]
sol = Solution()
print(sol.productExceptSelf(nums))
