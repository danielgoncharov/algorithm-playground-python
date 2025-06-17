from typing import Optional, List

from src.leetcode.linkedlists.tree_node import TreeNode
from collections import deque


class BinaryTreeRightSideVie:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result_with_index = [(root.val, 0)]
        processing_dequeue = deque([(root, 0)])
        while processing_dequeue:
            (current_node, current_level) = processing_dequeue.popleft()
            if current_node is None:
                continue
            last_element_index = len(result_with_index) - 1
            (last_value, last_level) = result_with_index[last_element_index]
            if current_level == last_level:
                result_with_index[last_element_index] = (current_node.val, current_level)
            else:
                result_with_index.append((current_node.val, current_level))
            processing_dequeue.append(
                (current_node.left, current_level + 1)
            )

            processing_dequeue.append(
                (current_node.right, current_level + 1)
            )
        return [item[0] for item in result_with_index]
