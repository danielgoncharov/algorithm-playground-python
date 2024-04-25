from collections import deque


class Dota2Senate:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_queue = deque()
        dire_queue = deque()
        for index in range(len(senate)):
            character = senate[index]
            if character == 'R':
                radiant_queue.appendleft(index)
            else:
                dire_queue.appendleft(index)

        next_index = len(senate)
        while len(dire_queue) != 0 and len(radiant_queue) != 0:
            dire = dire_queue.pop()
            radiant = radiant_queue.pop()
            if dire > radiant:
                radiant_queue.appendleft(next_index)
            else:
                dire_queue.appendleft(next_index)
            next_index += 1

        if len(dire_queue) != 0:
            return "Dire"
        else:
            return "Radiant"
