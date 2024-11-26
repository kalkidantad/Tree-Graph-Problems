from typing import List, Optional

class TreeNode:
    def __init__(self, value: int):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def consTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        rootNodeVal = preorder[0]
        rootNode = TreeNode(rootNodeVal)

        indexRootInorder = inorder.index(rootNodeVal)

        inorderLeft = inorder[:indexRootInorder]
        inorderRight = inorder[indexRootInorder + 1:]

        leftSubtreeSize = len(inorderLeft)

        preorderLeft = preorder[1:leftSubtreeSize + 1]
        preorderRight = preorder[leftSubtreeSize + 1:]

        rootNode.left = self.consTree(preorderLeft, inorderLeft)
        rootNode.right = self.consTree(preorderRight, inorderRight)

        return rootNode
    

    def treeToList(self, root: TreeNode) -> List[Optional[int]]:
        def dfs(node, index, output):
            # Extend the list to fit the current index
            if index >= len(output):
                output.extend([None] * (index - len(output) + 1))
            
            if node is not None:
                output[index] = node.val
                dfs(node.left, 2 * index + 1, output)  # Left child index
                dfs(node.right, 2 * index + 2, output)  # Right child index

        result = []
        dfs(root, 0, result)
        return result
    
if __name__ == "__main__":
    preorder = [3, 1, 4, 5, 2] 
    inorder = [4,1,5,3,2]

    solution = Solution()
    treeRoot = solution.consTree(preorder, inorder)

    treeAsList = solution.treeToList(treeRoot)
    print("Constructed Tree as List:", treeAsList)