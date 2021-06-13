import copy
from collections import defaultdict

from utils import points, is_word_possible, get_max_letters, add_word_to_list


def get_seventeenth_words_by_first_last(letters, score, words):
    multiplier = [1, 1, 1, 1, 1]
    seventeenth_words = [x for x in words[5] if points(x, multiplier, 2) == score]
    seventeenth_words = [x for x in seventeenth_words if is_word_possible(x, letters, {x[-1]: 1})]

    seventeenth_words_by_first_last = defaultdict(list)
    for x in seventeenth_words:
        seventeenth_words_by_first_last['-' + x[-1]].append(x)
        seventeenth_words_by_first_last[x[0] + x[-1]].append(x)
    return seventeenth_words_by_first_last


def guess_17th_word(possibilities, scores, dictionary, variant):
    score = scores['17th']
    letters = get_max_letters(possibilities)
    seventeenth_words_by_first_last = get_seventeenth_words_by_first_last(letters, score, dictionary)
    new_possibilities = []
    for possibility in possibilities:
        if possibility['words'][17]:
            key = possibility['words'][17][0]
        else:
            key = '-'
        key += possibility['words'][5][-1]
        words = seventeenth_words_by_first_last[key]
        extra_letters = {possibility['words'][5][-1]: 1}
        for word in words:
            letters = is_word_possible(word, possibility['letters'], extra_letters)
            if not letters:
                continue
            new_possibilities.append(
                {'words': add_word_to_list(word, possibility['words'], 16), 'letters': letters})
    print('Adding 17th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    return new_possibilities