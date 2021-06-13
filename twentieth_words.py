import copy
from collections import defaultdict

from utils import points, is_word_possible, VALUES, get_max_letters, add_word_to_list


def get_twentieth_words(letters, words, variant):
    twentieth_words = [x for x in words[5] if is_word_possible(x, letters, {x[0]: 1})]
    if variant['3'] == '1':
        multiplier = [2, 1, 1, 1, 1]
        twentieth_words = [x for x in twentieth_words if points(x, multiplier, 3) + 6 + VALUES[x[0]] == 48]
    else:
        multiplier = [1, 1, 1, 1, 1]
        twentieth_words = [x for x in twentieth_words if points(x, multiplier, 3) == 48]
    twentieth_words_by_first = defaultdict(list)
    for x in twentieth_words:
        twentieth_words_by_first['-'].append(x)
        twentieth_words_by_first[x[0]].append(x)
    return twentieth_words_by_first


def guess_20th_word(possibilities, scores, dictionary, variant):
    letters = get_max_letters(possibilities)
    twentieth_words_by_first = get_twentieth_words(letters, dictionary, variant)
    new_possibilities = []
    for possibility in possibilities:
        key = '-'
        if possibility['words'][17]:
            key = possibility['words'][17][-1]
        words = twentieth_words_by_first[key]
        for twentieth_word in words:
            letters = is_word_possible(twentieth_word, possibility['letters'], {twentieth_word[0]: 1})
            if not letters:
                continue
            new_possibilities.append(
                {'words': add_word_to_list(twentieth_word, possibility['words'], 19), 'letters': letters})
    print('Adding 20th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    return new_possibilities
