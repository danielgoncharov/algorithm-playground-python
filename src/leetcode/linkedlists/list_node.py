class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = None
        node = self
        while node is not None:
            if result is None:
                result = str(node.val)
            else:
                result += " ," + str(node.val)
            node = node.next
        return result[::-1]
