# ==========================================================
# Course Code : BTP500
# Lab         : Lab 08
# Student Name: Syed Farhan Zaheer Hussainy
# Student ID  : 154614232
# Topic       : AVL TREE
# ==========================================================


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def getHeight(self, root):
        return root.height if root else 0

    def getBalance(self, root):
        return self.getHeight(root.left) - self.getHeight(root.right) if root else 0

    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        return x

    def leftRotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def insert(self, root, key):
        if not root:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        # Rotations
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def minValueNode(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        return root

    def search(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def printTree(self, root):
        if root:
            print(f"{root.key} (Height: {root.height}, Balance: {self.getBalance(root)})")
            self.printTree(root.left)
            self.printTree(root.right)


# DATA
countries = ["Peru","Bolivia","Brazil","Chile","Colombia","Ecuador",
             "Guyana","Paraguay","Argentina","Suriname","Uruguay","Venezuela"]

credits = [2500,3500,1000,5000,1000,500,200,15000]

# RUN
avl = AVLTree()
root1 = None
root2 = None

for c in countries:
    root1 = avl.insert(root1, c)

for num in credits:
    root2 = avl.insert(root2, num)

print("\nAVL Tree (Countries):")
avl.printTree(root1)

print("\nAVL Tree (Credits):")
avl.printTree(root2)

# DELETE
root1 = avl.delete(root1, "Uruguay")
root2 = avl.delete(root2, 500)

print("\nAfter Deletion:")
avl.printTree(root1)
avl.printTree(root2)

# SEARCH
print("\nSearch Results:")

result = avl.search(root1, "Venezuela")
if result:
    print(f"Venezuela found -> {result.key} (Height: {result.height}, Balance: {avl.getBalance(result)})")
else:
    print("Venezuela not found")

result = avl.search(root1, "Uruguay")
if result:
    print(f"Uruguay found -> {result.key} (Height: {result.height}, Balance: {avl.getBalance(result)})")
else:
    print("Uruguay not found")

result = avl.search(root2, 500)
if result:
    print(f"500 found -> {result.key} (Height: {result.height}, Balance: {avl.getBalance(result)})")
else:
    print("500 not found")

result = avl.search(root2, 2500)
if result:
    print(f"2500 found -> {result.key} (Height: {result.height}, Balance: {avl.getBalance(result)})")
else:
    print("2500 not found")