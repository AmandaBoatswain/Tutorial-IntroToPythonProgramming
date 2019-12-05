
# coding: utf-8

# ** Mac Robotics Club Tutorial 5: An Introduction to Coding in Python **
# Tuesday November 7, 2017
# Created by Amanda Boatswain Jacques

# In[3]:

## Printing to the screen
print('Hello')
print('World!')


# In[4]:

## Simple numerical operations
# (*) Means multiply, (/) means divide, (+) means to add, (-) means substract, etc. 
print(2+2)
print(3*7)
print(30-2)


# In[5]:

## Creating numerical variables
a = 9/5 
b = 20*a + 5 # use variable a in an operation
print('b = ')
print(b)

c = 30.985 # c is a floating point variable 
print('datatype of c: ')
print (type(c))

# We can also assign multiple variables at once
d, e, f = 1, 2, 3
print('e = ')
print(e)


# ** Other types of variables: **

# In[6]:

## Creating strings
item_name = "Raspberry Pi"
print('item name: ')
print(item_name)
print(len(item_name)) # Returns the number of characters in the string 
print(item_name[0]) # Find character in a particular place of the string
first_word = item_name[0:10]
print(first_word)

# Adding strings together 
a = 'A'
b = 'B'
print(a+b+a)  # Note that there are no spaces when characters are added together 


# In[7]:

## Creating and Manipulating Lists 
numbers = [67, 34, 51, 123, 10]
print('Numbers in list: ')
print(len(numbers))
print(numbers)
print(' ')

print('First number: ')
print(numbers[0])
print('First 3 numbers: ')
print(numbers[0:3])
print(' ')

# Change a value in the list 
numbers[2] = 1
print('Third value changed: ')
print(numbers)
print(' ')

# Sort the numbers
numbers.sort()
print('Sorted numbers: ')
print(numbers)
print(' ')

# Remove a value from the list
numbers.pop() # default is the last number in the list 
print('First number removed: ')
print(numbers)
print(' ')

print('Third number removed: ')
numbers.pop(2)
print(numbers)
print(' ')

# Insert a new value 
numbers.insert(1, 66) # Arguments are position of insertion and new value 
print(numbers)
print(' ')


# In[8]:

## Creating Dictionnaries
ages = {'Penny': 7, 'Alex': 10, 'Cynthia': 3}
print("Penny's age: ")
print(ages['Penny']) 

ages['Penny'] = 8 # Let's say it was Penny's birthday yesterday 
print('Updated ages: ')
print(ages) # Does not print in order! 


# ** Loops, Logicals and Functions ** 

# In[9]:

## For Loops
import random
for x in range(0, 11):
    print('x = ')
    print(x)
    
for a in range(0,6): 
    random_number = random.randint(1,6)
    print('random number = ')
    print(random_number)


# In[10]:

## Using Logical Statements 

# Boolean variables
print('Is 10 greater than 9? ')
print(10 > 9) # Returns a "True" value

k = 7 

if k > 9: # Will check if this condition is true 
    print('k is large')
elif k > 7: # Else if (adds multiple cases)
    print('k is fairly large')
else: 
    print('k is small')
    
# Try changing the value of k and see what prints next!


# In[11]:

## Dice Throwing using "if" statements 

import random # import the random function 
import time 
for x in range (1, 11):
    throw1 = random.randint(1,6) # choose a random integer between 1 and 6 
    throw2 = random.randint(1,6)
    total = throw1 + throw2
    time.sleep(2)  # Will wait two seconds 
    print(total)
    
    if total == 7:
        print('Seven thrown!')
    if total == 11:
        print('Eleven thrown!')
    if throw1 == throw2:
        print('Double thrown!')


# In[12]:

## Dice Throwing using a "while" Loop
import random # import the random function 

while True: 
    throw1 = random.randint(1,6) # choose a random integer between 1 and 6 
    throw2 = random.randint(1,6)
    total = throw1 + throw2
    print(total)
    if (throw1 == 6 and throw2 == 6):  
        break  # Will break out of the loop when a double six is thrown 
print('Double Six Thrown!')


# **Let's create a Hangman Game using functions**
# *Taken from Programming the Raspberry Pi by Simon Monk*

# In[15]:

## Functions 

import random

words = ['dog', 'cat', 'mouse', 'frog', 'chicken', 'snake'] # Create a list of words
lives_remaining = 14
guessed_letters = ' '


def play(): # Define the play game function 
    word = pick_a_word()
    while True:  # While loop will continue until the word is guessed or there are not more lives left 
        guess = get_guess(word)
        if process_guess(guess, word):
            print('You win!')
            break
        if lives_remaining == 0: 
            print('You are hung! :( ')
            print('The word was: ' + word)
            break 
            
# Now let's write up the individual functions that will create our game.
            
def pick_a_word(): # Picks a word from the list at random  
    return random.choice(words) 

def get_guess(word):
    print_word_with_blanks(word)
    print('Lives remaining: ' + str(lives_remaining))
    guess = input('Guess a letter or whole word? ') # Prompts the user for a letter 
    return guess

def print_word_with_blanks(word):
    display_word = ' '
    for letter in word:
        if guessed_letters.find(letter) > -1:
            # Letter found
            display_word = display_word + letter # Everytime a letter is properly guessed, it gets added to this string 
        else: 
            # Letter not found
            display_word = display_word + '-'
    print(display_word)

def process_guess(guess, word): 
    if len(guess) > 1: # If there is more than 1 letter, we assume it's a whole word guess 
        return whole_word_guess(guess, word)
    else: 
        return single_letter_guess(guess, word)

def whole_word_guess(guess, word):
    global lives_remaining # Global variable: Can be accessed from anywhere in the program 
    if guess.lower() == word.lower(): # Make sure the word/guesses are lowercase 
        return True
    else: 
        lives_remaining = lives_remaining -1 
        return False 

def single_letter_guess(guess, word):
    global guessed_letters
    global lives_remaining
    if (word.find(guess) == -1):
        # the letter was incorrect
        lives_remaining = lives_remaining - 1
    guessed_letters = guessed_letters + guess
    if all_letters_guessed(word):
        return True
    return False

def all_letters_guessed(word):
    for letter in word:
        if (guessed_letters.find(letter) == -1):
            return False # Searches through all the letters to see if they were all found 
    return True 

play()

