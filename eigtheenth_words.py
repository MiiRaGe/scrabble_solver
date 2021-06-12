import copy
from collections import defaultdict

from generate_dict import TWL
from utils import points, is_word_possible, VALUES, INITIAL_COUNT


def get_eighteenth_words_by_first(letters, words, variant):
    eighteenth_words = [x for x in words[4] if is_word_possible(x, letters, {x[0]: 1})]
    eighteenth_words = [x for x in eighteenth_words if VALUES[x[1]] == 1]
    if variant['3'] == 1:
        eighteenth_words = [x for x in eighteenth_words if points(x[0:3], [1, 1, 1], 1) == 6]
        eighteenth_words = [x for x in eighteenth_words if x[0:3] in words[3]]
    else:
        eighteenth_words = [x for x in eighteenth_words if points(x, [1, 1, 1, 2], 1) == 6]

    eighteenth_words_by_first = defaultdict(list)
    for x in eighteenth_words:
        eighteenth_words_by_first[x[0]].append(x)
    return eighteenth_words_by_first


if __name__ == '__main__':
    words = get_eighteenth_words_by_first(INITIAL_COUNT, TWL, {'3': 1})
    for k,v in words.items():
        print(k, len(v))

    print('--- VARIANT ---')
    words = get_eighteenth_words_by_first(INITIAL_COUNT, TWL, {'3': 0})
    for k,v in words.items():
        print(k, len(v))
