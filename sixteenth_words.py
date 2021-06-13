from collections import defaultdict

from utils import points, is_word_possible, get_max_letters, add_word_to_list


def get_sixteenth_words_by_last(letters, score, words):
    multiplier = [2, 1, 1, 1, 1]
    sixteenth_words = [x for x in words[5] if points(x, multiplier, 2) == score]
    sixteenth_words = [x for x in sixteenth_words if is_word_possible(x, letters, {x[-1]: 1})]

    sixteenth_words_by_last = defaultdict(list)
    for x in sixteenth_words:
        sixteenth_words_by_last['-'].append(x)
        sixteenth_words_by_last[x[-1]].append(x)
    return sixteenth_words_by_last


def guess_16th_word(possibilities, scores, dictionary, variant):
    score = scores['16th']
    letters = get_max_letters(possibilities)
    sixteenth_words_by_last = get_sixteenth_words_by_last(letters, score, dictionary)
    new_possibilities = []
    for possibility in possibilities:
        key = '-'
        if possibility['words'][14]:
            key = possibility['words'][14][4]
        words = sixteenth_words_by_last[key]
        for word in words:
            letters = is_word_possible(word, possibility['letters'], {word[-1]: 1})
            if not letters:
                continue
            new_possibilities.append(
                {'words': add_word_to_list(word, possibility['words'], 15), 'letters': letters})
    print('Adding 16th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    return new_possibilities
