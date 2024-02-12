from bisect import bisect_left


class SuccessfulPairsOfSpellsAndPotions:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        return [len(potions) - bisect_left(potions, (success + spell - 1) // spell) for spell in spells]
