from src.leetcode.top_150.gas_station import GasStation
from src.leetcode.top_150.trapping_rain_water import TrappingRainWater


def run():
    result = TrappingRainWater().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(result)


if __name__ == "__main__":
    run()
