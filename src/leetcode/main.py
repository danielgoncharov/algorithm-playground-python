from src.leetcode.top_150.word_break import WordBreak
from src.leetcode.top_150.word_search import WordSearch


def run():
    result = WordBreak().wordBreak(
        "applepenapple",
        ["apple","pen"])

    print(result)


if __name__ == "__main__":
    run()
