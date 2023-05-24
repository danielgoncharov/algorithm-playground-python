from src.leetcode.top_150.merge_sorted_array import MergeSortedArray


def run():
    result = [1, 2, 3, 0, 0, 0]
    MergeSortedArray().merge(result, 3, [2, 5, 6], 3)
    print(result)


if __name__ == "__main__":
    run()
