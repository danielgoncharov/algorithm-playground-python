class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        next_span = 1
        while len(self.stack) != 0 and self.stack[-1][0] <= price:
            (_, span_size) = self.stack.pop()
            next_span += span_size
        self.stack.append((price, next_span))
        return next_span
