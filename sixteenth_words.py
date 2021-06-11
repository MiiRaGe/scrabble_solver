from collections import defaultdict

from utils import points, is_word_possible


def get_sixteenth_words_by_last(letters, score, words):
    multiplier = [2, 1, 1, 1, 1]
    sixteenth_words = [x for x in words[5] if points(x, multiplier, 2) == score]
    sixteenth_words = [x for x in sixteenth_words if is_word_possible(x, letters, {x[-1]: 1})]

    sixteenth_words_by_last = defaultdict(list)
    for x in sixteenth_words:
        sixteenth_words_by_last[x[-1]].append(x)
    return sixteenth_words_by_last
