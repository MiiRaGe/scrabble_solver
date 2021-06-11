import copy
from collections import defaultdict

from utils import points, is_word_possible


def get_seventeenth_words_by_last(letters, score, words):
    multiplier = [1, 1, 1, 1, 1]
    seventeenth_words = [x for x in words[5] if points(x, multiplier, 2) == score]
    seventeenth_words = [x for x in seventeenth_words if is_word_possible(x, letters, {x[-1]: 1})]

    seventeenth_words_by_last = defaultdict(list)
    for x in seventeenth_words:
        seventeenth_words_by_last[x[-1]].append(x)
    return seventeenth_words_by_last
