import copy
from collections import defaultdict

from generate_dict import SOWPODS
from utils import points, is_word_possible, INITIAL_COUNT, VALUES, get_max_letters, add_word_to_list


def get_tenth_words_by_third_last(letters, scores, words, variant):
    multiplier = [3, 1, 1, 1, 1, 1]
    if variant['1'] == 1:
        tenth_words = [x for x in words[6] if points(x, multiplier, 2) + scores['9th'] / 2 + VALUES[x[2]] == scores['10th']]
    else:
        tenth_words = [x for x in words[6] if points(x, multiplier, 2) == scores['10th']]
    tenth_words = [x for x in tenth_words if is_word_possible(x, letters, {x[2]: 1})]
    tenth_words_by_third_last = defaultdict(list)
    for x in tenth_words:
        tenth_words_by_third_last[x[2] + '-'].append(x)
        tenth_words_by_third_last[x[2] + x[-1]].append(x)
    return tenth_words_by_third_last


def guess_10th_word(possibilities, scores, dictionary, variant):
    letters = get_max_letters(possibilities)
    tenth_words_by_third_last = get_tenth_words_by_third_last(letters, scores, dictionary, variant)
    new_possibilities = []
    for possibility in possibilities:
        extra_letters = {possibility['words'][8][-1]: 1}
        key = possibility['words'][8][-1]
        if possibility['words'][10]:
            key += possibility['words'][10][-1]
        else:
            key += '-'
        words = tenth_words_by_third_last[key]
        for word in words:
            letters = is_word_possible(word, possibility['letters'], extra_letters)
            if not letters:
                continue
            new_possibilities.append(
                {'words': add_word_to_list(word, possibility['words'], 9), 'letters': letters})
    print('Adding 10th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    return new_possibilities
