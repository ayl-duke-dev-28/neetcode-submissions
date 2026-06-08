import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId -> [(time, tweetId), ...]
        self.following = defaultdict(set)    # userId -> {followeeId, ...}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        users = self.following[userId] | {userId}
        # heapq is a min-heap, so negate time to get most-recent first
        heap = []
        for u in users:
            for t in self.tweets[u][-10:]:
                heap.append((-t[0], t[1]))
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(min(10, len(heap)))]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)