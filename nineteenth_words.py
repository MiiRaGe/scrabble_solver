from utils import points, is_word_possible, VALUES, END_LETTER_OF_2_POINTS_DUO


def get_nineteenth_words(letters, words):
    nineteenth_words = [x for x in words[2] if points(x, None, 2) == 4]
    return [x for x in nineteenth_words if is_word_possible(x, letters, {x[1]: 1})]
