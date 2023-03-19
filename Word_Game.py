# Autor: Ana Luisa Castañeda Garce
#    Wordle Type Game
import random

class ANSI():
    def color_text(code):
        # Black:   30
        # Red:     31
        # Green:   32
        # Yellow:  33
        # Blue:    34
        # Magenta: 35
        # Cyan:    36
        # White:   37
        return "\33[{code};1m".format(code=code)  
    
    def reset() :
        return "\33[0m".format()

print('Welcome to the game.\n\nInstructions: You have to guess our secret word. Pay attention to the number of letters in the word.')

word_list = ['mexico', 'python', 'origin', 'brazil', 'cheese', 'book', 'tiger', 'headphones', 'underscore', 'computer']
again = 'yes'

while again.lower() == 'yes' :
    word = random.choice(word_list)
    print('\nThe word is ', end="")
    for let in word :
        let = '_ '
        print(ANSI.color_text(31) + let  + ANSI.reset(), end="")    
    word_color = ANSI.color_text(34) + word.upper() + ANSI.reset() 
    print()

    guess = input('\nWhat is your guess? ')

    num_guess = 1

    while guess.lower() != word :
        num_guess = num_guess + 1
        
        if len(word) == len(guess) :
            print('\nYou are in the right path but this is not our secret word.\n')
            
            for i, letter in enumerate(guess) :
                if word[i] == guess[i] :
                    letter = letter.upper() + ' '
                elif letter in word:
                    letter = letter.lower() + ' '
                else :
                    letter = ANSI.color_text(31) + '_ ' + ANSI.reset()
                
                print(letter, end="")
            print()
        else :
            print('\nSorry, your guess needs to have the same number of letters as the word we are playing with.')

        guess = input('\nWhat is your guess? ')

    else :
        if num_guess == 1 :    
            print(f'\nCongratulations! Your guess is correct!\n \nThe word is {word_color}!\n')
            print(f'It took you 1 guess.\n')
        else :
            print(f'\nCongratulations! Your guess is correct!\n \nThe word is {word_color}!\n')
            print(f'It took you {num_guess} guesses.\n')
        
        again = input('Do you want to play again? ')
else :
    print('\nThank you for playing with me today.\n\nGoodbye!\n')