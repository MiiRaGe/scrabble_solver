import copy
from collections import defaultdict

from utils import points, is_word_possible, VALUES, END_LETTER_OF_2_POINTS_DUO, get_max_letters, TWO_LETTERS_SET, \
    add_word_to_list


def get_eleventh_words_by_last(letters, words):
    multiplier = [1, 1, 1, 1, 1, 2, 1, 1]
    eleventh_words = [x for x in words[8] if points(x, multiplier, 3) == 36]
    eleventh_words = [x for x in eleventh_words if is_word_possible(x, letters, {x[-1]: 1})]
    eleventh_words = [x for x in eleventh_words if VALUES[x[0]] == VALUES[x[1]] == 1]
    eleventh_words = [x for x in eleventh_words if x[0] in END_LETTER_OF_2_POINTS_DUO]
    eleventh_words = [x for x in eleventh_words if x[1] in END_LETTER_OF_2_POINTS_DUO]
    eleventh_words_by_last = defaultdict(list)
    for x in eleventh_words:
        eleventh_words_by_last['-'].append(x)
        eleventh_words_by_last[x[-1]].append(x)
    return eleventh_words_by_last


def guess_11th_word(possibilities, scores, dictionary, variant):
    letters = get_max_letters(possibilities)
    eleventh_words_by_last = get_eleventh_words_by_last(letters, dictionary)
    new_possibilities = []
    for possibility in possibilities:
        key = '-'
        if possibility['words'][9]:
            key = possibility['words'][9][-1]
        words = eleventh_words_by_last[key]
        for word in words:
            if possibility['words'][11]:
                if possibility['words'][11][-2] + word[0] not in TWO_LETTERS_SET:
                    continue
                if possibility['words'][11][-1] + word[1] not in TWO_LETTERS_SET:
                    continue
            letters = is_word_possible(word, possibility['letters'], {word[-1]: 1})
            if not letters:
                continue
            new_possibilities.append(
                {'words': add_word_to_list(word, possibility['words'], 10), 'letters': letters})
    print('Adding 11th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    return new_possibilities
