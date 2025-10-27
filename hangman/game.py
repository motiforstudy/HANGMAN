from hangman.io import print_result, print_status, prompt_guess


def init_game (secret_word : str, display : str ,max_tries : int):

    dict_of_info = {"secret_word" : secret_word, "display" : display, "guessed" : [], "wrong_guesses" : 0, "max_tries" : max_tries}


    return dict_of_info


def validate_guess(user_guess: str, guessed: set[str]):
    if len(user_guess) > 1:
        print("there is more than one letter. please guess again")
        return True

    elif user_guess in guessed:
        print("your guess is already in guessed")
        return True

    elif not user_guess.isalpha():
        print("please enter a letter not just char")
        return True

    else:
        guessed.append(user_guess)
        print("the guess went successfully")
        return False



def apply_guess (state : dict, user_guess : str):

        if user_guess in state["secret_word"]:
            for i in range (0, len(state["secret_word"])):
                if state["secret_word"][i] == user_guess:
                    state["display"][i] = user_guess
                    return True

        else:

            state ["wrong_guesses"] += 1
            return False


def is_won (state : dict):

    if "_" not in state["display"]:
        return True


def is_lost (state : dict):

    if state["wrong_guesses"] >= state["max_tries"]:

        return True



def render_display (state : dict):

    return state["display"]


def render_summary (state : dict):

    return state["secret_word"] , state["display"]