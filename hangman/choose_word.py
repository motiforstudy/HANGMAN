from random import randint



def choose_secret_word (words : list[str]) -> str:

    len_of_index = len(words)
    random_number = randint(0, len_of_index)
    secret_word = words[random_number]



    return secret_word


def display_the_under_score(secrete_word):

    the_under_score = ["_"]
    the_len_of_the_word = len(secrete_word)
    all_line_of_under_score = the_under_score * the_len_of_the_word

    return all_line_of_under_score