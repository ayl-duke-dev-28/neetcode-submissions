class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0
        result = []

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                product *= nums[i]
        
        if count > 1:
            return [0] * len(nums)

        if count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    result.append(int(product))
                else:
                    result.append(0)

        if count == 0:    
            for i in range(len(nums)):
                result.append(int(product/nums[i]))

        return result