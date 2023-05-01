from src.leetcode.linkedlists.max_product_of_splitted_binary_tree import Solution
from src.leetcode.linkedlists.tree_node import TreeNode


def run():
    result = Solution().maxProduct(
        TreeNode(1,
                 TreeNode(2,
                          TreeNode(4),
                          TreeNode(5)
                          ),
                 TreeNode(3,
                          TreeNode(6)
                          )
                 )
    )
    print(result)


if __name__ == "__main__":
    run()
