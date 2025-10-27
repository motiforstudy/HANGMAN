from hangman.choose_word import choose_secret_word
from data.words import words

def play (words: list[str], max_tries : int = 6):

    the_word = choose_secret_word(words)
    return the_word






if __name__ == "__main__":
    game_1 = play(words, 10)


    print(game_1)