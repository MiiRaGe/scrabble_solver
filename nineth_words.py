import copy
from collections import defaultdict

from generate_dict import SOWPODS
from utils import points, is_word_possible, INITIAL_COUNT


def get_extra_letters(x):
    extra_letters = defaultdict(lambda: 0)
    extra_letters[x[0]] += 1
    extra_letters[x[1]] += 1


def get_ninth_words_by_duo_letter(letters, score, words, variant):
    ninth_words = [x for x in words[5] if is_word_possible(x, letters, get_extra_letters(x))]
    if variant['1'] == 1:
        multiplier = [1, 1, 1, 1, 1]
        ninth_words = [x for x in ninth_words if points(x, multiplier, 2) == score]
    else:
        multiplier = [1, 1, 1, 1]
        ninth_words = [x for x in ninth_words if x[0:4] in words[4]]
        ninth_words = [x for x in ninth_words if points(x[0:4], multiplier, 2) == score]
    ninth_words_by_duo_letter = defaultdict(list)
    for x in ninth_words:
        ninth_words_by_duo_letter[x[0] + x[1]].append(x)
    return ninth_words_by_duo_letter


if __name__ == '__main__':
    words = get_ninth_words_by_duo_letter(INITIAL_COUNT, 22, SOWPODS, {'1': 1})
    for k,v in words.items():
        print(k, len(v))
    words = get_ninth_words_by_duo_letter(INITIAL_COUNT, 22, SOWPODS, {'1': 0})
    for k, v in words.items():
        print(k, len(v))
