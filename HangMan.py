import random_words
from easygui import passwordbox
import os
# global pixel art for the game

strikes_0 = """ 
                ____________
                |           |
                |           |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                   _________|__________"""

strikes_1 = """
                ____________
                |           |
                |           |
               _|_          |
              |___|         |
                            |
                            |
                            |
                            |
                            |
                            |
                   _________|__________"""

strikes_2 = """
                ____________
                |           |
                |           |
               _|_          |
              |___|         |
                |           |
                |           |
                |           |
                            |
                            |
                            |
                   _________|__________ """

strikes_3 = """
                ____________
                |           |
                |           |
               _|_          |
              |___|         |
                |           |
                | \         |
                |  \        |
                            |
                            |
                            |
                   _________|__________"""

strikes_4 = """
                ____________
                |           |
                |           |
               _|_          |
              |___|         |
                |           |
              / | \         |
             /  |  \        |
                            |
                            |
                            |
                   _________|__________"""

strikes_5 = """
                ____________
                |           |
                |           |
               _|_          |
              |___|         |
                |           |
              / | \         |
             /  |  \        |
                 \          |
                  \         |
                            |
                   _________|__________"""

strikes_6 = """ 
                ____________
                |           |
                |           |
               _|_          |
              |___|         |
                |           |
              / | \         |
             /  |  \        |
               / \          |
              /   \         |
                            |
                   _________|__________ """


def get_random_word():
    rw = random_words.RandomWords()
    return rw.random_word().upper()


def run_two_player():
    rw = passwordbox('Enter your secret word. Type carefully!').upper()
    rw_list = [char for char in rw]
    strlen = len(rw)
    string_for_player = get_string_for_player(rw)
    strikes = 0
    guess_list = []
    replace = 0

    while strikes < 6:
        guess_list.sort()
        for i in range(strlen):
            print string_for_player[i],
        print_man(strikes)
        print 'Guesses: ',
        print guess_list
        print '\n'
        letter = get_guess()
        guess_list.append(letter)
        if letter in rw_list:
            print "You found a letter!"
            for x in range(strlen):
                if rw_list[x] == letter:
                    string_for_player[x] = rw_list[x]
                    replace += 1
            if replace == strlen:
                for i in range(strlen):
                    print string_for_player[i],
                print 'YOU WON!'
                break
            print '\n'
        else:
            print 'Sorry. That is not a letter!'
            strikes += 1
            print str(strikes)
    if strikes == 6:
        print_man(strikes)
        print 'You lose! The word was ' + rw


def get_guess():
    proper_guess = False
    while not proper_guess:
        guess = raw_input("Enter a single letter: ").upper()
        if len(guess) == 1:
            proper_guess = True
        elif guess == 'EXIT':
            exit(1)
        else:
            guess = raw_input("Enter a single letter: ")
    return guess


def get_string_for_player(s):
    ret = []
    for i in range(len(s)):
        ret.append("*")
    return ret


def print_man(strike_count):
    if strike_count == 0:
        print strikes_0
    elif strike_count == 1:
        print strikes_1
    elif strike_count == 2:
        print strikes_2
    elif strike_count == 3:
        print strikes_3
    elif strike_count == 4:
        print strikes_4
    elif strike_count == 5:
        print strikes_5
    elif strike_count == 6:
        print strikes_6


def run_one_player():
    rw = get_random_word().upper()
    rw_list = [char for char in rw]
    strlen = len(rw)
    string_for_player = get_string_for_player(rw)
    strikes = 0
    guess_list = []
    replace = 0

    while strikes < 6:
        os.system('cls')
        guess_list.sort()
        for i in range(strlen):
            print string_for_player[i],
        print_man(strikes)
        print 'Guesses: ',
        print guess_list
        print '\n'
        letter = get_guess()
        guess_list.append(letter)
        if letter in rw_list:
            print "You found a letter!"
            for x in range(strlen):
                if rw_list[x] == letter:
                    string_for_player[x] = rw_list[x]
                    replace += 1
            if replace == strlen:
                for i in range(strlen):
                    print string_for_player[i],
                print 'YOU WON!'
                break
            print '\n'
        else:
            print 'Sorry. That is not a letter!'
            strikes += 1
            print str(strikes)
    if strikes == 6:
        print_man(strikes)
        print 'You lose! The word was ' + rw


def start_game():
    players = 0
    play_again = False
    exit_loop = False
    while players < 1:
        num = raw_input('Please enter the number of players (One or Two):').strip()
        if num == '1' or num == 'one' or num == 'One':
            print 'One-Player Selected'
            players = 1
            run_one_player()
        elif num == '2' or num == 'two' or num == 'Two':
            print 'Two-Player Selected'
            players = 2
            run_two_player()
    while not exit_loop:
        string = raw_input("Would you like to play again?").upper()
        if 'YES' == string:
            play_again = True
            exit_loop = True
        elif 'NO' == string:
            exit(0)
        else:
            pass
    if play_again:
        start_game()


if __name__ == '__main__':
    print "Welcome to the game!"
    start_game()
    print '\nThanks for playing!'
