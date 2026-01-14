from src.leetcode.leetcode_75.online_stock_span import StockSpanner


def run():
    stock_spanner = StockSpanner()
    print(stock_spanner.next(31))
    print(stock_spanner.next(41))
    print(stock_spanner.next(48))
    print(stock_spanner.next(59))
    print(stock_spanner.next(79))


if __name__ == "__main__":
    run()
