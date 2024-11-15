class Trie:

    def __init__(self):
        self.character = None
        self.nodes = dict()
        self.is_word = False

    def character(self, new_value):
        self.character = new_value

    def insert(self, word: str) -> None:
        if len(word) == 0: return None

        node = self.nodes.get(word[0], None)
        if node is None:
            node = Trie()
            node.character = word[0]
            self.nodes[word[0]] = node

        sufix = word[1:len(word)]
        if len(sufix) == 0:
            node.is_word = True
            return None
        else:
            node.insert(sufix)

    def search(self, word: str) -> bool:
        return self.search_with(word, True)

    def startsWith(self, prefix: str) -> bool:
        return self.search_with(prefix, False)

    def search_with(self, word: str, check_word):
        nodes = self.nodes
        word_length = len(word)
        for index in range(word_length):
            character = word[index]
            node = nodes.get(character)
            if node is None:
                return False
            else:
                nodes = node.nodes

            check_if_word = node.is_word if check_word else True

            if (
                    index == word_length - 1 and
                    node is not None and
                    check_if_word
            ):
                return True
        return False
