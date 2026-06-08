from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # stores indices
        ret = []

        for r in range(len(nums)):
            # remove smaller values from the back
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)

            # remove front if it's out of this window
            if dq[0] <= r - k:
                dq.popleft()

            # start recording answers once window size is k
            if r >= k - 1:
                ret.append(nums[dq[0]])

        return ret