class Stack:
    def __init__(self):
        self.list = []
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
    def push(self, value):
        self.list.append(value)
        return "The Element has been successfully inserted"
    def pop(self):
        if self.isEmpty():
            return "There is not any Element in the Stack"
        else:
            return self.list.pop()
    # Peek
    def peek(self):
        if self.isEmpty():
            return "Ther is no element in the stack"
        else:
            return self.list[len(self.list)-1]
    # delete
    def delete(self):
        self.list = None

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
# customStack.pop()
print(customStack.peek())
print(customStack.delete())
