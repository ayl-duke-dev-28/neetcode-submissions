class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:                        # edge case: empty input -> no combinations
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        result = []
        current = []

        def backtrack(index):
            if index == len(digits):          # used every digit -> complete combination
                result.append("".join(current))
                return

            letters = phone[digits[index]]    # the letters this digit maps to
            for letter in letters:             # try each one
                current.append(letter)        # choose
                backtrack(index + 1)          # explore
                current.pop()                  # un-choose

        backtrack(0)
        return result