import random


class ChapterClass:

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.current_translate = ''

    def random_word(self):
        word = random.choice(list(self.dictionary.items()))
        return word
