from bisect import bisect_left
from math import ceil


class SuccessfulPairsOfSpellsAndPotions:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        return [len(potions) - bisect_left(potions, ceil(success / spell)) for spell in spells]
