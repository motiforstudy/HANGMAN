



def prompt_guess ():

    user_guess = input ("please guess a letter: ")
    return user_guess


def print_status (state : dict):

    print("the word:" ,state["display"], "    your wrong guesses:" ,state ["guessed"], "       you left: ", state["max_tries"] - state["wrong_guesses"], "guesses")


def print_result (state : dict):

    print (state)