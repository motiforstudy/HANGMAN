from data.words import words
from hangman.choose_word import choose_secret_word, display_the_under_score
from hangman.game import init_game, validate_guess, apply_guess, render_summary, is_won, is_lost
from hangman.io import prompt_guess, print_status

def play (words: list[str], max_tries : int):

    choose_sec_word = choose_secret_word(words)
    turn_to_under_score = display_the_under_score(choose_sec_word)
    start_the_game = init_game (choose_sec_word, turn_to_under_score ,max_tries)

    while start_the_game["wrong_guesses"] < max_tries:
        print_status(start_the_game)
        user_choice = prompt_guess()
        validate_guess(user_choice, start_the_game["guessed"])
        apply_guess(start_the_game, user_choice)
        if is_won(start_the_game):
            print("you win")
            break
        if is_lost(start_the_game):
            print("you loss")
            print (render_summary(start_the_game))
            break






if __name__ == "__main__":
    game_1 = play(words, 10)