class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force

        # dict = {}
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Solution using hash map

        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict:
                return [dict[target-num], i]
            dict[num] = i
