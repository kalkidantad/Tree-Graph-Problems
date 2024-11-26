from typing import Optional

class TreeNode:
    def __init__(self, value: int):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [None]  # Store the previous node's value during traversal

        def inorder(node: Optional[TreeNode]) -> bool:
            if not node:
                return True  # Base case: Empty nodes are valid

            # Step 1: Check the left subtree
            if not inorder(node.left):
                return False
            
            # Step 2: Validate the current node
            if prev[0] is not None and node.val <= prev[0]:
                print(f"Invalid BST: Current node {node.val} is not greater than previous node {prev[0]}")
                return False
            print(f"Visited Node: {node.val}, Previous Node: {prev[0]}")
            prev[0] = node.val  # Update previous node value
            
            # Step 3: Check the right subtree
            return inorder(node.right)
        
        # Start the inorder traversal from the root
        return inorder(root)

# Example Usage
if __name__ == "__main__":
  
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(0)
    solution = Solution()
    print("Is the tree a valid BST?", solution.isValidBST(root))  


    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print("Is the tree a valid BST?", solution.isValidBST(root))  
