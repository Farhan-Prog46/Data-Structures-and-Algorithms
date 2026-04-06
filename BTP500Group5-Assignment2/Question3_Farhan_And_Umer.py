# Completed by: Syed Farhan & Muhammad Umer – Group #5
# Question 3: Library System using BST

class BookNode:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.left_child = None
        self.right_child = None


class LibraryBST:
    def __init__(self):
        self.root = None

    # Insert
    def insert(self, title, author, year):
        if self.root is None:
            self.root = BookNode(title, author, year)
            print(f"Inserted root book: {title}")
        else:
            self._insert(self.root, title, author, year)

    def _insert(self, node, title, author, year):
        if title.lower() < node.title.lower():
            if node.left_child is None:
                node.left_child = BookNode(title, author, year)
                print(f"Inserted '{title}' to LEFT of '{node.title}'")
            else:
                self._insert(node.left_child, title, author, year)

        elif title.lower() > node.title.lower():
            if node.right_child is None:
                node.right_child = BookNode(title, author, year)
                print(f"Inserted '{title}' to RIGHT of '{node.title}'")
            else:
                self._insert(node.right_child, title, author, year)

        else:
            print(f"Book '{title}' already exists in the BST")

    # Search
    def search(self, title):
        return self._search(self.root, title)

    def _search(self, node, title):
        if node is None:
            return None

        if title.lower() == node.title.lower():
            return node
        elif title.lower() < node.title.lower():
            return self._search(node.left_child, title)
        else:
            return self._search(node.right_child, title)

    # In-order Traversal
    def in_order_traversal(self, node, result=None):
        if result is None:
            result = []

        if node is not None:
            self.in_order_traversal(node.left_child, result)
            result.append((node.title, node.author, node.year))
            self.in_order_traversal(node.right_child, result)

        return result

    # Pre-order Traversal
    def pre_order_traversal(self, node, result=None):
        if result is None:
            result = []

        if node is not None:
            result.append((node.title, node.author, node.year))
            self.pre_order_traversal(node.left_child, result)
            self.pre_order_traversal(node.right_child, result)

        return result

    # Post-order Traversal
    def post_order_traversal(self, node, result=None):
        if result is None:
            result = []

        if node is not None:
            self.post_order_traversal(node.left_child, result)
            self.post_order_traversal(node.right_child, result)
            result.append((node.title, node.author, node.year))

        return result

    # Display traversal output
    def display_books(self, books, heading):
        print(f"\n{heading}")
        for title, author, year in books:
            print(f"Title: {title}, Author: {author}, Year: {year}")

    # Simple tree visualization
    def display_tree(self, node, level=0, label="Root: "):
        if node is not None:
            self.display_tree(node.right_child, level + 1, "R--- ")
            print("    " * level + label + node.title)
            self.display_tree(node.left_child, level + 1, "L--- ")


def main():
    library = LibraryBST()

    print("INSERTING BOOKS")
    library.insert("Python Basics", "John Smith", 2020)
    library.insert("Data Structures", "Alice Brown", 2019)
    library.insert("Algorithms", "Michael Lee", 2021)
    library.insert("Database Systems", "Sara Khan", 2018)
    library.insert("Operating Systems", "David Miller", 2022)

    print("\nBST STRUCTURE")
    library.display_tree(library.root)

    print("\nSEARCH RESULT")
    book = library.search("Algorithms")
    if book:
        print(f"Book Found -> Title: {book.title}, Author: {book.author}, Year: {book.year}")
    else:
        print("Book not found")

    library.display_books(
        library.in_order_traversal(library.root),
        "IN-ORDER TRAVERSAL"
    )

    library.display_books(
        library.pre_order_traversal(library.root),
        "PRE-ORDER TRAVERSAL"
    )

    library.display_books(
        library.post_order_traversal(library.root),
        "POST-ORDER TRAVERSAL"
    )


if __name__ == "__main__":
    main()