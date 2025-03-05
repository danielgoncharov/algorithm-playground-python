from typing import Optional

from src.leetcode.linkedlists.list_node import ListNode


class DeleteTheMiddleNodeOfALinkedList:

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        count = self.count_nodes(head)
        if count == 1:
            return None
        elif count == 2:
            head.next = None
            return head
        else:
            node_index_to_delete = count // 2
            return self.deleteNode(head, node_index_to_delete)

    def count_nodes(self, head) -> int:
        current = head
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter

    def deleteNode(self, head, node_index_to_delete) -> Optional[ListNode]:
        left, right = None, None
        current_node = head
        for index in range(0, node_index_to_delete + 2):
            if index == node_index_to_delete + 1:
                right = current_node
            elif index == node_index_to_delete - 1:
                left = current_node
            current_node = current_node.next
        left.next = right
        return head
