class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lb = 0
        ub = len(numbers) - 1

        while lb < ub:
            if numbers[lb] + numbers[ub] == target:
                return [lb + 1, ub + 1]
            elif numbers[lb] + numbers[ub] < target:
                lb += 1
            else:
                ub -= 1