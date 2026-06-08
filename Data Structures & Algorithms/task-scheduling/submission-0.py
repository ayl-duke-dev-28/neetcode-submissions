class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        heap = []
        for val in count.values():
            heap.append(-val)
        heapq.heapify(heap)

        cooldown = deque()
        time = 0

        while heap or cooldown:
            time += 1

            if cooldown and cooldown[0][1] <= time:
                val, read_at = cooldown.popleft()
                heapq.heappush(heap, val)

            if heap:
                val = heapq.heappop(heap)
                val += 1
                if val != 0:
                    cooldown.append((val, time + n + 1))
            
        return time