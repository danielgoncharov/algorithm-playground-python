from src.leetcode.linkedlists.add_two_numbers import Solution
from src.leetcode.linkedlists.list_node import ListNode


def run():
    result = Solution().addTwoNumbers(
        ListNode(2, ListNode(4, ListNode(3))),
        ListNode(5, ListNode(6, ListNode(4)))
    )
    print(result)


if __name__ == "__main__":
    run()
