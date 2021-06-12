import copy
from collections import defaultdict

from utils import points, is_word_possible, VALUES, add_blanks_7, \
    START_LETTER_OF_2_POINTS_DUO


def get_compute_score_by_variant(variant, scores):
    multiplier = [1, 1, 1, 1, 1, 3, 1, 1]
    if variant['2'] == 1:
        def compute_score(x):
            return points(x, multiplier, 2) + VALUES[x[3]] + scores['15th'] // 2
    else:
        def compute_score(x):
            return points(x, multiplier, 2)
    return compute_score


def get_twelveth_words(letters, words, scores, variant):
    compute_score = get_compute_score_by_variant(variant, scores)
    twelveth_words = [x for x in words[7] if x[0] in START_LETTER_OF_2_POINTS_DUO]
    twelveth_words = [x for x in twelveth_words if x[1] in START_LETTER_OF_2_POINTS_DUO]
    twelveth_words = [x for x in twelveth_words if x[2] in START_LETTER_OF_2_POINTS_DUO]
    twelveth_words = [x for x in twelveth_words if x[-1] in START_LETTER_OF_2_POINTS_DUO]
    twelveth_words = [x for x in twelveth_words if x[-2] in START_LETTER_OF_2_POINTS_DUO]
    twelveth_words = [x for x in twelveth_words if compute_score(x) >= 28]
    twelveth_words, originals = add_blanks_7(twelveth_words)
    twelveth_words = [x for x in twelveth_words if compute_score(x) >= 28]
    twelveth_words, originals_2 = add_blanks_7(twelveth_words)
    twelveth_words = [x for x in twelveth_words if compute_score(x) == 28]
    twelveth_words = [x for x in twelveth_words if VALUES[x[0]] == VALUES[x[-1]] == VALUES[x[-2]] == 1]
    twelveth_words = [x for x in twelveth_words if VALUES[x[1]] <= 1 and VALUES[x[2]] in {0, 2}]
    twelveth_words = [x for x in twelveth_words if is_word_possible(x, letters)]
    twelveth_words_by_fourth = defaultdict(list)
    for x in twelveth_words:
        twelveth_words_by_fourth[x[3]].append(x)
    return twelveth_words, twelveth_words_by_fourth
