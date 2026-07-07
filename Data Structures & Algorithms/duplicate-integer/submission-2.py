class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # if len(nums) == 0:
        #     output = False
        # else:
        #     hmap ={}

        #     for i, num in enumerate(nums):
        #         if num in hmap:
        #             hmap[num]+= 1
        #         else:
        #             hmap[num]= 1

        #     if max(hmap.values()) > 1:
        #         output = True
            
        #     else:
        #         output = False
        # return output

        hset = set()

        for num in nums:
            if num in hset:
                return True
            else:
                hset.add(num)
        return False
