from typing import List, Optional

class TreeNode:
    def __init__(self, value: int):
        self.val = value
        self.left = None
        self.right = None
class Solution:
    def getPreOrder(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def helper(current):
            if current is None:
                return

            output.append(current.val)
            helper(current.left)
            helper(current.right)

        helper(root)
        return output



if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)


    solution = Solution()
    preorder_output = solution.getPreOrder(root)

    print("Preorder Traversal Output:", preorder_output)