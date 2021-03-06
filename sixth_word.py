import copy
from collections import defaultdict

from generate_dict import SOWPODS
from utils import points, is_word_possible, VALUES, START_LETTER_OF_3_POINTS_DUO, INITIAL_COUNT


def get_extra_letters(x):
    extra_letters = defaultdict(lambda: 0)
    extra_letters[x[0]] += 1
    extra_letters[x[4]] += 1
    return extra_letters


def get_sixth_words_by_first_fifth(letters, words):
    multiplier = [1, 1, 3, 1, 1, 1, 3, 1, 1]
    sixth_words = [x for x in words[9] if points(x, multiplier) == 24]
    sixth_words = [x for x in sixth_words if is_word_possible(x, letters, get_extra_letters(x))]
    sixth_words = [x for x in sixth_words if VALUES[x[-2]] == 1]
    sixth_words = [x for x in sixth_words if x[-3] in START_LETTER_OF_3_POINTS_DUO]

    sixth_words_by_first_fifth = defaultdict(list)
    for x in sixth_words:
        sixth_words_by_first_fifth[x[0]+x[4]].append(x)
    return sixth_words_by_first_fifth


if __name__ == '__main__':
    get_sixth_words_by_first_fifth(INITIAL_COUNT, SOWPODS)
    get_sixth_words_by_first_fifth(INITIAL_COUNT, SOWPODS)
    get_sixth_words_by_first_fifth(INITIAL_COUNT, SOWPODS)
    get_sixth_words_by_first_fifth(INITIAL_COUNT, SOWPODS)
    get_sixth_words_by_first_fifth(INITIAL_COUNT, SOWPODS)
    get_sixth_words_by_first_fifth(INITIAL_COUNT, SOWPODS)
    get_sixth_words_by_first_fifth(INITIAL_COUNT, SOWPODS)