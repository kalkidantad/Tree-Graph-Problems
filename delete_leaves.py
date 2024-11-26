

from typing import Optional

class TreeNode:
    def __init__(self, value: int):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def eliminateLeaves(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def postOrder(node):
            if not node:
                return None

            # update the pointers
            node.left = postOrder(node.left)
            node.right = postOrder(node.right)

            # to check it satisfies the trhee criterias
            if node.left is None and node.right is None and node.val == target:
                print(f"Removing leaf with value {node.val}")
                return None  # Remove this node (leaf)

            # Print the node being retained
            print(f"Retaining node with value {node.val}")
            return node  # Retain this node

        # Start post-order traversal
        return postOrder(root)

# Helper function to display the tree as a list (level-order)
def treeToList(root: Optional[TreeNode]) -> list:
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:  # Trim trailing None values
        result.pop()
    return result

if __name__ == "__main__":
    # Construct the tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)

    target = 2
    print("Original Tree:", treeToList(root))

    solution = Solution()
    newRoot = solution.eliminateLeaves(root, target)
    print("Modified Tree:", treeToList(newRoot))
