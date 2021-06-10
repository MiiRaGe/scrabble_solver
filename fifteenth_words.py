import copy
from collections import defaultdict

from generate_dict import ALL_WORDS
from utils import points, is_word_possible, INITIAL_COUNT, possible_scores


def get_fifteenth_words_by_first_last(letters, score):
    fifteenth_words = [x for x in ALL_WORDS[7] if points(x, None, 2) == score and is_word_possible(x, letters)]
    fifteenth_words_by_first_last = defaultdict(list)
    for x in fifteenth_words:
        fifteenth_words_by_first_last[x[0] + x[-1]].append(x)
    return fifteenth_words_by_first_last
