from typing import List, Optional

class TreeNode:
    def __init__(self, value: int):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def removeSpecifiedNodes(self, root: Optional[TreeNode], toRemove: List[int]) -> List[TreeNode]:
        resultTrees = []  # List to store roots of resulting trees
        toRemoveSet = set(toRemove)  # Convert to set for faster lookup

        def helper(node, isEligibleRoot):
            if not node:
                return None
            
            nodeRemoved = node.val in toRemoveSet
            # If the node is a valid root and not removed, add it to the result
            if isEligibleRoot and not nodeRemoved:
                print(f"Adding node {node.val} as a new root")
                resultTrees.append(node)

            # Process the left and right children
            node.left = helper(node.left, nodeRemoved)
            node.right = helper(node.right, nodeRemoved)

            # If the node is removed, return None
            if nodeRemoved:
                print(f"Removing node {node.val}")
                return None
            
            # Return the current node if it's not removed
            return node

        # Start the recursion
        helper(root, True)
        return resultTrees

# Helper function to display the tree as a list (level-order)
def treeToList(root: Optional[TreeNode]) -> List[Optional[int]]:
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

# Test Example
if __name__ == "__main__":
    # Construct the tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    toRemove = [3, 5]

    solution = Solution()
    print("Original Tree:", treeToList(root))
    resultForest = solution.removeSpecifiedNodes(root, toRemove)

    # Get and print the roots of the resulting forest
    forestRoots = [tree.val for tree in resultForest]
    print("Roots of Resulting Forest:", forestRoots)

    # Print the resulting forest as lists
    # print("Resulting Forest:")
    # for tree in resultForest:
    #     print(treeToList(tree))
