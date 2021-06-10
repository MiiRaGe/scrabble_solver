from generate_dict import ALL_WORDS
from utils import points, is_word_possible, INITIAL_COUNT


multiplier = [1, 1, 2, 1, 1, 1, 1]
first_words = [x for x in ALL_WORDS[7] if points(x, multiplier, 2) == 70]
first_words = [x for x in first_words if is_word_possible(x, INITIAL_COUNT)]

if __name__ == '__main__':
    print(first_words)