class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)        # O(1) lookup instead of O(n) list search
        result = []
        current = []

        def backtrack(start):
            if start == len(s):                         # used the whole string -> record
                result.append(" ".join(current))
                return

            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if sub not in word_set:                 # not a valid word -> skip this cut
                    continue

                current.append(sub)                     # choose
                backtrack(end)                          # explore
                current.pop()                           # un-choose

        backtrack(0)
        return result