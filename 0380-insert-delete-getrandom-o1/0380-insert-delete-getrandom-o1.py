class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.mp = {}

    def insert(self, val: int) -> bool:
        if val not in self.mp:
            self.mp[val] = len(self.mp)
            self.nums.append(val)
            return True
        return False


    def remove(self, val: int) -> bool:
        if val in self.mp:
            idx, last_val = self.mp[val], self.nums[-1]
            self.nums[idx] = last_val
            self.mp[last_val] = idx
            del self.mp[val]
            self.nums.pop()
            return True
            
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()