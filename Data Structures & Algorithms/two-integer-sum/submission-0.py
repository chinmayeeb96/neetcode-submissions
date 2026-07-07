class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap = {}
        output = []

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hmap:
                output = [hmap[complement], i]
            else:
                hmap[nums[i]] = i
        return output
        