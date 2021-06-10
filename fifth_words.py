import copy
from collections import defaultdict

from generate_dict import ALL_WORDS
from utils import points, is_word_possible, INITIAL_COUNT


def get_extra_letters(x):
    extra_letters = defaultdict(lambda: 0)
    extra_letters[x[0]] += 1
    extra_letters[x[4]] += 1
    return extra_letters


def get_fifth_words_by_first_and_fifth(letters):
    multiplier = [1, 1, 1, 1, 1, 1, 1, 1, 2]
    fifth_words = [x for x in ALL_WORDS[9] if points(x, multiplier) == 16]

    fifth_words = [x for x in fifth_words if is_word_possible(x, letters, get_extra_letters(x))]

    fifth_words_by_first_and_fifth = defaultdict(list)

    for x in fifth_words:
        fifth_words_by_first_and_fifth[x[0] + x[4]].append(x)
    return fifth_words_by_first_and_fifth


if __name__ == '__main__':
    print(get_fifth_words_by_first_and_fifth(INITIAL_COUNT)['cl'])