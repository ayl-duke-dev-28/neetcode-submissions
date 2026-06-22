class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        current = []

        def is_palindrome(sub):
            return sub == sub[::-1]         # reverse and compare

        def backtrack(start):
            if start == len(s):             # partitioned the whole string -> record
                result.append(current[:])
                return

            for end in range(start + 1, len(s) + 1):   # try every possible next cut
                sub = s[start:end]                       # the next candidate substring
                if not is_palindrome(sub):               # not a palindrome -> skip this cut
                    continue

                current.append(sub)         # CHOOSE: take this palindrome substring
                backtrack(end)              # EXPLORE: partition the rest from `end`
                current.pop()              # UN-CHOOSE: remove it, try next cut

        backtrack(0)
        return result