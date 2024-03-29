class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        from collections import deque, defaultdict
        from itertools import combinations
        self.chars = characters
        self.len = combinationLength
        
        self.res = deque()
        mp = set()
        
        def dfs(idx, length, curr):
            
            if length == self.len:
                temp = ''.join(curr)
                if temp not in self.res:
                    self.res.append(temp)
                return
            
            length += 1
            
            for j in range(idx, len(self.chars)):
                curr.append(self.chars[j])
                dfs(j+1, length, curr)
                curr.pop()
        
        for i in range( len(self.chars) - self.len + 1):
            dfs(i, 0, [])
        
        # self.res = deque([''.join(combo) for combo in combinations(self.chars, self.len)])
        
        # self.res = collections.deque(self.res)
        
        
    def next(self) -> str:
        return self.res.popleft()
        

    def hasNext(self) -> bool:
        return len(self.res) != 0


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()