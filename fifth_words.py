import copy
from collections import defaultdict

from utils import points, is_word_possible


def get_extra_letters(x):
    extra_letters = defaultdict(lambda: 0)
    extra_letters[x[0]] += 1
    extra_letters[x[4]] += 1
    return extra_letters


def get_fifth_words_by_first_and_fifth(letters, words):
    multiplier = [1, 1, 1, 1, 1, 1, 1, 1, 2]
    fifth_words = [x for x in words[9] if points(x, multiplier) == 16]

    fifth_words = [x for x in fifth_words if is_word_possible(x, letters, get_extra_letters(x))]

    fifth_words_by_first_and_fifth = defaultdict(list)

    for x in fifth_words:
        fifth_words_by_first_and_fifth[x[0] + x[4]].append(x)
    return fifth_words_by_first_and_fifth
