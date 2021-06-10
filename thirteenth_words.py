import copy
from collections import defaultdict

from generate_dict import ALL_WORDS
from utils import points, is_word_possible, INITIAL_COUNT, VALUES, possible_scores, add_blanks_7, add_blanks_4, \
    END_LETTER_OF_2_POINTS_DUO


def get_thirteenth_words(letters):
    multiplier = [1, 1, 1, 2]
    thirteenth_words = [x for x in ALL_WORDS[4] if points(x, multiplier, 3) >= 18]
    thirteenth_words = [x for x in thirteenth_words if x[1] in END_LETTER_OF_2_POINTS_DUO]
    thirteenth_words = [x for x in thirteenth_words if x[2] in END_LETTER_OF_2_POINTS_DUO]
    thirteenth_words = [x for x in thirteenth_words if x[3] in END_LETTER_OF_2_POINTS_DUO]
    thirteenth_words, _ = add_blanks_4(thirteenth_words)
    thirteenth_words = [x for x in thirteenth_words if points(x, multiplier, 3) >= 18]
    thirteenth_words, _ = add_blanks_4(thirteenth_words)
    thirteenth_words = [x for x in thirteenth_words if points(x, multiplier, 3) == 18]
    thirteenth_words = [x for x in thirteenth_words if is_word_possible(x, letters)]
    thirteenth_words = [x for x in thirteenth_words if VALUES[x[1]] == 1]
    thirteenth_words = [x for x in thirteenth_words if VALUES[x[2]] <= 1 and VALUES[x[3]] <= 1]
    return thirteenth_words