class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()                            # sort so equal values sit next to each other
        result = []
        current = []

        def backtrack(start, remaining):
            if remaining == 0:                       # exact hit -> record this combination
                result.append(current[:])
                return
            if remaining < 0:                        # overshot -> prune this branch
                return

            for i in range(start, len(candidates)):
                # skip a duplicate value at THIS level (but not the first occurrence)
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current.append(candidates[i])        # choose
                backtrack(i + 1, remaining - candidates[i])  # explore; i+1 -> each element used once
                current.pop()                        # un-choose

        backtrack(0, target)
        return result