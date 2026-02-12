# ----------------------------------------
# Course: BTP500
# Student Name: Syed Farhan Zaheer Hussainy
# Student ID: 154714232
# Lab: 04
# ----------------------------------------

# Stack implementation using array (list) for string data

class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    
    def push(self, item):
        if self.isFull():
            print("Stack is Full! Cannot push:", item)
        else:
            self.stack.append(item)
            print(f"Pushed: {item}")

    
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty! Cannot pop.")
        else:
            removed = self.stack.pop()
            print(f"Popped: {removed}")

    
    def top(self):
        if self.isEmpty():
            print("Stack is Empty! No top element.")
        else:
            print("Top element is:", self.stack[-1])

    
    def isEmpty(self):
        return len(self.stack) == 0


    def isFull(self):
        return len(self.stack) == self.size



# Stack implementation using Linked List for string data

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, size):
        self.top_node = None
        self.size = size
        self.count = 0

    # push() - add element
    def push(self, item):
        if self.isFull():
            print("Stack is Full! Cannot push:", item)
        else:
            new_node = Node(item)
            new_node.next = self.top_node
            self.top_node = new_node
            self.count += 1
            print(f"Pushed: {item}")

    # pop() - remove element (LIFO)
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty! Cannot pop.")
        else:
            removed = self.top_node.data
            self.top_node = self.top_node.next
            self.count -= 1
            print(f"Popped: {removed}")

    # top() - display top element
    def top(self):
        if self.isEmpty():
            print("Stack is Empty! No top element.")
        else:
            print("Top element is:", self.top_node.data)

    # isEmpty() - check if empty
    def isEmpty(self):
        return self.top_node is None

    # isFull() - check if full
    def isFull(self):
        return self.count == self.size


# ---------------- MAIN PROGRAM ----------------

print("======================================")
print("Course Code: BTP500")
print("Student Name: Syed Farhan Zaheer Hussainy")
print("Student ID: 154714232")
print("Lab 04 - Stack")
print("======================================")

s = Stack(5)

print("\n--- PUSH 5 FRUITS ---")
s.push("Apples")
s.push("Bananas")
s.push("Grapes")
s.push("Berries")
s.push("Oranges")

print("\n--- TOP AFTER PUSH ---")
s.top()

print("\n--- POP 2 FRUITS ---")
s.pop()
s.pop()

print("\n--- CHECK EMPTY ---")
print("Is Stack Empty?", s.isEmpty())

print("\n--- CHECK FULL ---")
print("Is Stack Full?", s.isFull())



