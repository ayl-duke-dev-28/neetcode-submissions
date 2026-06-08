class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = []
        b = set()
        nums.sort()

        for i in range(len(nums)):
            b.add(nums[i])
        
        a = list(b)
        counter = [0] * len(b)

        for i in range(len(counter)):
            for j in range(len(nums)):
                if nums[j] == a[i]:
                    counter[i] += 1

        top_idx = sorted(range(len(counter)), key=lambda i: counter[i], reverse=True)[:k]

        return [a[i] for i in top_idx]