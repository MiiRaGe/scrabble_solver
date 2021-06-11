import copy
from collections import defaultdict

from utils import points, is_word_possible, VALUES


def get_twentieth_words_by_first(letters, words):
    multiplier = [1, 1, 1, 1, 1]
    twentieth_words = [x for x in words[5] if points(x, multiplier, 3) == 48]
    twentieth_words = [x for x in twentieth_words if is_word_possible(x, letters, {x[0]: 1})]
    twentieth_words_by_first = defaultdict(list)
    for x in twentieth_words:
        twentieth_words_by_first[x[0]].append(x)
    return twentieth_words_by_first


def get_twentieth_words_by_first_2(letters, words, last_letters):
    multiplier = [2, 1, 1, 1, 1]
    twentieth_words = [x for x in words[5] if points(x, multiplier, 3) + 6 + VALUES[x[0]] * 2 == 48]
    twentieth_words = [x for x in twentieth_words if is_word_possible(x, letters, {})]
    twentieth_words = [x for x in twentieth_words if x[0] in last_letters]
    twentieth_words_by_first = defaultdict(list)
    for x in twentieth_words:
        twentieth_words_by_first[x[0]].append(x)
    return twentieth_words_by_first
