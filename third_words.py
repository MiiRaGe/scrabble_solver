import copy
from collections import defaultdict

from generate_dict import ALL_WORDS
from utils import points, is_word_possible, INITIAL_COUNT


def get_third_words_by_fourth(letters):
    multiplier = [2, 1, 1, 1, 1, 1, 1, 2]
    third_words = [x for x in ALL_WORDS[8] if points(x, multiplier) == 39]
    third_words = [x for x in third_words if is_word_possible(x, letters, {x[3]: 1})]

    third_words_by_fourth = defaultdict(list)
    for x in third_words:
        third_words_by_fourth[x[3]].append(x)
    return third_words_by_fourth


if __name__ == '__main__':
    print(get_third_words_by_fourth(INITIAL_COUNT))