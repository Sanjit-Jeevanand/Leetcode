class RecentCounter:

    def __init__(self):
        self.dq = deque()

    def ping(self, t: int) -> int:
        while self.dq and t - 3000 > self.dq[0]:
            self.dq.popleft()
        self.dq.append(t)
        return len(self.dq)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# Queue Pattern