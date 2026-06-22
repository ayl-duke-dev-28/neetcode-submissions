class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()                              # equal values must be adjacent for the skip to work
        result = []
        current = []

        def backtrack(start):
            result.append(current[:])            # every node is a subset -> record on entry (copy!)

            for i in range(start, len(nums)):
                # skip a duplicate value at THIS level (but allow the first occurrence)
                if i > start and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])          # choose
                backtrack(i + 1)                 # explore (i+1: each element used at most once)
                current.pop()                    # un-choose

        backtrack(0)
        return result