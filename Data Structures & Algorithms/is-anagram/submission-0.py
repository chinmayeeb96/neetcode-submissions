class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        output = False
        hmap_s = {}
        hmap_t = {}

        for char in s:
            if char in hmap_s:
                hmap_s[char] +=1
            else:
                hmap_s[char] = 1
        
        for char in t:
            if char in hmap_t:
                hmap_t[char] +=1
            else:
                hmap_t[char] = 1
         
        if hmap_s == hmap_t:
            output = True
        
        return output
        