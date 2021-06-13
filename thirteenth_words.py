from utils import points, is_word_possible, VALUES, add_blanks_4, END_LETTER_OF_2_POINTS_DUO, add_word_to_list, \
    get_max_letters, TWO_LETTERS_SET


def get_thirteenth_words(letters, words):
    multiplier = [1, 1, 1, 2]
    thirteenth_words = [x for x in words[4] if points(x, multiplier, 3) >= 18]
    thirteenth_words = [x for x in thirteenth_words if x[1] in END_LETTER_OF_2_POINTS_DUO]
    thirteenth_words = [x for x in thirteenth_words if x[2] in END_LETTER_OF_2_POINTS_DUO]
    thirteenth_words = [x for x in thirteenth_words if x[3] in END_LETTER_OF_2_POINTS_DUO]
    thirteenth_words, _ = add_blanks_4(thirteenth_words)
    thirteenth_words = [x for x in thirteenth_words if points(x, multiplier, 3) >= 18]
    thirteenth_words, _ = add_blanks_4(thirteenth_words)
    thirteenth_words = [x for x in thirteenth_words if points(x, multiplier, 3) == 18]
    thirteenth_words = [x for x in thirteenth_words if is_word_possible(x, letters)]
    thirteenth_words = [x for x in thirteenth_words if VALUES[x[1]] == 1]
    thirteenth_words = [x for x in thirteenth_words if VALUES[x[2]] <= 1 and VALUES[x[3]] <= 1]
    return thirteenth_words


def guess_13th_word(possibilities, scores, dictionary, variant):
    letters = get_max_letters(possibilities)
    thirteenth_words = get_thirteenth_words(letters, dictionary)
    new_possibilities = []
    for possibility in possibilities:
        extra_letters = {}
        for word in thirteenth_words:
            if possibility['words'][11]:
                twelveth_word = possibility['words'][11]
                if twelveth_word[0] + word[1] not in TWO_LETTERS_SET:
                    continue
                if points(twelveth_word[1] + word[2]) != 1:
                    continue
                if points(twelveth_word[2] + word[3], None, 2) != 2:
                    continue
            letters = is_word_possible(word, possibility['letters'], extra_letters)
            if not letters:
                continue
            new_possibilities.append(
                {'words': add_word_to_list(word, possibility['words'], 12), 'letters': letters})
    print('Adding 13th: Before/After {} {}'.format(len(possibilities), len(new_possibilities)))
    return new_possibilities

