import copy
from collections import defaultdict

from generate_dict import ALL_WORDS
from utils import points, is_word_possible, INITIAL_COUNT, VALUES


def get_twentieth_words(letters):
    multiplier = [2, 1, 1, 1, 1]
    twentieth_words = [x for x in ALL_WORDS[5] if points(x, multiplier, 3) + 6 + VALUES[x[0]] * 2 == 48]
    twentieth_words = [x for x in twentieth_words if is_word_possible(x, letters, {})]
    return twentieth_words


def get_twentieth_words_by_first(letters):
    multiplier = [1, 1, 1, 1, 1]
    twentieth_words = [x for x in ALL_WORDS[5] if points(x, multiplier, 3) == 48]
    twentieth_words = [x for x in twentieth_words if is_word_possible(x, letters, {x[0]: 1})]
    twentieth_words_by_first = defaultdict(list)
    for x in twentieth_words:
        twentieth_words_by_first[x[0]].append(x)
    return twentieth_words_by_first


if __name__ == '__main__':
    letters = {'*': 1, 'a': 6, 'b': 0, 'c': 0, 'd': 1, 'e': 5, 'f': 2, 'g': 1, 'h': 1, 'i': 2, 'j': 0, 'k': 0, 'l': 2, 'm': 0, 'n': 5, 'o': 2, 'p': 1, 'q': 0, 'r': 6, 's': 2, 't': 4, 'u': 1, 'v': 1, 'w': 0, 'x': 0, 'y': 1, 'z': 0}
    words_by_first = get_twentieth_words_by_first(letters)
    print(list(words_by_first[x] for x in {'s', 'n', 'o', 'e', 'i', 'a'}))