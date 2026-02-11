from typing import Optional

from src.leetcode.linkedlists.list_node import ListNode


class ReverseLinkedList:


    def reverseList(
            self,
            head: Optional[ListNode]
    ) -> Optional[ListNode]:
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous