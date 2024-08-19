class TribonacciNumber:
    def tribonacci(self, n: int) -> int:
        cache = [0, 1, 1]
        for item in range(3, n + 1):
            n_2 = cache[item - 1]
            n_1 = cache[item - 2]
            n_0 = cache[item - 3]
            cache.append(n_0 + n_1 + n_2)
        return cache[n]
