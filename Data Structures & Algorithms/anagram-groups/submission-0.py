class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap_list = [None] * len(strs)
        output_list = []

        for i, word in enumerate(strs):
            hmap_list[i] = {}

            for char in word:
                if char in hmap_list[i]:
                    hmap_list[i][char] += 1
                else:
                    hmap_list[i][char] = 1
        
        visited = set()

        for k in range(len(strs)):
            if k in visited:
                continue
                
            same_hmap = [strs[k]]
            visited.add(k)
            for j in range(k+1, len(strs)):
                if j not in visited and hmap_list[k] == hmap_list[j]:
                    same_hmap.append(strs[j])
                    visited.add(j)


            output_list.append(same_hmap)

        return output_list

            




        