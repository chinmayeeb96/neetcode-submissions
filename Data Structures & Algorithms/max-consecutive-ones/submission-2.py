class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        max_countc = 0
        for i in range(len(nums)):
            if nums[i]== 1:
                max_countc += 1
                max_count = max(max_count, max_countc)

            else:
                max_countc = 0
        return max_count
        