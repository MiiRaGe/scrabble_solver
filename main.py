# This is a sample Python script.
import copy
import sys
import json
import hashlib
from collections import defaultdict

from eigth_words import guess_8th_word
from eigtheenth_words import guess_18th_word
from eleventh_word import guess_11th_word
from fifteenth_words import guess_15th_word
from fifth_words import get_fifth_words_by_first_and_fifth
from fourteenth_word import get_fourteenth_words
from generate_dict import TWL, SOWPODS
from nineth_words import get_ninth_words_by_duo_letter
from seventeenth_words import guess_17th_word
from seventh_words import get_seventh_words_by_first_fourth
from sixteenth_words import guess_16th_word
from sixth_word import get_sixth_words_by_first_fifth
from tenth_words import guess_10th_word
from thirteenth_words import guess_13th_word
from twelveth_words import guess_12th_word
from twentieth_words import guess_20th_word
from first_words import get_first_words
from fourth_words import get_fourth_words_by_fourth
from second_words import get_second_words_by_sixth
from third_words import get_third_words_by_fourth
from utils import is_word_possible, INITIAL_COUNT, \
    TWO_LETTERS_SET_BY_POINTS, get_max_letters, add_word_to_list


def summary(possibilities):
    summary = defaultdict(set)
    for possibility in possibilities:
        for (i, word) in enumerate(possibility['words']):
            if word:
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


GUESS_FUNCTIONS = {
    '15th': guess_15th_word,
    '8th': guess_8th_word,
    '12th': guess_12th_word,
    '20th': guess_20th_word,
    '17th': guess_17th_word,
    '18th': guess_18th_word,
    '13th': guess_13th_word,
    '10th': guess_10th_word,
    '11th': guess_11th_word,
    '16th': guess_16th_word,
}


