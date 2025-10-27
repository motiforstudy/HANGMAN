from random import randint



def choose_secret_word (words : list[str]) -> str:

    len_of_index = len(words)
    random_number = randint(0, len_of_index)
    secret_word = words[random_number]

    return secret_word