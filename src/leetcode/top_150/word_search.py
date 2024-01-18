from dataclasses import dataclass, field
from typing import List


class WordSearch:

    def findWords(
            self,
            board: List[List[str]],
            words: List[str]
    ) -> List[str]:
        result = []
        root = self.build_trie(words)
        for row_index in range(len(board)):
            for column_index in range(len(board[0])):
                self.dfs(
                    row_index,
                    column_index,
                    board,
                    root,
                    result
                )
        return list(set(result))

    def build_trie(self, words) -> 'Trie':
        root = Trie()
        for word in words:
            current_trie = root
            for character in word:
                current_trie = current_trie.add_child(character)
            current_trie.word = word
        return root

    def dfs(
            self,
            row_index,
            column_index,
            board,
            trie,
            words
    ):
        if (
                row_index < 0 or
                row_index == len(board) or
                column_index < 0 or
                column_index == len(board[0]) or
                board[row_index][column_index] == "#" or
                not trie.has_child_with_character(board[row_index][column_index])
        ):
            return

        if trie.has_word_at(board[row_index][column_index]):
            words.append(trie.child_word(board[row_index][column_index]))

        trie = trie.child_for(board[row_index][column_index])
        buffer = board[row_index][column_index]
        board[row_index][column_index] = "#"
        self.dfs(row_index + 1, column_index, board, trie, words)
        self.dfs(row_index - 1, column_index, board, trie, words)
        self.dfs(row_index, column_index + 1, board, trie, words)
        self.dfs(row_index, column_index - 1, board, trie, words)
        board[row_index][column_index] = buffer


@dataclass
class Trie:
    children: List['Trie'] = field(default_factory=lambda: [None] * 26)
    word: str = None

    def index(self, character):
        return ord(character) - ord('a')

    def add_child(self, character):
        if self.children[self.index(character)] is None:
            self.children[self.index(character)] = Trie()
        return self.children[self.index(character)]

    def child_for(self, character):
        return self.children[self.index(character)]

    def has_child_with_character(self, character):
        return self.children[self.index(character)] is not None

    def has_word_at(self, character):
        return self.children[self.index(character)].word is not None

    def child_word(self, character):
        return self.children[self.index(character)].word
