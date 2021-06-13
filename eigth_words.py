import copy
from collections import defaultdict

from generate_dict import SOWPODS, TWL
from utils import points, is_word_possible, INITIAL_COUNT, get_max_letters, add_word_to_list


def get_extra_letters(x):
    extra_letters = defaultdict(lambda: 0)
    extra_letters[x[2]] += 1
    extra_letters[x[-1]] += 1


def get_eighth_words_by_third_last(letters, score, words):
    eighth_words = [x for x in words[5]]
    eighth_words = [x for x in eighth_words if is_word_possible(x, letters, get_extra_letters(x))]
    multiplier = [3, 1, 1, 1, 1]
    eighth_words = [x for x in eighth_words if points(x, multiplier) == score]
    eighth_words_by_third_last = defaultdict(list)
    for x in eighth_words:
        eighth_words_by_third_last[x[2]+x[-1]].append(x)
    return eighth_words_by_third_last


def guess_8th_word(possibilities, scores, dictionary, variant):
    letters = get_max_letters(possibilities)
    score = scores['8th']
    eighth_words_by_third_last = get_eighth_words_by_third_last(letters, score, dictionary)
    new_possibilities = []
    for possibility in possibilities:
        possible_words = possibility['words']
        words = eighth_words_by_third_last[possible_words[2][-3] + possible_words[6][-1]]

        extra_letters = defaultdict(lambda: 0)
        extra_letters[possible_words[2][-3]] += 1
        extra_letters[possible_words[6][-1]] += 1
        for word in words:
            letters = is_word_possible(word, possibility['letters'], extra_letters)
            if not letters:
                continue
            new_possibilities.append({'words': add_word_to_list(word, possibility['words'], 7), 'letters': letters})
    print('Adding 8th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    return new_possibilities
