class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        combos = []

        for i in range(len(nums) - 2):
            lb = i + 1
            rb = len(nums) - 1
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while lb < rb:
                sum = nums[lb] + nums[rb] + nums[i]
                if sum == 0:
                    combos.append([nums[lb], nums[rb], nums[i]])
                    lb += 1
                    rb -=1
                    while lb < rb and nums[lb] == nums[lb - 1]:
                        lb += 1
                    while lb < rb and nums[rb] == nums[rb + 1]:
                        rb -= 1
                elif sum < 0:
                    lb += 1
                else:
                    rb -= 1
        return combos