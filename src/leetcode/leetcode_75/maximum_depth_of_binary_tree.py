from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaximumDepthOfBinaryTree:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.calculate_depth(root, 0)

    def calculate_depth(self, node: TreeNode, current_depth) -> int:
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1 + current_depth
        return max(
            self.calculate_depth(node.left, current_depth + 1),
            self.calculate_depth(node.right, current_depth + 1)
        )
