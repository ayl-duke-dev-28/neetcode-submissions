class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        result = []                              # all complete combinations we find go here
        current = []                             # the combination we're building right now (shared, mutated)

        def backtrack(start, remaining):         # start = first candidate index we're allowed to use
                                                 # remaining = how much of target is left to fill
            if remaining == 0:                   # we've hit the target exactly
                result.append(current[:])        # save a COPY of current (snapshot, not a live reference)
                return                           # this branch is done — stop and climb back up

            if remaining < 0:                    # we overshot the target
                return                           # dead branch — prune it, climb back up

            for i in range(start, len(nums)):    # try each candidate from `start` onward (never backward)
                current.append(nums[i])          # CHOOSE: add nums[i] to the current combination
                backtrack(i, remaining - nums[i])# EXPLORE: recurse, passing `i` (so nums[i] can be reused)
                current.pop()                    # UN-CHOOSE: remove nums[i] before trying the next candidate

        backtrack(0, target)                     # kick it off: may use any index, full target remaining
        return result                            # hand back every combination we collected