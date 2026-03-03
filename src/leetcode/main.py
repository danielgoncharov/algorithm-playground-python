from src.leetcode.leetcode_75.edit_distance import EditDistance


def run():
    distance = EditDistance()
    # print(distance.minDistance("horse", "ros"))
    print(distance.minDistance("intention", "execution"))


if __name__ == "__main__":
    run()
