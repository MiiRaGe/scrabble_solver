import copy
from collections import defaultdict

from generate_dict import ALL_WORDS
from utils import points, is_word_possible, INITIAL_COUNT


eigth_or_nineth_5_words = [x for x in ALL_WORDS[5] if points(x, None, 2) == 16]
eigth_or_nineth_5_words = [x for x in eigth_or_nineth_5_words if is_word_possible(x, INITIAL_COUNT)]
eigth_or_nineth_5_words_by_duo_letter = defaultdict(list)
for x in eigth_or_nineth_5_words:
    eigth_or_nineth_5_words_by_duo_letter[x[0:2]].append(x)

if __name__ == '__main__':
    print(eigth_or_nineth_5_words_by_duo_letter)
    print(len(eigth_or_nineth_5_words))