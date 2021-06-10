import copy
from collections import defaultdict

from generate_dict import ALL_WORDS
from utils import points, is_word_possible, INITIAL_COUNT


def get_extra_letters(x):
    extra_letters = defaultdict(lambda: 0)
    extra_letters[x[0]] += 1
    extra_letters[x[1]] += 1


def get_ninth_words_by_duo_letter(letters, score):
    ninth_words = [x for x in ALL_WORDS[5] if is_word_possible(x, letters, get_extra_letters(x))]
    multiplier = [1, 1, 1, 1, 1]
    ninth_words = [x for x in ninth_words if points(x, multiplier, 2) == score]
    ninth_words_by_duo_letter = defaultdict(list)
    for x in ninth_words:
        ninth_words_by_duo_letter[x[0]+x[1]].append(x)
    return ninth_words_by_duo_letter
