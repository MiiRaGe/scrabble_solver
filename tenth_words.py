import copy
from collections import defaultdict

from generate_dict import ALL_WORDS
from utils import points, is_word_possible, INITIAL_COUNT


def get_tenth_words_by_third_letter(letters, score):
    multiplier = [3, 1, 1, 1, 1, 1]
    tenth_words = [x for x in ALL_WORDS[6] if points(x, multiplier, 2) == score]
    tenth_words = [x for x in tenth_words if is_word_possible(x, letters, {x[2]: 1})]
    tenth_words_by_third_letter = defaultdict(list)
    for x in tenth_words:
        tenth_words_by_third_letter[x[2]].append(x)
    return tenth_words_by_third_letter

