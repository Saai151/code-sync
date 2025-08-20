class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.count = -1
        

    def push(self, x: int) -> None:
        if self.count + 1 == self.maxSize:
            return
        self.stack.append(x)
        self.count +=1
        

    def pop(self) -> int:
        if self.count == -1:
            return -1
        value = self.stack[self.count]
        del self.stack[self.count]
        self.count -= 1
        return value

    def increment(self, k: int, val: int) -> None:
        print(self.stack)
        if k > self.count:
            for i in range(self.count + 1):
                self.stack[i] += val
        else:
            for i in range(k):
                self.stack[i] += val
        print(self.stack)
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)