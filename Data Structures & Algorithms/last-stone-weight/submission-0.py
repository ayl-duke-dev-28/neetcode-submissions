class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negated = []
        for s in stones:
            negated.append(-s)
        
        heapq.heapify(negated)

        while len(negated) > 1:
            y = -heapq.heappop(negated)
            x = -heapq.heappop(negated)

            if x != y:
                heapq.heappush(negated, -(y-x))
            
        if negated:
            return -negated[0]

        else:
            return 0