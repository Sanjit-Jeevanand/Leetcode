class EventManager:

    def __init__(self, events: list[list[int]]):
        self.h = []
        self.map = {}
        for i in events:
            self.map[i[0]] = i[1]
            heapq.heappush(self.h, (-i[1],i[0]))
    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.map[eventId] = newPriority
        heapq.heappush(self.h, (-newPriority, eventId))
    def pollHighest(self) -> int:
        while self.h:
            p, eid = heapq.heappop(self.h)
            if eid in self.map and self.map[eid] == -p:
                del self.map[eid]
                return eid
        return -1

# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()

# Hashmap -> Lazy Deletion [If doesnt match, delete]