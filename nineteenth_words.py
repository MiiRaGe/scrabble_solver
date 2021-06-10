import copy
from collections import defaultdict

from generate_dict import ALL_WORDS
from utils import points, is_word_possible, INITIAL_COUNT, VALUES, END_LETTER_OF_2_POINTS_DUO

letters = {
    '*': 1,
    'a': 7,
    'b': 1,
    'c': 1,
    'd': 0,
    'e': 5,
    'f': 2,
    'g': 0,
    'h': 1,
    'i': 2,
    'j': 0,
    'k': 0,
    'l': 3,
    'm': 0,
    'n': 4,
    'o': 6,
    'p': 2,
    'q': 0,
    'r': 4,
    's': 2,
    't': 2,
    'u': 1,
    'v': 1,
    'w': 1,
    'x': 0,
    'y': 1,
    'z': 0,
}

multiplier = [1, 1, 1]
nineteenth_words = [x for x in ALL_WORDS[3] if points(x, multiplier) == 6 if VALUES[x[1]] == 1]
nineteenth_words = [x for x in nineteenth_words if is_word_possible(x, letters, {})]

all_fours = {x[0:3] for x in ALL_WORDS[4] if x[3] in {'c', 'p', 'b'}}
nineteenth_words = [x for x in nineteenth_words if x in all_fours]
nineteenth_words = [x for x in nineteenth_words if x[1] in END_LETTER_OF_2_POINTS_DUO]


if __name__ == '__main__':
    print(len(nineteenth_words))
    print(nineteenth_words)