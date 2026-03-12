# Stack with single linked list

class Stack:
    def __init__(self, size):
        self.Stack = []
        self.size = size

    def push (self, item):
        if self.isFull(item):
            print ("stack is full", item)
        else:
            self.Stack.append(item)
            print(f"Pushed {item}")

    def pop (self):
        if self.isEmpty():
            print ("stack is empty")
        else:
            remove = self.Stack.pop()
            print(f"removed: {remove}")

    def top (self):
        if self.isEmpty():
            print ("stack is empty")
        else:
            print ("top element is : ", self.Stack[-1])

    def isFull(self):
        return len(self.Stack) == self.size
    
    def isEmpty(self):
        return len(self.Stack) == 0
    

class Node:
        def __init__(self, data, next = None):
            self.data = data
            self.next = next
        
class Stack:
        def __init__(self, size):
            self.top_node  = None
            self.size = size
            MyCount = 0

        def push(self, item):
            if self.isFull():
                print ("stack is full")
            else:
                new_node = Node(item)
                self.new_node.next = self.top_node
                self.top_node = new_node
                self.MyCount += 1
                print(f"Pushed: {item}")

        def pop (self):
            if self.isEmpty():
                print("Stack is Empty")
            else:
                remove = self.top_node.data
                self.top_node = self.top_node.next
                self.MyCount -= 1
                print (f"Removed : {remove}")

        def top (self):
            if self.isEmpty():
                print ("stack is empty")
            else:
                print("Top element is:", self.top_node.data)

        def isFull(self):
            return len(self.MyCount) == self.size
        
        def isEmpty(self):
            return len(self.top_node) is None
    