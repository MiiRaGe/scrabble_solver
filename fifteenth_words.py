from collections import defaultdict

from utils import points, is_word_possible


def get_fifteenth_words_by_first_last(letters, score, words):
    fifteenth_words = [x for x in words[7] if points(x, None, 2) == score and is_word_possible(x, letters)]
    fifteenth_words_by_first_last = defaultdict(list)
    for x in fifteenth_words:
        fifteenth_words_by_first_last[x[0] + x[-1]].append(x)
    return fifteenth_words_by_first_last
