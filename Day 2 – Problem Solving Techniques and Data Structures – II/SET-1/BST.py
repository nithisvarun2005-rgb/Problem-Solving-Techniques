class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert(current.right, data)

    def search(self, data):
        current = self.root

        while current:
            if current.data == data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right

        return False

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")


bst = BinarySearchTree()

categories = [
    "Electronics", "Clothing", "Books",
    "Furniture", "Mobiles", "Shoes",
    "Laptops", "Watches", "Gaming",
    "Beauty", "Sports", "Kitchen",
    "Toys", "Bags", "Groceries"
]

for category in categories:
    bst.insert(category)

print("PRODUCT CATEGORY BST")

print("\nInorder Traversal:")
bst.inorder(bst.root)

print("\n\nPreorder Traversal:")
bst.preorder(bst.root)

print("\n\nPostorder Traversal:")
bst.postorder(bst.root)

print("\n\nSearch Electronics:", bst.search("Electronics"))
print("Search Jewellery:", bst.search("Jewellery"))

