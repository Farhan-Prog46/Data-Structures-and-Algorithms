# ==========================================================
# Course Code : BTP500
# Lab         : Lab 07
# Student Name: Syed Farhan Zaheer Hussainy
# Student ID  : 154614232
# Topic       : Binary Search Tree using Linked List
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert a new node
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)

    # Search a node
    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, current, data):
        if current is None:
            return None
        if current.data == data:
            return current
        elif data < current.data:
            return self._search_recursive(current.left, data)
        else:
            return self._search_recursive(current.right, data)

    # Delete a node
    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, current, data):
        if current is None:
            return current

        if data < current.data:
            current.left = self._delete_recursive(current.left, data)
        elif data > current.data:
            current.right = self._delete_recursive(current.right, data)
        else:
            # Case 1: no child
            if current.left is None and current.right is None:
                return None

            # Case 2: one child
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # Case 3: two children
            successor = self._find_min(current.right)
            current.data = successor.data
            current.right = self._delete_recursive(current.right, successor.data)

        return current

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    # Display BST sideways
    def display(self):
        self._display_recursive(self.root, 0)

    def _display_recursive(self, node, level):
        if node is not None:
            self._display_recursive(node.right, level + 1)
            print("    " * level + str(node.data))
            self._display_recursive(node.left, level + 1)


# ==========================================================
# Main Program
# ==========================================================

# Given data
countries = [
    "Peru", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador",
    "Guyana", "Paraguay", "Argentina", "Suriname", "Uruguay", "Venezuela"
]

customers_creditLimit = [2500, 3500, 1000, 5000, 1000, 500, 200, 15000]

# Create BST1 for countries
bst1 = BST()
for country in countries:
    bst1.insert(country)

print("\n================ BST1: South American Countries ================\n")
bst1.display()

# Create BST2 for credit limits
bst2 = BST()
for credit in customers_creditLimit:
    bst2.insert(credit)

print("\n================ BST2: Customers Credit Limit ================\n")
bst2.display()

# Remove root node from BST1
if bst1.root is not None:
    root_country = bst1.root.data
    print(f"\nRemoving root node from BST1: {root_country}")
    bst1.delete(root_country)

print("\n================ BST1 After Removing Root ================\n")
bst1.display()

# Remove root node from BST2
if bst2.root is not None:
    root_credit = bst2.root.data
    print(f"\nRemoving root node from BST2: {root_credit}")
    bst2.delete(root_credit)

print("\n================ BST2 After Removing Root ================\n")
bst2.display()

# Search in BST1
print("\n================ Search Results in BST1 ================\n")
search_items_bst1 = ["Uruguay", "Paris"]

for item in search_items_bst1:
    result = bst1.search(item)
    if result:
        print(f"Node '{item}' found.")
        print(f"Node Address: {id(result)}")
        print(f"Present: Yes\n")
    else:
        print(f"Node '{item}' not found.")
        print("Node Address: None")
        print("Present: No\n")

# Search in BST2
print("\n================ Search Results in BST2 ================\n")
search_items_bst2 = [1000, 250]

for item in search_items_bst2:
    result = bst2.search(item)
    if result:
        print(f"Node '{item}' found.")
        print(f"Node Address: {id(result)}")
        print(f"Present: Yes\n")
    else:
        print(f"Node '{item}' not found.")
        print("Node Address: None")
        print("Present: No\n")