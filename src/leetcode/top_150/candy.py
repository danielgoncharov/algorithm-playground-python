from typing import List


class Candy:
    def candy(self, ratings: List[int]) -> int:
        ratings_size = len(ratings)

        left_to_right_traversal = [0] * ratings_size
        left_to_right_traversal[0] = 1
        for index in range(1, ratings_size):
            if ratings[index] > ratings[index - 1]:
                left_to_right_traversal[index] = left_to_right_traversal[index - 1] + 1
            else:
                left_to_right_traversal[index] = 1

        right_to_left_traversal = [0] * ratings_size
        right_to_left_traversal[ratings_size - 1] = 1
        for index in range(ratings_size - 2, -1, -1):
            if ratings[index] > ratings[index + 1]:
                right_to_left_traversal[index] = right_to_left_traversal[index + 1] + 1
            else:
                right_to_left_traversal[index] = 1

        result = 0
        for index in range(0, ratings_size):
            result += max(left_to_right_traversal[index], right_to_left_traversal[index])
        return result
