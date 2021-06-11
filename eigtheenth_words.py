import copy
from collections import defaultdict

from utils import points, is_word_possible, VALUES


def get_eighteenth_words_by_first(letters, words):
    eighteenth_words = [x for x in words[4] if points(x, [1, 1, 1, 2], 1) == 6]
    eighteenth_words = [x for x in eighteenth_words if is_word_possible(x, letters, {x[0]: 1})]
    eighteenth_words = [x for x in eighteenth_words if VALUES[x[1]] == 1]
    eighteenth_words_by_first = defaultdict(list)
    for x in eighteenth_words:
        eighteenth_words_by_first[x[0]].append(x)
    return eighteenth_words_by_first


def get_short_eighteenth_words_by_first(letters, words):
    eighteenth_words = [x for x in words[3] if points(x, [1, 1, 1], 1) == 6]
    eighteenth_words = [x for x in eighteenth_words if is_word_possible(x, letters, {x[0]: 1})]
    eighteenth_words = [x for x in eighteenth_words if VALUES[x[1]] == 1]
    eighteenth_words_by_first = defaultdict(list)
    for x in eighteenth_words:
        eighteenth_words_by_first[x[0]].append(x)
    return eighteenth_words_by_first

