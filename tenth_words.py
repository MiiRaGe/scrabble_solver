import copy
from collections import defaultdict

from generate_dict import SOWPODS
from utils import points, is_word_possible, INITIAL_COUNT, VALUES


def get_tenth_words_by_third_letter(letters, scores, words, variant):
    multiplier = [3, 1, 1, 1, 1, 1]
    if variant['1'] == 1:
        tenth_words = [x for x in words[6] if points(x, multiplier, 2) + scores['9th'] / 2 + VALUES[x[2]] == scores['10th']]
    else:
        tenth_words = [x for x in words[6] if points(x, multiplier, 2) == scores['10th']]
    tenth_words = [x for x in tenth_words if is_word_possible(x, letters, {x[2]: 1})]
    tenth_words_by_third_letter = defaultdict(list)
    for x in tenth_words:
        tenth_words_by_third_letter[x[2]].append(x)
    return tenth_words_by_third_letter



if __name__ == '__main__':
    words = get_tenth_words_by_third_letter(INITIAL_COUNT, {'9th': 16, '10th': 40}, SOWPODS, {'1': 0})
    for k,v in words.items():
        print(k, len(v))
    words = get_tenth_words_by_third_letter(INITIAL_COUNT, {'9th': 16, '10th': 40}, SOWPODS, {'1': 1})
    for k,v in words.items():
        print(k, len(v))