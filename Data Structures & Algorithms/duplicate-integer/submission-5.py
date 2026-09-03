class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) ==0:
            return False

        hmap ={}

        for i in nums:
            if i in hmap:
                hmap[i]+= 1
            else:
                hmap[i]= 1
        if max(hmap.values()) > 1:
            return True
        else:
            return False

      
                
    

        