class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.window = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        i = 0
        while i < len(self.window) and self.window[i] < val:
            i += 1
        self.window.insert(i, val)

        if len(self.window) > self.k:  # was `k`, needs to be `self.k`
            self.window.pop(0)

        return self.window[0]