import copy
from collections import defaultdict

from utils import points, is_word_possible, VALUES, END_LETTER_OF_2_POINTS_DUO


def get_eleventh_words_by_last(letters, words):
    multiplier = [1, 1, 1, 1, 1, 2, 1, 1]
    eleventh_words = [x for x in words[8] if points(x, multiplier, 3) == 36]
    eleventh_words = [x for x in eleventh_words if is_word_possible(x, letters, {x[-1]: 1})]
    eleventh_words = [x for x in eleventh_words if VALUES[x[0]] == VALUES[x[1]] == 1]
    eleventh_words = [x for x in eleventh_words if x[0] in END_LETTER_OF_2_POINTS_DUO]
    eleventh_words = [x for x in eleventh_words if x[1] in END_LETTER_OF_2_POINTS_DUO]
    eleventh_words_by_last = defaultdict(list)
    for x in eleventh_words:
        eleventh_words_by_last[x[-1]].append(x)
    return eleventh_words_by_last

