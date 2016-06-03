__author__ = 'felix.shaw@tgac.ac.uk - 02/06/2016'


class Featurize:

    def __init__(self):
        self.words = list()

    def get_category(self, word):

        if word in self.words:
            return self.words.index(word)
        else:
            self.words.append(word)
            return len(self.words) - 1
