from typing import List


class FindHighestAltitude:
    def largestAltitude(self, net_gains: List[int]) -> int:
        max_altitude = 0
        current_altitude = 0
        for index in range(len(net_gains)):
            current_altitude += net_gains[index]
            max_altitude = max(max_altitude, current_altitude)
        return max_altitude
