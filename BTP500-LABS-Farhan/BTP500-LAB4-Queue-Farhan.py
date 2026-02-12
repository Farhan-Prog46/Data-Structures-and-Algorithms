# ----------------------------------------
# Course: BTP500
# Student Name: Syed Farhan Zaheer Hussainy
# Student ID: 154714232
# Lab: 04
# ----------------------------------------


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self, size):
        self.front_node = None
        self.back_node = None
        self.size = size
        self.count = 0

    
    def enqueue(self, item):
        if self.isFull():
            print("Queue is Full! Cannot enqueue:", item)
            return

        new_node = Node(item)

        if self.isEmpty():  # first node
            self.front_node = new_node
            self.back_node = new_node
        else:
            self.back_node.next = new_node
            self.back_node = new_node

        self.count += 1
        print(f"Enqueued: {item}")


    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty! Cannot dequeue.")
            return

        removed = self.front_node.data
        self.front_node = self.front_node.next
        self.count -= 1

        
        if self.front_node is None:
            self.back_node = None

        print(f"Dequeued: {removed}")

    
    def front(self):
        if self.isEmpty():
            print("Queue is Empty! No front element.")
        else:
            print("Front element is:", self.front_node.data)

    
    def back(self):
        if self.isEmpty():
            print("Queue is Empty! No back element.")
        else:
            print("Back element is:", self.back_node.data)

    
    def isEmpty(self):
        return self.front_node is None

    
    def isFull(self):
        return self.count == self.size


# ---------------- MAIN PROGRAM (FOR SCREENSHOTS) ----------------

print("======================================")
print("Course Code: BTP500")
print("Student Name: Syed Farhan Zaheer Hussainy")
print("Student ID: 154714232")
print("Lab 04 - Queue")
print("======================================")

q = Queue(5)

print("\n--- ENQUEUE 5 FRUITS ---")
q.enqueue("Apples")
q.enqueue("Bananas")
q.enqueue("Grapes")
q.enqueue("Berries")
q.enqueue("Oranges")

print("\n--- CHECK FULL AFTER ENQUEUE ---")
print("Is Queue Full?", q.isFull())

print("\n--- FRONT POINTER DATA ---")
q.front()

print("\n--- BACK POINTER DATA ---")
q.back()

print("\n--- DEQUEUE 2 FRUITS (FIFO) ---")
q.dequeue()
q.dequeue()

print("\n--- CHECK EMPTY AFTER DEQUEUE ---")
print("Is Queue Empty?", q.isEmpty())


