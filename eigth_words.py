import copy
from collections import defaultdict

from generate_dict import ALL_WORDS
from utils import points, is_word_possible, INITIAL_COUNT


def get_extra_letters(x):
    extra_letters = defaultdict(lambda: 0)
    extra_letters[x[2]] += 1
    extra_letters[x[-1]] += 1


def get_eighth_words_by_third_last(letters, score):
    eighth_words = [x for x in ALL_WORDS[5]]
    eighth_words = [x for x in eighth_words if is_word_possible(x, letters, get_extra_letters(x))]
    multiplier = [3, 1, 1, 1, 1]
    eighth_words = [x for x in eighth_words if points(x, multiplier) == score]
    eighth_words_by_third_last = defaultdict(list)
    for x in eighth_words:
        eighth_words_by_third_last[x[2]+x[-1]].append(x)
    return eighth_words_by_third_last


if __name__ == '__main__':
    print(len(get_eighth_words_by_third_last(INITIAL_COUNT)['ty']))