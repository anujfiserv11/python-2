class WordCounter:
    def __init__(self, sentence):
        self.sentence = sentence
        self.word_count = 0
        self.shortest_word = None
        self.longest_word = None

    def count_words(self):
        words = self.sentence.split(" ")
        self.word_count = len(words)
        self.shortest_word = len(words[0])
        self.longest_word = len(words[0])
        for word in words[1:]:
            if len(word) < self.shortest_word:
                self.shortest_word = len(word)
            if len(word) > self.longest_word:
                self.longest_word = len(word)

    def get_word_count(self):
        return self.word_count

    def get_shortest_word(self):
        return self.shortest_word

    def get_longest_word(self):
        return self.longest_word
