class ArrayStack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return True if len(self.data) == 0 else False

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) == 0:
            raise Exception("Stack is empty")
        self.data.pop()

    def peek(self):
        if len(self.data) == 0:
            raise Exception("Stack is empty")
        return self.data[-1]

if __name__ == "__main__":
    stack = ArrayStack()

    stack.push(2)
    stack.push(0)
    stack.push(-3)
    stack.pop()
    top = stack.peek()
    print(stack.is_empty())
    print(top)