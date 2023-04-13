def solution(items):
    cache = [[0 for _ in range(len(items))] for _ in range(2)]

    for i in range(1, len(items)):
        for j in range(i - 1, -1, -1):
            if items[i] % items[j] == 0:
                cache[0][i] += 1

    for i in range(2, len(items)):
        for j in range(i - 1, -1, -1):
            if items[i] % items[j] == 0:
                cache[1][i] += cache[0][j]
    return sum(cache[1])
