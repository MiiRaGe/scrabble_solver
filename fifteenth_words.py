from collections import defaultdict

from utils import points, is_word_possible, get_max_letters, add_word_to_list


def get_extra_letters(x):
    extra_letters = defaultdict(lambda: 0)
    extra_letters[x[0]] += 1
    extra_letters[x[-1]] += 1
    return extra_letters


def get_fifteenth_words_by_first_mid_last(letters, score, words, variant):
    if variant['2'] == 1:
        fifteenth_words = [x for x in words[7] if points(x[0:6], None, 2) == score]
    else:
        fifteenth_words = [x for x in words[7] if points(x, None, 2) == score]
    fifteenth_words = [x for x in fifteenth_words if is_word_possible(x, letters, get_extra_letters(x))]
    fifteenth_words_by_first_mid_last = defaultdict(list)
    for x in fifteenth_words:
        fifteenth_words_by_first_mid_last[x[0] + x[4] + x[-1]].append(x)
        fifteenth_words_by_first_mid_last[x[0] + '--'].append(x)
        fifteenth_words_by_first_mid_last[x[0] + '-' + x[-1]].append(x)
        fifteenth_words_by_first_mid_last[x[0] + x[4] + '-'].append(x)

    return fifteenth_words_by_first_mid_last


# 15th word ? points
def guess_15th_word(possibilities, scores, dictionary, variant):
    score = scores['15th']
    letters = get_max_letters(possibilities)
    fifteenth_words_by_first_mid_last = get_fifteenth_words_by_first_mid_last(letters,score,dictionary,variant)
    new_possibilities = []
    for possibility in possibilities:
        key = possibility['words'][4][1]
        if possibility['words'][15]:
            key += possibility['words'][15][-1]
        else:
            key += '-'
        if possibility['words'][11]:
            key += possibility['words'][11][3]
        else:
            key += '-'
        words = fifteenth_words_by_first_mid_last[key]
        for word in words:
            letters = is_word_possible(word, possibility['letters'], get_extra_letters(word))
            if not letters:
                continue
            new_possibilities.append(
                {'words': add_word_to_list(word, possibility['words'], 14), 'letters': letters})
    print('Adding 15th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    return new_possibilities