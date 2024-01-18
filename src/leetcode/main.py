from src.leetcode.top_150.word_search import WordSearch


def run():
    result = WordSearch().findWords(
        [["a","a"]],
        ["aa"])

    print(result)


if __name__ == "__main__":
    run()
