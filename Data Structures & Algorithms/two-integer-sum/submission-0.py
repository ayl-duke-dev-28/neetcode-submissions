class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_list = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    my_list.append(i)
                    my_list.append(j)
                    return my_list