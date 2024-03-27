from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.q = deque([])
        self.cache = {}
        self.cnt = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cnt += 1
            self.q.append((key, self.cnt))
            self.d[key] = self.cnt
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.cnt += 1
        self.q.append((key, self.cnt))
        self.d[key] = self.cnt
        self.cache[key] = value

        while self.q and len(self.cache) > self.capacity:
            poppedKey, poppedCnt = self.q.popleft()
            if self.d[poppedKey] == poppedCnt:
                del self.d[poppedKey]
                del self.cache[poppedKey]
            



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
