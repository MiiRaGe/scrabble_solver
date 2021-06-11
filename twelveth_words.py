import copy
from collections import defaultdict

from utils import points, is_word_possible, INITIAL_COUNT, VALUES, possible_scores, add_blanks_7, \
    START_LETTER_OF_2_POINTS_DUO


def get_twelveth_words(letters, words):
    multiplier = [1, 1, 1, 1, 1, 3, 1, 1]
    twelveth_words = [x for x in words[7] if points(x, multiplier, 2) >= 28]
    twelveth_words = [x for x in twelveth_words if x[0] in START_LETTER_OF_2_POINTS_DUO]
    twelveth_words = [x for x in twelveth_words if x[1] in START_LETTER_OF_2_POINTS_DUO]
    twelveth_words = [x for x in twelveth_words if x[2] in START_LETTER_OF_2_POINTS_DUO]
    twelveth_words = [x for x in twelveth_words if x[-1] in START_LETTER_OF_2_POINTS_DUO]
    twelveth_words = [x for x in twelveth_words if x[-2] in START_LETTER_OF_2_POINTS_DUO]
    twelveth_words, originals = add_blanks_7(twelveth_words)
    twelveth_words = [x for x in twelveth_words if points(x, multiplier, 2) >= 28]
    twelveth_words, originals_2 = add_blanks_7(twelveth_words)
    twelveth_words = [x for x in twelveth_words if points(x, multiplier, 2) == 28]
    twelveth_words = [x for x in twelveth_words if is_word_possible(x, letters)]
    twelveth_words = [x for x in twelveth_words if VALUES[x[0]] == VALUES[x[-1]] == VALUES[x[-2]] == 1]
    twelveth_words = [x for x in twelveth_words if VALUES[x[1]] <= 1 and VALUES[x[2]] in {0, 2}]
    return twelveth_words
