from typing import Optional

from src.leetcode.linkedlists.tree_node import TreeNode
from collections import deque


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.calculate_sums(root)
        return self.get_best_product(root)

    def get_best_product(self, root):
        max_product = 0
        total_sum = root.val
        items_deque = deque([root])
        while items_deque:
            item = items_deque.popleft()
            if item.left is not None:
                max_product = max(
                    max_product,
                    (total_sum - item.left.val) * item.left.val,
                )
                items_deque.append(item.left)
            if item.right is not None:
                max_product = max(
                    max_product,
                    (total_sum - item.right.val) * item.right.val,
                )
                items_deque.append(item.right)

        return max_product % (10 ** 9 + 7)

    def calculate_sums(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.val

        node.val = node.val + self.calculate_sums(node.left) + self.calculate_sums(node.right)
        return node.val
