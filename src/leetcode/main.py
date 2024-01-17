from src.leetcode.top_150.word_search import WordSearch


def run():
    result = WordSearch().findWords(
        [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
        ["oath", "pea", "eat", "rain"])

    print(result)


if __name__ == "__main__":
    run()
