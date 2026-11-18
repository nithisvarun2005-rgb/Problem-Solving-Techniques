class Node:
    def __init__(self, hub_code):
        self.hub_code = hub_code
        self.left = None
        self.right = None


class HubBST:
    def __init__(self):
        self.root = None

    def insert(self, hub_code):
        if self.root is None:
            self.root = Node(hub_code)
        else:
            self._insert(self.root, hub_code)

    def _insert(self, current, hub_code):
        if hub_code < current.hub_code:
            if current.left is None:
                current.left = Node(hub_code)
            else:
                self._insert(current.left, hub_code)
        else:
            if current.right is None:
                current.right = Node(hub_code)
            else:
                self._insert(current.right, hub_code)

    def search(self, hub_code):
        current = self.root

        while current:
            if current.hub_code == hub_code:
                return True
            elif hub_code < current.hub_code:
                current = current.left
            else:
                current = current.right

        return False

    def height(self, node):
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)


# Create BST
bst = HubBST()

hub_codes = ["H50", "H30", "H70", "H20",
             "H40", "H60", "H80"]

for code in hub_codes:
    bst.insert(code)

print("HUB MANAGEMENT SYSTEM")

print("\nHub Codes Inserted:")
print(hub_codes)

print("\nSearch H40:", bst.search("H40"))
print("Search H90:", bst.search("H90"))

print("\nHeight of BST:", bst.height(bst.root))



sorted_bst = HubBST()

sorted_codes = ["H20", "H30", "H40", "H50",
                "H60", "H70", "H80"]

for code in sorted_codes:
    sorted_bst.insert(code)

print("\nHeight with Sorted Input:",
      sorted_bst.height(sorted_bst.root))

