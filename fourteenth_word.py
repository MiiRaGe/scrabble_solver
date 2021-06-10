import copy
from collections import defaultdict

from generate_dict import ALL_WORDS
from utils import points, is_word_possible, INITIAL_COUNT, VALUES


def get_fourteenth_words(letters):
    multiplier = [1, 1, 1, 1]
    fourteenth_words = [x for x in ALL_WORDS[4] if points(x, multiplier, 2) == 18]
    fourteenth_words = [x for x in fourteenth_words if is_word_possible(x, letters)]
    fourteenth_words = [x for x in fourteenth_words if VALUES[x[0]] <= 2 and VALUES[x[1]] == 1]

    return fourteenth_words


if __name__ == '__main__':
    pass