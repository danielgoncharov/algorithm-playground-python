from src.leetcode.leetcode_75.online_stock_span import StockSpanner
from src.leetcode.leetcode_75.odd_even_linked_list import OddEvenLinkedList
from src.leetcode.leetcode_75.reverse_linked_list import ReverseLinkedList
from src.leetcode.linkedlists.list_node import ListNode


def run():
    stock_spanner = StockSpanner()
    print(stock_spanner.next(31))
    print(stock_spanner.next(41))
    print(stock_spanner.next(48))
    print(stock_spanner.next(59))
    print(stock_spanner.next(79))

    # OddEvenLinkedList debug for [1,2,3,4,5]
    def pylist_to_list(pylist):
        if not pylist:
            return None
        head = ListNode(pylist[0])
        current = head
        for val in pylist[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def list_to_pylist(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    oll = ReverseLinkedList()
    head = pylist_to_list([1, 2, 3, 4, 5])
    result = oll.reverseList(head)
    print('OddEvenLinkedList [1,2,3,4,5] ->', list_to_pylist(result))


if __name__ == "__main__":
    run()
