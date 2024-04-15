import random
import string

LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]


class Cipher:
    def __init__(self, key=None):
        self.key = ""

        if key == None:
            self.key = ''.join(random.choices(string.ascii_lowercase, k=100))
        else:
            self.key = key

    def encode(self, text):

        _ctr = 0
        key_len = len(self.key)
        if len(text) > len(self.key):
            while len(text) > len(self.key):
                if _ctr < key_len:
                    self.key += self.key[_ctr]
                    _ctr += 1
                else:
                    _ctr = 0

        new_text = ""

        for item in range(len(text)):
            new_text += LETTERS[LETTERS.index(self.key[item]) + LETTERS.index(text[item])]

        return new_text

    def decode(self, text):

        decoded = ""
        for item in range(len(text)):
            decoded += LETTERS[(LETTERS.index(self.key[item]) - LETTERS.index(text[item])) % 26]

        return decoded