def try_to_solve(scores, last_letter, dictionary, variant):
    print(scores, last_letter, variant)
    letters = copy.copy(INITIAL_COUNT)
    letters[last_letter] -= 1
    possibilities = []
    # First 120
    for first_word in get_first_words(letters, dictionary):
        possibilities.append({'words': add_word_to_list(first_word, [], 0),
                              'letters': is_word_possible(first_word, copy.copy(INITIAL_COUNT))})

    # print('Adding 1st: Before/After {} {}'.format(0, len(possibilities)))
    # return possibilities
    # Second word 102
    letters = get_max_letters(possibilities)
    second_words_by_sixth = get_second_words_by_sixth(letters, dictionary)
    new_possibilities = []
    for possibility in possibilities:
        words = second_words_by_sixth[possibility['words'][0][2]]
        for second_word in words:
            letters = is_word_possible(second_word, possibility['letters'], {second_word[5]: 1})
            if not letters:
                continue
            new_possibilities.append(
                {'words': add_word_to_list(second_word, possibility['words'], 1), 'letters': letters})
    # print('Adding 2nd: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities

    # Third word 89 - quixotic
    letters = get_max_letters(possibilities)
    third_words_by_fourth = get_third_words_by_fourth(letters, dictionary)
    new_possibilities = []
    for possibility in possibilities:
        words = third_words_by_fourth[possibility['words'][1][1]]
        for third_word in words:
            letters = is_word_possible(third_word, possibility['letters'], {possibility['words'][1][1]: 1})
            if not letters:
                continue
            new_possibilities.append(
                {'words': add_word_to_list(third_word, possibility['words'], 2),
                 'letters': letters})
    # print('Adding 3rd: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities

    # Fourth word 66 - kumquat
    letters = get_max_letters(possibilities)
    fourth_words_by_fourth = get_fourth_words_by_fourth(letters, dictionary)
    new_possibilities = []
    for possibility in possibilities:
        words = fourth_words_by_fourth[possibility['words'][2][0]]
        for fourth_word in words:
            letters = is_word_possible(fourth_word, possibility['letters'], {possibility['words'][2][0]: 1})
            if not letters:
                continue
            new_possibilities.append(
                {'words': add_word_to_list(fourth_word, possibility['words'], 3), 'letters': letters})
    # print('Adding 4th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities

    # display_status(possibilities)
    # Fifth word 66 - ?
    letters = get_max_letters(possibilities)
    fifth_words_by_first_and_fifth = get_fifth_words_by_first_and_fifth(letters, dictionary)
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
                {'words': add_word_to_list(fifth_word, possibility['words'], 4), 'letters': letters})

    print('Adding 5th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities

    # Sixth word - 74
    letters = get_max_letters(possibilities)
    sixth_words_by_first_fifth = get_sixth_words_by_first_fifth(letters, dictionary)

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
                {'words': add_word_to_list(sixth_word, possibility['words'], 5), 'letters': letters})
    print('Adding 6th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities

    # Seventh word - 29
    score = 29
    letters = get_max_letters(possibilities)
    seventh_words_by_first_fourth = get_seventh_words_by_first_fourth(letters, score, dictionary)
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
                {'words': add_word_to_list(seventh_word, possibility['words'], 6), 'letters': letters})
    print('Adding 7th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities

    # 14th word 18 points
    letters = get_max_letters(possibilities)
    fourteenth_words = get_fourteenth_words(letters, dictionary)
    valid_2_of_5 = {x[0:2] for x in dictionary[5]}
    new_possibilities = []
    for possibility in possibilities:
        for word in fourteenth_words:
            letters = is_word_possible(word, possibility['letters'])
            if not letters:
                continue
            first_duo = possibility['words'][5][-3] + word[0]
            second_duo = possibility['words'][5][-2] + word[1]
            third_duo = possibility['words'][5][-1] + word[2]
            if first_duo not in TWO_LETTERS_SET_BY_POINTS[3]:
                continue
            if second_duo not in TWO_LETTERS_SET_BY_POINTS[2]:
                continue
            if third_duo not in valid_2_of_5:
                continue
            new_possibilities.append(
                {'words': add_word_to_list(word, possibility['words'], 13), 'letters': letters})
    print('Adding 14th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities
    if not possibilities:
        return

    # 9th
    score = scores['9th']
    letters = get_max_letters(possibilities)
    ninth_words_by_duo_letter = get_ninth_words_by_duo_letter(letters, score, dictionary, variant)
    new_possibilities = []
    for possibility in possibilities:
        duo = possibility['words'][5][-1] + possibility['words'][13][2]
        extra_letters = defaultdict(lambda: 0)
        extra_letters[possibility['words'][5][-1]] += 1
        extra_letters[possibility['words'][13][2]] += 1
        words = ninth_words_by_duo_letter[duo]
        for word in words:
            letters = is_word_possible(word, possibility['letters'], extra_letters)
            if not letters:
                continue
            new_possibilities.append(
                {'words': add_word_to_list(word, possibility['words'], 8), 'letters': letters})

    print('Adding 9th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    possibilities = new_possibilities
    if not possibilities:
        return

    guesses_left = {'15th', '8th', '12th', '20th', '17th', '18th', '13th', '10th', '11th', '16th'}
    while guesses_left:
        new_possibilities = []
        for x in guesses_left:
            result = GUESS_FUNCTIONS[x](possibilities, scores, dictionary, variant)
            if not result:
                print('No solutions :(')
                return
            new_possibilities.append((x, result))
        new_possibilities.sort(key=lambda x: len(x[1]))
        print([(x, len(y)) for x,y in new_possibilities])
        number, possibilities = new_possibilities[0]
        print('Using :', number)
        guesses_left.remove(number)
    return possibilities


if __name__ == '__main__':
    if len(sys.argv) == 2:
        config = json.loads(sys.argv[1])
        hash = hashlib.md5(sys.argv[1].encode('utf8')).hexdigest()
    else:
        config = {
            'dictionary': 'twl',
            'variant': {'1': 0, '2': 1, '3': 1},
            'last_letter': 'g',
            'scores': {
                '8th': 16,
                '9th': 16,
                '10th': 40,
                '15th': 22,
                '16th': 18,
                '17th': 20,
            }
        }
        hash = 'test'

    dictionary = None
    if config['dictionary'] == 'sowpods':
        dictionary = SOWPODS
    elif config['dictionary'] == 'twl':
        dictionary = TWL
    if not dictionary:
        print('Wrong dictionary param')

    result = try_to_solve(config['scores'], config['last_letter'], dictionary, config['variant'])
    if result:
        with open('solutions/solution_{}.json'.format(hash), 'w') as solution:
            json.dump(config, solution)
            solution.write('\n')
            json.dump(result, solution)
