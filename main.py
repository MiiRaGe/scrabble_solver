# This is a sample Python script.
import copy
import sys
import json
import hashlib
from collections import defaultdict

from eigth_words import get_eighth_words_by_third_last
from eigtheenth_words import get_eighteenth_words_by_first
from eleventh_word import get_eleventh_words_by_last
from fifteenth_words import get_fifteenth_words_by_first_last
from fifth_words import get_fifth_words_by_first_and_fifth
from fourteenth_word import get_fourteenth_words
from generate_dict import TWL, SOWPODS
from nineth_words import get_ninth_words_by_duo_letter
from seventeenth_words import get_seventeenth_words_by_last
from seventh_words import get_seventh_words_by_first_fourth
from sixteenth_words import get_sixteenth_words_by_last
from sixth_word import get_sixth_words_by_first_fifth
from tenth_words import get_tenth_words_by_third_letter
from thirteenth_words import get_thirteenth_words
from twelveth_words import get_twelveth_words
from twentieth_words import get_twentieth_words_by_first
from first_words import get_first_words
from fourth_words import get_fourth_words_by_fourth
from second_words import get_second_words_by_sixth
from third_words import get_third_words_by_fourth
from utils import is_word_possible, points, INITIAL_COUNT, \
    TWO_LETTERS_SET_BY_POINTS, TWO_LETTERS_SET


def summary(possibilities):
    summary = defaultdict(set)
    for possibility in possibilities:
        for (i, word) in enumerate(possibility['words']):
            summary[i].add(word)
    if not possibilities:
        return
    for i in range(0, len(possibilities[0]['words'])):
        words = summary[i] if len(summary[i]) <= 20 else ''
        print('{}: {} {}'.format(i, len(summary[i]), words))


def sum_letters(possibilities):
    letter_sum = defaultdict(set)
    for possibility in possibilities:
        for (letter, count) in possibility['letters'].items():
            letter_sum[letter].add(count)
    for (letter, counts) in letter_sum.items():
        print("'{}': {},".format(letter, max(counts)))


def display_status(possibilities):
    print(len(possibilities))
    summary(possibilities)
    print(possibilities[0]['words'])


def get_max_letters(possibilities):
    if not possibilities:
        return defaultdict(lambda: 0)
    letter_sum = defaultdict(set)
    for possibility in possibilities:
        for (letter, count) in possibility['letters'].items():
            letter_sum[letter].add(count)
    for (letter, counts) in letter_sum.items():
        letter_sum[letter] = max(counts)
    return letter_sum


