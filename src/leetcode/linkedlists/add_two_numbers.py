from typing import Optional

from src.leetcode.linkedlists.list_node import ListNode


class Solution:
    def addTwoNumbers(
            self,
            first_number: Optional[ListNode],
            second_number: Optional[ListNode]
    ) -> Optional[ListNode]:
        if first_number is None and second_number is None:
            return None
        elif first_number is None:
            return second_number
        elif second_number is None:
            return first_number

        previous_digit = None
        first_number_digit = first_number
        second_number_digit = second_number
        carry_over = 0
        answer = None
        while first_number is not None and second_number is not None:
            if first_number is None:
                current_sum = second_number.val
                second_number = second_number.next
            elif second_number is None:
                current_sum = first_number.val
                first_number = first_number.next
            else:
                current_sum = first_number_digit.val + second_number_digit.val
                first_number = first_number.next
                second_number = second_number.next

            carry_over = (current_sum + carry_over) / 10
            val = (current_sum + carry_over) % 10

            current_digit = ListNode(val)
            if previous_digit is None:
                answer = current_digit
            else:
                previous_digit.next = current_digit
            previous_digit = current_digit
        return answer
