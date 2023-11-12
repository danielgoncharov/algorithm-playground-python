# https://leetcode.com/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=top-interview-150

class Trie:

    def __init__(self):
        self.entry_nodes = dict()

    def insert(self, word: str) -> None:
        if len(word) == 0: return None

        node = self.entry_nodes[word[0]]
        if node is None:
            node = Node(word[0])
            self.entry_nodes[word[0]] = node

        node.insert(word[1: len(word)])

    def search(self, word: str) -> bool:

    def startsWith(self, prefix: str) -> bool:


class Node:

    def __init__(self, character):
        self.nodes = dict()
        self.character = character

    def insert(self, word) -> None:
        if len(word) == 0: return None

        node = self.nodes[word[0]]
        if node is None:
            node = Node(word[0])
            self.nodes[word[0]] = node

        node.insert(word[1:len(word)])
