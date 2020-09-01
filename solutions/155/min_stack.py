class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.minVal = float("inf")


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s.append(x)
        if x < self.minVal:
            self.minVal = x

    def updateMin(self):
        tmpStack = []
        newMin = float("inf")
        while len(self.s) > 0:
            item = self.s.pop()
            tmpStack.append(item)
            if item < newMin:
                newMin = item
        while len(tmpStack) > 0:
            self.s.append(tmpStack.pop())
        self.minVal = newMin

    def pop(self):
        """
        :rtype: None
        """
        item = self.s.pop()
        if item == self.minVal:
            self.updateMin()
        return item


    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minVal




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()