def try_to_solve(scores, last_letter, dictionnary, variant):
    letters = copy.copy(INITIAL_COUNT)
    letters[last_letter] -= 1
    possibilities = []
    # First 120
    for first_word in get_first_words(letters, dictionnary):
        possibilities.append({'words': [first_word],
                              'letters': is_word_possible(first_word, copy.copy(INITIAL_COUNT))})

    # print('Adding 1st: Before/After {} {}'.format(0, len(possibilities)))
    # return possibilities
    # Second word 102
    letters = get_max_letters(possibilities)
    second_words_by_sixth = get_second_words_by_sixth(letters, dictionnary)
    new_possibilities = []
    for possibility in possibilities:
        words = second_words_by_sixth[possibility['words'][0][2]]
        for second_word in words:
            letters = is_word_possible(second_word, possibility['letters'], {second_word[5]: 1})
            if not letters:
                continue
            new_possibilities.append(
                {'words': possibility['words'] + [second_word], 'letters': letters})
    # print('Adding 2nd: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities

    # Third word 89 - quixotic
    letters = get_max_letters(possibilities)
    third_words_by_fourth = get_third_words_by_fourth(letters, dictionnary)
    new_possibilities = []
    for possibility in possibilities:
        words = third_words_by_fourth[possibility['words'][1][1]]
        for third_word in words:
            letters = is_word_possible(third_word, possibility['letters'], {possibility['words'][1][1]: 1})
            if not letters:
                continue
            new_possibilities.append(
                {'words': possibility['words'] + [third_word],
                 'letters': letters})
    # print('Adding 3rd: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities

    # Fourth word 66 - kumquat
    letters = get_max_letters(possibilities)
    fourth_words_by_fourth = get_fourth_words_by_fourth(letters, dictionnary)
    new_possibilities = []
    for possibility in possibilities:
        words = fourth_words_by_fourth[possibility['words'][2][0]]
        for fourth_word in words:
            letters = is_word_possible(fourth_word, possibility['letters'], {possibility['words'][2][0]: 1})
            if not letters:
                continue
            new_possibilities.append(
                {'words': possibility['words'] + [fourth_word], 'letters': letters})
    # print('Adding 4th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities

    # display_status(possibilities)
    # Fifth word 66 - ?
    letters = get_max_letters(possibilities)
    fifth_words_by_first_and_fifth = get_fifth_words_by_first_and_fifth(letters, dictionnary)
    new_possibilities = []
    for possibility in possibilities:
        words = fifth_words_by_first_and_fifth[possibility['words'][2][-1] + possibility['words'][0][-1]]
        for fifth_word in words:
            extra_letters = defaultdict(lambda: 0)
            extra_letters[possibility['words'][0][-1]] += 1
            extra_letters[possibility['words'][2][-1]] += 1
            letters = is_word_possible(fifth_word, possibility['letters'], extra_letters)
            if not letters:
                continue
            new_possibilities.append(
                {'words': possibility['words'] + [fifth_word], 'letters': letters})

    # print('Adding 5th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities

    # Sixth word - 74
    letter = get_max_letters(possibilities)
    sixth_words_by_first_fifth = get_sixth_words_by_first_fifth(letters, dictionnary)
    new_possibilities = []
    for possibility in possibilities:
        words = sixth_words_by_first_fifth[possibility['words'][1][-1] + possibility['words'][4][6]]
        for sixth_word in words:
            extra_letters = defaultdict(lambda: 0)
            extra_letters[possibility['words'][1][-1]] += 1
            extra_letters[possibility['words'][4][6]] += 1
            letters = is_word_possible(sixth_word, possibility['letters'], extra_letters)
            if not letters:
                continue
            new_possibilities.append(
                {'words': possibility['words'] + [sixth_word], 'letters': letters})
    print('Adding 6th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities

    # Seventh word - 29
    score = 29
    letters = get_max_letters(possibilities)
    seventh_words_by_first_fourth = get_seventh_words_by_first_fourth(letters, score, dictionnary)
    new_possibilities = []
    for possibility in possibilities:
        extra_letters = defaultdict(lambda: 0)
        extra_letters[possibility['words'][3][5]] += 1
        extra_letters[possibility['words'][1][3]] += 1
        first_fourth = possibility['words'][3][5] + possibility['words'][1][3]
        words = seventh_words_by_first_fourth[first_fourth]
        for seventh_word in words:
            letters = is_word_possible(seventh_word, possibility['letters'], extra_letters)
            if not letters:
                continue
            new_possibilities.append(
                {'words': possibility['words'] + [seventh_word], 'letters': letters})
    print('Adding 7th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities

    # 8th -
    letters = get_max_letters(possibilities)
    score = scores['8th']
    eighth_words_by_third_last = get_eighth_words_by_third_last(letters, score, dictionnary)
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
            new_possibilities.append({'words': possibility['words'] + [word], 'letters': letters})
    print('Adding 8th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities
    if not possibilities:
        return

    # 14th word 18 points
    letters = get_max_letters(possibilities)
    fourteenth_words = get_fourteenth_words(letters, dictionnary)
    new_possibilities = []
    for possibility in possibilities:
        for word in fourteenth_words:
            letters = is_word_possible(word, possibility['letters'])
            if not letters:
                continue
            first_duo = possibility['words'][5][-3] + word[0]
            second_duo = possibility['words'][5][-2] + word[1]
            if first_duo not in TWO_LETTERS_SET_BY_POINTS[3]:
                continue
            if second_duo not in TWO_LETTERS_SET_BY_POINTS[2]:
                continue
            new_possibilities.append(
                {'words': possibility['words'] + [word], 'letters': letters})
    print('Adding 14th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities
    if not possibilities:
        return
    # 9th
    score = scores['9th']
    letters = get_max_letters(possibilities)
    ninth_words_by_duo_letter = get_ninth_words_by_duo_letter(letters, score, dictionnary, variant)
    new_possibilities = []
    for possibility in possibilities:
        duo = possibility['words'][5][-1] + possibility['words'][-1][2]
        words = ninth_words_by_duo_letter[duo]
        for word in words:
            extra_letters = defaultdict(lambda: 0)
            extra_letters[possibility['words'][5][-1]] += 1
            extra_letters[possibility['words'][-1][2]] += 1
            letters = is_word_possible(word, possibility['letters'], extra_letters)
            if not letters:
                continue
            new_possibilities.append(
                {'words': possibility['words'] + [word], 'letters': letters})
    print('Adding 9th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities
    if not possibilities:
        return

    # 10th word 6 letters
    letters = get_max_letters(possibilities)
    score = scores['10th']
    tenth_words_by_third_letter = get_tenth_words_by_third_letter(letters, scores, dictionnary, variant)
    new_possibilities = []
    for possibility in possibilities:
        if variant['1'] == 1:
            extra_letters = {}
            for last, words in tenth_words_by_third_letter.items():
                if possibility['words'][-1] + last not in dictionnary[5]:
                    continue
                for word in words:
                    letters = is_word_possible(word, possibility['letters'], extra_letters)
                    if not letters:
                        continue
                    new_possibilities.append(
                        {'words': possibility['words'] + [word], 'letters': letters})
        else:
            extra_letters = {possibility['words'][8][-1]: 1}
            words = tenth_words_by_third_letter[possibility['words'][-1][-1]]
            for word in words:
                letters = is_word_possible(word, possibility['letters'], extra_letters)
                if not letters:
                    continue
                new_possibilities.append(
                    {'words': possibility['words'] + [word], 'letters': letters})
    print('Adding 10th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities
    if not possibilities:
        return
    # 11th word 86 points
    letters = get_max_letters(possibilities)
    eleventh_words_by_last = get_eleventh_words_by_last(letters, dictionnary)
    new_possibilities = []
    for possibility in possibilities:
        words = eleventh_words_by_last[possibility['words'][-1][-1]]
        for word in words:
            extra_letters = {possibility['words'][-1][-1]: 1}
            letters = is_word_possible(word, possibility['letters'], extra_letters)
            if not letters:
                continue
            new_possibilities.append(
                {'words': possibility['words'] + [word], 'letters': letters})
    print('Adding 11th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities
    if not possibilities:
        return
    # 12th word 7 letters
    letters = get_max_letters(possibilities)
    twelveth_words = get_twelveth_words(letters, dictionnary, scores, variant)
    new_possibilities = []
    for possibility in possibilities:
        for word in twelveth_words:
            if word[-2] + possibility['words'][-1][0] not in TWO_LETTERS_SET:
                continue
            if word[-1] + possibility['words'][-1][1] not in TWO_LETTERS_SET:
                continue
            extra_letters = {}
            letters = is_word_possible(word, possibility['letters'], extra_letters)
            if not letters:
                continue
            new_possibilities.append(
                {'words': possibility['words'] + [word], 'letters': letters})
    print('Adding 12th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities
    if not possibilities:
        return
    # 15th word 18 points
    score = scores['15th']
    letters = get_max_letters(possibilities)
    fifteenth_words_by_first_last = get_fifteenth_words_by_first_last(letters, score, dictionnary, variant)
    new_possibilities = []
    for possibility in possibilities:
        words = fifteenth_words_by_first_last[possibility['words'][4][1] + possibility['words'][-1][3]]
        extra_letters = defaultdict(lambda: 0)
        extra_letters[possibility['words'][4][1]] += 1
        extra_letters[possibility['words'][-1][3]] += 1
        for word in words:
            letters = is_word_possible(word, possibility['letters'], extra_letters)
            if not letters:
                continue
            new_possibilities.append(
                {'words': possibility['words'] + [word], 'letters': letters})
    print('Adding 15th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities
    if not possibilities:
        return
    # 16th word
    score = scores['16th']
    letters = get_max_letters(possibilities)
    sixteenth_words_by_last = get_sixteenth_words_by_last(letters, score, dictionnary)
    new_possibilities = []
    for possibility in possibilities:
        words = sixteenth_words_by_last[possibility['words'][-1][4]]
        extra_letters = {possibility['words'][-1][4]: 1}
        for word in words:
            letters = is_word_possible(word, possibility['letters'], extra_letters)
            if not letters:
                continue
            new_possibilities.append(
                {'words': possibility['words'] + [word], 'letters': letters})
    print('Adding 16th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities
    if not possibilities:
        return
    # 17th word
    score = scores['17th']
    letters = get_max_letters(possibilities)
    seventeenth_words_by_last = get_seventeenth_words_by_last(letters, score, dictionnary)
    new_possibilities = []
    for possibility in possibilities:
        words = seventeenth_words_by_last[possibility['words'][5][-1]]
        extra_letters = {possibility['words'][5][-1]: 1}
        for word in words:
            letters = is_word_possible(word, possibility['letters'], extra_letters)
            if not letters:
                continue
            new_possibilities.append(
                {'words': possibility['words'] + [word], 'letters': letters})
    print('Adding 17th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities
    if not possibilities:
        return
    # 18th Word - 6 points
    letters = get_max_letters(possibilities)
    eighteenth_words_by_first = get_eighteenth_words_by_first(letters, dictionnary)
    new_possibilities = []
    for possibility in possibilities:
        eighteenth_words = eighteenth_words_by_first[possibility['words'][-1][0]]
        extra_letters = defaultdict(lambda: 0)
        extra_letters[possibility['words'][-1][0]] += 1
        for eighteenth_word in eighteenth_words:
            letters = is_word_possible(eighteenth_word, possibility['letters'], extra_letters)
            if not letters:
                continue
            new_possibilities.append(
                {'words': possibility['words'] + [eighteenth_word], 'letters': letters})
    print('Adding 18th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities
    if not possibilities:
        return
    # LAST WORD - ?
    letters = get_max_letters(possibilities)
    twentieth_words_by_first = get_twentieth_words_by_first(letters, dictionnary)
    new_possibilities = []
    for possibility in possibilities:
        eigthteenth_word = possibility['words'][-1]
        words = twentieth_words_by_first[eigthteenth_word[-1]]
        for twentieth_word in words:
            letters = is_word_possible(twentieth_word, possibility['letters'], {twentieth_word[0]: 1})
            if not letters:
                print('No letters :(')
                continue
            new_possibilities.append(
                {'words': possibility['words'] + [twentieth_word], 'letters': letters})
    print('Adding last: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities
    if not possibilities:
        return
    # 13th word 18 points
    letters = get_max_letters(possibilities)
    thirteenth_words = get_thirteenth_words(letters, dictionnary)
    new_possibilities = []
    for possibility in possibilities:
        twelveth_word = possibility['words'][12]
        extra_letters = {}
        for word in thirteenth_words:
            if twelveth_word[0] + word[1] not in TWO_LETTERS_SET:
                print('Not a valid set:', twelveth_word[0] + word[1])
                continue
            if points(twelveth_word[1] + word[2]) != 1:
                print(twelveth_word[1] + word[2], '!= 1')
                continue
            if points(twelveth_word[2] + word[3], None, 2) != 2:
                print(twelveth_word[2] + word[3], '!= 2')
                continue
            letters = is_word_possible(word, possibility['letters'], extra_letters)
            if not letters:
                print('No letters :(')
                continue
            new_possibilities.append(
                {'words': possibility['words'] + [word], 'letters': letters})
    print('Adding 13th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities

    if possibilities:
        return possibilities


if __name__ == '__main__':
    config = json.loads(sys.argv[1])
    hash = hashlib.md5(sys.argv[1].encode('utf8')).hexdigest()

    dictionnary = None
    if config['dictionnary'] == 'sowpods':
        dictionnary = SOWPODS
    elif config['dictionnary'] == 'twl':
        dictionnary = TWL
    if not dictionnary:
        print('Wrong dictionnary param')

    result = try_to_solve(config['scores'],config['last_letter'],dictionnary, config['variant'])
    if result:
        with open('solutions/solution_{}.json'.format(hash), 'w') as solution:
            json.dump(config, solution)
            solution.write('\n')
            json.dump(result, solution)