from typing import Optional

from src.leetcode.linkedlists.list_node import ListNode


class OddEvenLinkedList:

    def oddEvenList(
            self,
            head: Optional[ListNode]
    ) -> Optional[ListNode]:
        odd = None
        even = None
        next_node = head
        index = 1
        first_event = None
        while next_node is not None:
            next_node_temp = next_node.next
            if index % 2 == 1:
                odd = self.assign_node(odd,next_node)
            else:
                if even is None and first_event is None:
                    first_event = self.assign_node(first_event,next_node)
                    even = first_event
                else:
                    even = self.assign_node(even,next_node)

            index = index + 1
            next_node = next_node_temp

        if odd is not None:
            odd.next = first_event
        return head

    @staticmethod
    def assign_node(node, next_node):
        if node is None:
            node = next_node
            node.next = None
        else:
            node.next = next_node
            next_node.next = None
        return next_node

