import copy
from collections import defaultdict

from generate_dict import TWL
from utils import points, is_word_possible, VALUES, INITIAL_COUNT, get_max_letters, add_word_to_list


def get_eighteenth_words(letters, words, variant):
    eighteenth_words = [x for x in words[4] if is_word_possible(x, letters, {x[0]: 1})]
    eighteenth_words = [x for x in eighteenth_words if VALUES[x[1]] == 1]
    if variant['3'] == 1:
        eighteenth_words = [x for x in eighteenth_words if points(x[0:3], [1, 1, 1], 1) == 6]
        eighteenth_words = [x for x in eighteenth_words if x[0:3] in words[3]]
    else:
        eighteenth_words = [x for x in eighteenth_words if points(x, [1, 1, 1, 2], 1) == 6]

    eighteenth_words_by_first_last = defaultdict(list)
    for x in eighteenth_words:
        eighteenth_words_by_first_last['--'].append(x)
        eighteenth_words_by_first_last[x[0] + '-'].append(x)
        eighteenth_words_by_first_last[x[0] + x[-1]].append(x)
        eighteenth_words_by_first_last['-' + x[-1]].append(x)
    return eighteenth_words_by_first_last


def guess_18th_word(possibilities, scores, dictionary, variant):
    letters = get_max_letters(possibilities)
    eighteenth_words_by_first_last = get_eighteenth_words(letters, dictionary, variant)
    new_possibilities = []
    for possibility in possibilities:
        if possibility['words'][16]:
            key = possibility['words'][16][0]
        else:
            key = '-'
        if possibility['words'][19]:
            key += possibility['words'][19][0]
        else:
            key += '-'
        words = eighteenth_words_by_first_last[key]
        for eighteenth_word in words:
            letters = is_word_possible(eighteenth_word, possibility['letters'], {eighteenth_word[0]: 1})
            if not letters:
                continue
            new_possibilities.append(
                {'words': add_word_to_list(eighteenth_word, possibility['words'], 17), 'letters': letters})
    print('Adding 18th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    return new_possibilities