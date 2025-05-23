# Time Complexity : O(n · k) where n = len(strs), k = max length of a string
# Space Complexity : O(n · k) to store the grouped anagrams
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : No issues

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map each 26-length frequency signature
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26  # build character count for s in O(k)
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)   # use tuple(count) as a hashable key
            
        return list(res.values())

        # Naive Appriach
        # for s in strs:
        #     # sorting every element
        #     key = ''.join(sorted(s))
            
        #     placed = False
        #     # scan all existing groups for a matching key
        #     for i, rep in enumerate(reps):
        #         if rep == key:
        #             groups[i].append(s)
        #             placed = True
        #             break
            
        #     # if no group found, make a new one
        #     if not placed:
        #         reps.append(key)
        #         groups.append([s])
        
        # return groups

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    # possible output: [["eat","tea","ate"],["tan","nat"],["bat"]]
    
    print(sol.groupAnagrams([""]))
    # [[""]]
    
    print(sol.groupAnagrams(["a"]))
    # [["a"]]

