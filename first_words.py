from utils import points, is_word_possible


multiplier = [1, 1, 2, 1, 1, 1, 1]


def get_first_words(letters, words):
    first_words = [x for x in words[7] if points(x, multiplier, 2) == 70]
    return [x for x in first_words if is_word_possible(x, letters)]


if __name__ == '__main__':
    pass