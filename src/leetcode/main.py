from src.leetcode.linkedlists.add_two_numbers import Solution
from src.leetcode.linkedlists.list_node import ListNode


def run():
    result = Solution().addTwoNumbers(
        ListNode(9, ListNode(9, ListNode(9))),
        ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    )
    print(result)


if __name__ == "__main__":
    run()
