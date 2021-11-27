# random number guessing game

import random

def start_game():
### determine whether or not user wants to play
    while True:
        play = input('Welcome to Guess the Number! Would you like to play? (y/n): ')

        if play.isalpha():
            play = play.lower()        
        if play == 'y' or play == 'yes':
            lets_play(set_range())
        if play == 'n' or play == 'no':
            print('That\'s too bad. Come back soon!')
            quit()
        else:
            print('Invalid input. Please try again.')

def set_range():
### allow user to choose upper bound
    while True:
        maximum_range = input('Choose the maximum range (Enter a number): ')

        if maximum_range.isdigit():
            print('Time to play!')
            maximum_range = int(maximum_range)
            return maximum_range
        else:
            print('Invalid input. Please try again.')

def lets_play(maximum_range):
### guess until you win and find out number of guesses at the end
    correct_answer = random.randint(1,maximum_range)

    player_guess = None
    number_of_guesses = 1

    while player_guess != correct_answer:
        player_guess = input('Guess a number between 1 and ' + str(maximum_range) + ': ')
        
        if player_guess.isdigit():
            player_guess = int(player_guess)
        if player_guess == correct_answer:
            print('You guessed correctly! Congratulations!')
        else:
            low_high_check(correct_answer, player_guess)
            number_of_guesses += 1

    print('It took you ' + str(number_of_guesses) + ' tries.')
    play_again()

def low_high_check(correct_answer, player_guess):
### tells user whether their guess was above or below the correct number
    if player_guess < correct_answer:
        print('Your guess was too low. Please try again.')
    elif player_guess > correct_answer:
        print('Your guess was too high. Please try again.')

def play_again():
### allow for perpetual replayability
    while True:
        final_choice = input('Play again? (y/n)')

        if final_choice.isalpha():
            final_choice = final_choice.lower()        
        if final_choice == 'y' or final_choice == 'yes':
            lets_play(set_range())
        if final_choice == 'n' or final_choice == 'no':
            print('That\'s too bad. Come back soon!')
            quit()
        else:
            print('Invalid input. Please try again.')

start_game()