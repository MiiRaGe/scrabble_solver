import copy
from collections import defaultdict

from generate_dict import SOWPODS, TWL
from utils import points, is_word_possible, INITIAL_COUNT


def get_extra_letters(x):
    extra_letters = defaultdict(lambda: 0)
    extra_letters[x[0]] += 1
    extra_letters[x[3]] += 1


def get_seventh_words_by_first_fourth(letters, score, words):
    seventh_words_6_base = [x for x in words[6]]
    seventh_words_6_base = [x for x in seventh_words_6_base if is_word_possible(x, letters, get_extra_letters(x))]
    multiplier = [1, 3, 1, 1, 1, 3]
    seventh_words = [x for x in seventh_words_6_base if points(x, multiplier) == score]
    seventh_words_by_first_fourth = defaultdict(list)
    for x in seventh_words:
        seventh_words_by_first_fourth[x[0]+x[3]].append(x)
    return seventh_words_by_first_fourth

