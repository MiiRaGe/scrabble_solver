import copy
from collections import defaultdict

from generate_dict import ALL_WORDS

end_letter = 'd'
INITIAL_COUNT = {
    '*': 2,
    'a': 9,
    'b': 2,
    'c': 2,
    'd': 4,
    'e': 12,
    'f': 2,
    'g': 2, # CHOICE
    'h': 2,
    'i': 9,
    'j': 1,
    'k': 1,
    'l': 4,
    'm': 2,
    'n': 6,
    'o': 8,
    'p': 2,
    'q': 1,
    'r': 6,
    's': 4,
    't': 6,
    'u': 4,
    'v': 2,
    'w': 2,
    'x': 1,
    'y': 2,
    'z': 1,
}
VALUES = {
    '*': 0,
    'a': 1,
    'e': 1,
    'i': 1,
    'l': 1,
    'n': 1,
    'o': 1,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'd': 2,
    'g': 2,
    'b': 3,
    'c': 3,
    'm': 3,
    'p': 3,
    'f': 4,
    'h': 4,
    'v': 4,
    'w': 4,
    'y': 4,
    'k': 5,
    'j': 8,
    'x': 8,
    'q': 10,
    'z': 10,
}



def add_blanks():
    raise Exception('do not use!')


def add_blanks_4(words):
    words_with_blanks = []
    originals = defaultdict(list)
    for word in words:
        words_with_blanks.append(word)
        for i in range(2, 4):
            new_word = word[:i] + '*' + word[i + 1:]
            originals[new_word].append(word)
            words_with_blanks.append(new_word)
    return list(set(words_with_blanks)), originals


def add_blanks_7(words):
    words_with_blanks = []
    originals = defaultdict(list)
    for word in words:
        words_with_blanks.append(word)
        for i in range(1, 3):
            new_word = word[:i] + '*' + word[i + 1:]
            originals[new_word].append(word)
            words_with_blanks.append(new_word)
    return list(set(words_with_blanks)), originals


def is_word_possible(word, remaining, extra_letters=None):
    if not extra_letters:
        extra_letters = {}
    remaining = copy.copy(remaining)
    for letter in word:
        remaining[letter] -= 1
        if remaining[letter] + extra_letters.get(letter, 0) < 0:
            return
    for (k, v) in extra_letters.items():
        remaining[k] += v
    return remaining


def points(word, index_multipliers=None, word_multiplier=1):
    if index_multipliers is None:
        index_multipliers = []
    if not index_multipliers:
        index_multipliers = [1] * len(word)
    total = 0
    for i, letter in enumerate(word):
        total += VALUES[letter] * index_multipliers[i]
    return total * word_multiplier


def is_score_possible(score, remaining):
    r = copy.copy(remaining)
    r[score] -= 1
    if r[score] >= 0:
        return r


TWO_LETTERS_SET = {x for x in ALL_WORDS[2]}
TWO_LETTERS_SET_BY_POINTS = defaultdict(set)
for duo in TWO_LETTERS_SET:
    TWO_LETTERS_SET_BY_POINTS[points(duo)].add(duo)

START_LETTER_OF_3_POINTS_DUO = set()
for duo in TWO_LETTERS_SET_BY_POINTS[3]:
    START_LETTER_OF_3_POINTS_DUO.add(duo[0])

START_LETTER_OF_2_POINTS_DUO = set()
END_LETTER_OF_2_POINTS_DUO = set()
for duo in TWO_LETTERS_SET_BY_POINTS[2]:
    START_LETTER_OF_2_POINTS_DUO.add(duo[0])
    END_LETTER_OF_2_POINTS_DUO.add(duo[1])

SEVEN_LETTERS_SET = {x for x in ALL_WORDS[7]}

VALID_FOUR = {x for x in ALL_WORDS[4]}

scrabble_scores = {16, 24, 36, 28}
remaining_scores = {66, 29, 22, 16, 40, 86, 74, 78, 18, 20, 6, 48}

possible_scores = {
    4: 1,
    6: 1,
    16: 2,
    18: 3,
    20: 1,
    22: 1,
    74: 1,
    78: 1,
    29: 1,
    86: 1,
    40: 1,
    66: 2,
    48: 1,
}


if __name__ == '__main__':
    print(START_LETTER_OF_3_POINTS_DUO)