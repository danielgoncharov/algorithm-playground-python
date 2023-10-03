class ReverseWordsInAString:
    def reverseWords(self, sentence: str) -> str:
        words = sentence.strip().split()
        words = map(lambda word: word.strip(), words)
        words = list(words)
        words.reverse()
        return " ".join(words)
