class Node:
    "Represents a node in the Binary Search Tree"
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree implementation with insertion, deletion, and traversal"""
    
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert a value into the BST"""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Helper method to recursively insert a value"""
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        """Search for a value in the BST"""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Helper method to recursively search for a value"""
        if node is None:
            return False
        
        if value == node.data:
            return True
        elif value < node.data:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def delete(self, value):
        """Delete a value from the BST"""
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        """Helper method to recursively delete a value"""
        if node is None:
            return None
        
        if value < node.data:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.data:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with no children (leaf node)
            if node.left is None and node.right is None:
                return None
            
            # Node with one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            # Node with two children
            # Find the minimum value in the right subtree (in-order successor)
            min_larger_node = self._find_min(node.right)
            node.data = min_larger_node.data
            node.right = self._delete_recursive(node.right, min_larger_node.data)
        
        return node
    
    def _find_min(self, node):
        """Find the node with minimum value"""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inorder_traversal(self):
        """Inorder traversal (Left, Root, Right)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper method for inorder traversal"""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        """Preorder traversal (Root, Left, Right)"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """Helper method for preorder traversal"""
        if node is not None:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        """Postorder traversal (Left, Right, Root)"""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        """Helper method for postorder traversal"""
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)
    
    def height(self):
        """Calculate the height of the tree"""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        """Helper method to calculate height"""
        if node is None:
            return -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)
    
    def is_empty(self):
        """Check if the tree is empty"""
        return self.root is None
    
    def display_tree(self, node=None, level=0, prefix="Root: "):
        """Display the tree structure"""
        if node is None:
            node = self.root
        
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.data))
            if node.left is not None or node.right is not None:
                if node.left:
                    self.display_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self.display_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")


# Demo/Test Code
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    print("=== Binary Search Tree Operations ===\n")
    
    # Insert values
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65]
    print(f"Inserting values: {values}")
    for value in values:
        bst.insert(value)
    
    print("\nTree Structure:")
    bst.display_tree()
    
    print("\n--- Traversals ---")
    print(f"Inorder (sorted):   {bst.inorder_traversal()}")
    print(f"Preorder:           {bst.preorder_traversal()}")
    print(f"Postorder:          {bst.postorder_traversal()}")
    
    print(f"\nTree Height: {bst.height()}")
    
    print("\n--- Search Operations ---")
    search_values = [25, 100, 50]
    for val in search_values:
        found = bst.search(val)
        print(f"Search for {val}: {'Found' if found else 'Not Found'}")
    
    print("\n--- Delete Operations ---")
    delete_values = [10, 30, 50]
    for val in delete_values:
        print(f"\nDeleting {val}...")
        bst.delete(val)
        print(f"Inorder after deletion: {bst.inorder_traversal()}")
