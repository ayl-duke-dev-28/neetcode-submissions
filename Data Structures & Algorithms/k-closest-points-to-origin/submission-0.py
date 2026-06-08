class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for x, y in points:
            dist.append(((x ** 2) + (y ** 2), x, y))
        
        heapq.heapify(dist)

        result = []

        for i in range(k):
            d, x, y = heapq.heappop(dist)
            result.append([x, y])
        
        return result