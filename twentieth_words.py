import copy
from collections import defaultdict

from utils import points, is_word_possible, VALUES


def get_twentieth_words(letters, words, variant):
    twentieth_words = [x for x in words[5] if is_word_possible(x, letters, {x[0]: 1})]
    if variant['3'] == '1':
        multiplier = [2, 1, 1, 1, 1]
        twentieth_words = [x for x in twentieth_words if points(x, multiplier, 3) + 6 + VALUES[x[0]] == 48]
    else:
        multiplier = [1, 1, 1, 1, 1]
        twentieth_words = [x for x in twentieth_words if points(x, multiplier, 3) == 48]
    twentieth_words_by_first = defaultdict(list)
    for x in twentieth_words:
        twentieth_words_by_first[x[0]].append(x)
    return twentieth_words_by_first, twentieth_words

