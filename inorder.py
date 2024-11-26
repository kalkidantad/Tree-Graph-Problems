from typing import List, Optional

class TreeNode:
    def __init__(self, value: int):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [], []  # Initialize stack and result list
        current = root  # Start from the root node
        
        while current or stack:  # Continue while nodes to process
            # Step 1: Push all left nodes onto the stack
            while current:
                stack.append(current)
                print(f"Pushed to stack: {current.val}")
                current = current.left
            
            # Step 2: Process the node at the top of the stack
            current = stack.pop()
            print(f"Popped from stack and visiting: {current.val}")
            result.append(current.val)
            
            # Step 3: Move to the right subtree
            current = current.right
            if current:
                print(f"Moving to right subtree of: {current.val}")
        
        return result
if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.left = TreeNode(10)
    
    solution = Solution()
    print("Inorder Traversal:", solution.inorderTraversal(root))
