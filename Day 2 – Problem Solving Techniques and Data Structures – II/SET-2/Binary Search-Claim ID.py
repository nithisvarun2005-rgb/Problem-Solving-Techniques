class Node:
    def __init__(self, claim_id):
        self.claim_id = claim_id
        self.left = None
        self.right = None


class ClaimBST:
    def __init__(self):
        self.root = None

    def insert(self, claim_id):
        if self.root is None:
            self.root = Node(claim_id)
        else:
            self._insert(self.root, claim_id)

    def _insert(self, current, claim_id):
        if claim_id < current.claim_id:
            if current.left is None:
                current.left = Node(claim_id)
            else:
                self._insert(current.left, claim_id)
        else:
            if current.right is None:
                current.right = Node(claim_id)
            else:
                self._insert(current.right, claim_id)

    def search(self, claim_id):
        current = self.root

        while current:
            if current.claim_id == claim_id:
                return True
            elif claim_id < current.claim_id:
                current = current.left
            else:
                current = current.right

        return False

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.claim_id, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.claim_id, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.claim_id, end=" ")



bst = ClaimBST()

claim_ids = [105, 102, 108, 101, 104,
             107, 110, 103, 106, 109]

for claim in claim_ids:
    bst.insert(claim)

print("CLAIM ID BST")

print("\nInorder Traversal:")
bst.inorder(bst.root)

print("\n\nPreorder Traversal:")
bst.preorder(bst.root)

print("\n\nPostorder Traversal:")
bst.postorder(bst.root)

print("\n\nSearch Claim 105:", bst.search(105))
print("Search Claim 120:", bst.search(120))

