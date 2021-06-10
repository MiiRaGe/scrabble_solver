import copy
from collections import defaultdict

from generate_dict import ALL_WORDS
from utils import points, is_word_possible, INITIAL_COUNT


def get_second_words_by_sixth(letters):
    second_words = [x for x in ALL_WORDS[8] if points(x, None, 2) == 52]
    second_words = [x for x in second_words if is_word_possible(x, letters, {x[5]: 1})]

    second_words_by_sixth = defaultdict(list)
    for x in second_words:
        second_words_by_sixth[x[5]].append(x)
    return second_words_by_sixth


if __name__ == '__main__':
    print(get_second_words_by_sixth(INITIAL_COUNT))