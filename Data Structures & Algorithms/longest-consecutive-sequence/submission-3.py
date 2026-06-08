class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max = 0
        counter = 1
        checker = sorted(set(nums))

        if len(checker) == 0:
            return 0

        if len(checker) == 1:
            return 1

        for i in range(len(checker)):
            if i+1 >= len(checker):
                break
            if checker[i]+1 == checker[i+1]:
                counter += 1
            else:
                counter = 1
            if counter > max:
                max = counter
        
        return max