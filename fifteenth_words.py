from collections import defaultdict

from utils import points, is_word_possible


def get_extra_letters(x):
    extra_letters = defaultdict(lambda: 0)
    extra_letters[x[0]] += 1
    extra_letters[x[-1]] += 1
    return extra_letters


def get_fifteenth_words_by_first_or_first_last(letters, score, words, variant):
    if variant['2'] == 1:
        fifteenth_words = [x for x in words[7] if points(x[0:6], None, 2) == score]
    else:
        fifteenth_words = [x for x in words[7] if points(x, None, 2) == score]
    fifteenth_words = [x for x in fifteenth_words if is_word_possible(x, letters, get_extra_letters(x))]
    fifteenth_words_by_first_last = defaultdict(list)
    fifteenth_words_by_first = defaultdict(list)
    for x in fifteenth_words:
        fifteenth_words_by_first_last[x[0] + x[-1]].append(x)
        fifteenth_words_by_first[x[0]].append(x)

    return fifteenth_words_by_first, fifteenth_words_by_first_last