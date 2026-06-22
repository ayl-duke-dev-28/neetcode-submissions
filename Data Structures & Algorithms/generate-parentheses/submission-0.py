class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        current = []                         # build the string as a list of chars, join at the end

        def backtrack(open, close):
            if open == close == n:           # used all n pairs and balanced -> valid, record it
                result.append("".join(current))
                return

            if open < n:                     # can still open a bracket
                current.append("(")          # choose
                backtrack(open + 1, close)   # explore
                current.pop()               # un-choose

            if close < open:                 # can still close a bracket (only if something's open)
                current.append(")")          # choose
                backtrack(open, close + 1)   # explore
                current.pop()               # un-choose

        backtrack(0, 0)
        return result