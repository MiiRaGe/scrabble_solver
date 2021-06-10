import copy
from collections import defaultdict

from generate_dict import ALL_WORDS
from utils import points, is_word_possible, INITIAL_COUNT, VALUES, END_LETTER_OF_2_POINTS_DUO


def get_eighteenth_words_by_first(letters):
    eighteenth_words = [x for x in ALL_WORDS[4] if points(x, [1,1,1,2], 1) == 6]
    eighteenth_words = [x for x in eighteenth_words if is_word_possible(x, letters, {x[0]: 1})]
    eighteenth_words = [x for x in eighteenth_words if VALUES[x[1]] == 1]
    eighteenth_words_by_first = defaultdict(list)
    for x in eighteenth_words:
        eighteenth_words_by_first[x[0]].append(x)
    return eighteenth_words_by_first


if __name__ == '__main__':
    letters = {'*': 1, 'a': 6, 'b': 0, 'c': 0, 'd': 1, 'e': 5, 'f': 2, 'g': 1, 'h': 1, 'i': 2, 'j': 0, 'k': 0, 'l': 2, 'm': 0, 'n': 5, 'o': 2, 'p': 1, 'q': 0, 'r': 6, 's': 2, 't': 4, 'u': 1, 'v': 1, 'w': 0, 'x': 0, 'y': 1, 'z': 0}
    print(get_eighteenth_words_by_first(letters))