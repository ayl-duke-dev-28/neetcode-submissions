class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb = 0
        rb = len(nums) - 1

        while lb <= rb:
            mid = (lb + rb) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lb = mid + 1
            else:
                rb = mid - 1

        return -1