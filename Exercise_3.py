# Time Complexity : O(n) where n = len(s) + len(pattern)
# Space Complexity : O(n) for the char_to_word dict and used set,
#                   plus O(1) extra for parsing pointers (no full split list)
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : No issues

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        i = 0
        n = len(s)

        char_to_word = {}  # maps pattern char -> word
        used = set()       # tracks which words are already assigned

        for c in pattern:
            # if we've run out of characters before finishing pattern, fail
            if i >= n:
                return False

            # find the end of the current word
            j = i
            while j < n and s[j] != ' ':
                j += 1
            word = s[i:j]

            # empty word is invalid
            if not word:
                return False

            # check existing mapping
            if c in char_to_word:
                if char_to_word[c] != word:
                    return False
            else:
                # new mapping: but word must not already be used
                if word in used:
                    return False
                char_to_word[c] = word
                used.add(word)

            # advance i past this word and the following space (if any)
            i = j + 1

        # after consuming pattern, we must also have consumed all of s
        # i == n+1 when there was a trailing space, or i == n otherwise
        return i == n + 1 or i == n


if __name__ == "__main__":
    sol = Solution()

    print(sol.wordPattern("abba", "dog cat cat dog"))  # True
    print(sol.wordPattern("abba", "dog cat cat fish"))# False
    print(sol.wordPattern("aaaa", "dog cat cat dog")) # False
    print(sol.wordPattern("abc",  "one two"))         # False (length mismatch)
    print(sol.wordPattern("a",    ""))                # False (no word to map)

