import copy

from generate_dict import ALL_WORDS
from utils import points, is_word_possible, add_blanks_4, add_blanks_7, INITIAL_COUNT, VALUES

maximum_letters = {
    '*': 2,
    'a': 7,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 7,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 4,
    'j': 0,
    'k': 0,
    'l': 3,
    'm': 0,
    'n': 4,
    'o': 4,
    'p': 1,
    'q': 0,
    'r': 6,
    's': 2,
    't': 4,
    'u': 0,
    'v': 1,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0,
}


def is_valid_4(word):
    if not VALUES[word[1]] == 1:
        return False
    if VALUES[word[2]] <= 1 and VALUES[word[3]] <= 1:
        return True
    return False


multiplier = [1, 1, 1, 2]
four_letters = [x for x in ALL_WORDS[4] if points(x, multiplier, 3) >= 18]
four_letters = [x for x in add_blanks_4(four_letters) if points(x, multiplier, 3) >= 18]
four_letters = [x for x in add_blanks_4(four_letters) if points(x, multiplier, 3) == 18]
four_letters = [x for x in four_letters if is_word_possible(x, maximum_letters, {})]
four_letters = [x for x in four_letters if is_valid_4(x)]


def is_valid_7(word):
    if not VALUES[word[0]] == 1:
        return False
    if VALUES[word[1]] > 1:
        return False
    if VALUES[word[2]] not in {0, 2}:
        return False
    if VALUES[word[-1]] != 1:
        return False
    if VALUES[word[-2]] != 1:
        return False
    return True


multiplier = [1, 1, 1, 1, 3, 1, 1]
seven_letter = [x for x in ALL_WORDS[7] if points(x, multiplier, 2) >= 28]
seven_letter = [x for x in add_blanks_7(seven_letter) if points(x, multiplier, 2) >= 28]
seven_letter = [x for x in add_blanks_7(seven_letter) if is_valid_7(x) and points(x, multiplier, 2) == 28]
seven_letter = [x for x in seven_letter if is_word_possible(x, maximum_letters, {})]


valid_two_letter_word = {x for x in ALL_WORDS[2]}


def good_match(seven, four):
    duo = seven[0] + four[1]
    if duo not in valid_two_letter_word:
        return False
    if points(seven[0] + four[1]) != 2:
        return False
    if points(seven[1] + four[2]) != 1:
        return False
    if points(seven[2] + four[3], [1, 2]) != 2:
        return False
    return is_word_possible(four + seven, maximum_letters, {})


combo_7_4 = []
for four in four_letters:
    for seven in seven_letter:
        if good_match(seven, four):
            combo_7_4.append((seven, four))

if __name__ == '__main__':
    print(len(seven_letter))
    print(four_letters)