# Time Complexity : O(n) where n = len(s)
# Space Complexity : O(1) auxiliary (since we store at most 128 ASCII‐to‐ASCII mappings)
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : No issues

class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        
        n = len(s)

        if n != len(t):
            return False
        
        sMap = {}
        tMap = {}

        for i in range(n):
            c1 = s[i]
            c2 = t[i]

            # if we've already mapped c1, it must match c2
            if c1 in sMap and sMap[c1] != c2:
                return False
            
            # if we've already mapped c2, it must match c1
            if c2 in tMap and tMap[c2] != c1:
                return False
            
            # establish the mapping both ways
            sMap[c1] = c2
            tMap[c2] = c1

        return True



if __name__ == "__main__":

    sol = Solution()
    # Example 1
    print(sol.isIsomorphic("egg", "add"))    # True

    # Example 2
    print(sol.isIsomorphic("foo", "bar"))    # False

    # Example 3
    print(sol.isIsomorphic("paper", "title"))# True

    # Additional tests
    print(sol.isIsomorphic("", ""))          # True
    print(sol.isIsomorphic("a", "a"))        # True
    print(sol.isIsomorphic("ab", "aa"))      # False