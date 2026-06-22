class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        current = []
        used = set()                          # indices already placed in `current`

        def backtrack():
            if len(current) == len(nums):     # placed all n elements -> a full permutation
                result.append(current[:])     # record a COPY (current keeps mutating)
                return

            for i in range(len(nums)):        # consider EVERY element (no start index)
                if i in used:                 # skip ones already in this permutation
                    continue

                current.append(nums[i])       # choose nums[i]
                used.add(i)                   # mark it used
                backtrack()                   # explore the next position

                current.pop()                 # un-choose
                used.remove(i)                # un-mark it

        backtrack()
        return result