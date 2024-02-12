from src.leetcode.leetcode_75.number_of_provinces import NumberOfProvinces
from src.leetcode.top_150.word_break import WordBreak


def run():
    result = NumberOfProvinces().findCircleNum(
        [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    )

    print(result)


if __name__ == "__main__":
    run()
