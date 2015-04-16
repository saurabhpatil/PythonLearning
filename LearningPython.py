##This file is created to practice the python course examples to learn interactively 
import random

def percent_letter():
    input_str = input("Enter your word: ")
    input_num = input("Enter your number: ")

    try:
        number = int(input_num)
    except:
        number = float(input_num)

    if '.' in input_num:
        print(input_str[round(len(input_str)*number)])
    else:
        print(input_str[number-1])


###################################################################################

def shopping_list():
    shopping_list = list()  ##shopping_list = []
    to_shop = input("Do you want to go shopping(Yes/No)? ")
    
    if str.lower(to_shop) == 'yes':
        print("Enter the items to your shopping bag.")
        print("1.Enter 'Done' to end shopping \n"
              "2.Enter 'Show' to show shopping cart items")
        while True:
            item = input('> ')

            if item == 'Done':
                break
            elif item == 'Show':
                print("Your current list is: ")
                show_list(shopping_list)
                continue
                
            shopping_list.append(item)
            print('Added')
            continue
        print("Your complete Shopping list is:-")
        show_list(shopping_list)
    else:
        print("See you again some other time!")

def show_list(shopping_list):
        for item in shopping_list:
            print(item)


#####################################################################################

def guessing_game():
    number = random.randint(1,10)
    print("Guess a number between 1 and 10.\n"
          "You will have 5 chances.\n")
    
    for num in range(1,5):
        input_num = inputs()
        if input_num == number:
            print("Congratulations! You guessed it right. You used {} guesses for that.".format(num))
            return None
        elif input_num < number:
            print("Oops! You guessed it too low. Try again!")
        else:
            print("Oops! You guessed it too high. Try again!")
        continue

    print("You ran out of maximum allowed guesses.\n Better luck next time.")

def inputs():
    return int(input("Enter your guess: "))

#####################################################################################

def word_count(input_str):
  dictionary = {}
  word_list = input_str.split(' ')
  for word in word_list:
    if word not in dictionary.keys():
        dictionary[word]=1
    else:
        count = dictionary[word]
        dictionary[word] = count+1
  return(dictionary)

#####################################################################################

dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(dicts,string):
    string_list = list()
    for dictionary in dicts:
        string_list.append(string.format(**dictionary))
    return(string_list)

#####################################################################################

colour = [ "red", "blue", "green", "yellow", "purple", "orange", "white", "black" ]
rand_colours = [random.choice(colour) for i in range(50)]

#####################################################################################

class GameScore:
    score = tuple([5,8])
    def __str__(self):
        return("Player 1: {}; Player 2: {}".format(*self.score))

from LearningPython import GameScore
game = GameScore()
print(game)

