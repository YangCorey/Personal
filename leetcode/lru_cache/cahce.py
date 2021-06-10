class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.res = {}
        

    def get(self, key: int) -> int:
        if key in self.res:
            val = self.res.pop(key)
            self.res[key] = val
        else:
            val = -1
        return val


    def put(self, key: int, value: int) -> None:
        if key in self.res:
            del self.res[key]
            self.res[key] = value
            return

        if len(self.res) < self.capacity:
            self.res[key] = value
        else:
            del self.res[next(iter(self.res))]
            self.res[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
