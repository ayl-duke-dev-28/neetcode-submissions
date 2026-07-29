class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(
            self.robLinear(nums[:-1]),
            self.robLinear(nums[1:])
        )

    def robLinear(self, nums):
        n = len(nums)

        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, n + 1):
            dp[i] = max(
                dp[i - 1],
                dp[i - 2] + nums[i - 1]
            )

        return dp[n]