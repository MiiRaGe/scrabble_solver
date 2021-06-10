import copy
from collections import defaultdict

from generate_dict import ALL_WORDS
from utils import points, is_word_possible, INITIAL_COUNT


def get_fourth_words_by_fourth(letters):
    fourth_words = [x for x in ALL_WORDS[7] if points(x, None, 3) == 66 and is_word_possible(x, letters, {x[3]: 1})]

    fourth_words_by_fourth = defaultdict(list)
    for x in fourth_words:
        fourth_words_by_fourth[x[3]].append(x)
    return fourth_words_by_fourth


if __name__ == '__main__':
    print(get_fourth_words_by_fourth(INITIAL_COUNT)['q'])