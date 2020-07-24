#!/usr/bin/env python
# coding: utf-8

# Module 3 - Python Coding
# 
# Please note that this script will require the Colorama 0.4.3 module avalible at https://pypi.org/project/colorama/ 
# (pip install colorama)
# 

# In[11]:


#game setup - import of the words file and setup of global defaults. 

import random
from colorama import Fore, Back, Style                          #used to style the colours for the HANGMAN display

with open("word_list.txt","r") as f:                            #read the words file, read only
    data = f.read() #import to the script
    data_list = data.split("\n")                                #splitting the file into the individual values using the newline value \n, list for indexing
    guess_word = data_list[random.randint(0,(len(data_list)))]  #randomly selecting word from the list. dynamic length to allow for changes to the list if needed
    
empty_grid = "*" * len(guess_word)                              #setup of the word to guess values
display_word = list(empty_grid)                                 #list of the values to allow updating by positional value

wrong_guess = 0                                                 #global value for counting the number of wrong guesses


# In[12]:


#function to allow for a guess to be input and check validity of the input

def guess_input():
    alpha = "abcdefghijklmnopqrstuvwxyz"                          #used to confirm only alpabet characters
    guess = ""                                                    #used as part of the input check process
        
    while not (len(guess) == 1 and guess in alpha):               #while loop will not allow function to close and submit value unless valid input entered. checking that only 1 character length and in teh aplhabet
        guess = input("Please enter your next guess: ").lower()   #input field, lower case for check against alpha
    else:
        return guess                                              #if valid function returns the input value to the main script


# In[13]:


#function to update the guesses characters into the display 

def update_correct():
    epos = [i for i, x in enumerate(guess_word) if x == guess]  #lambda expression to get the postion of the character in the origional word, outputs a list. pre filtered by previous code in main block so character always valid.

    for pos in epos:
        display_word[pos] = guess                               #uses the output from the previous expression to update the values in the display list
        


# In[14]:


#function to show the HANGMAN countdown as a colourised word

def hangman_display():
    HList = ["H","A","N","G","M","A","N"]                                #final word to be displayed as a list
    I_List = HList[0:wrong_guess]                                        #Slice to be displayed Red
    I_List2 = HList[wrong_guess:len(HList)]                              #Slice to be displayed Black
    print((Fore.RED+("".join(I_List)) + Fore.BLACK+("".join(I_List2))))  #rejoin the lists for display


# In[15]:


#Game code block

print("Welcome to HANGMAN, please only enter guesses as single characters")
while  True: #keeps the game playing 
    
    print("Word to guess = "+ "".join(display_word))
    
    if "*" not in display_word:              #win check
        print("congratulations you win")
        break                                #exit the game
        
    elif wrong_guess == 7:                   #loose check
        print(f"word was: "+ guess_word)
        print("you lose")
        break                                #exit the game
    else:                                    #if game not won or lost run the input function
        guess = guess_input()
        if guess in guess_word:              #check if character guessed is in the word
            update_correct()                 #if true run the update function
        else:
            wrong_guess = wrong_guess +1     #if character not in the work update the wrong guesses global variable and run the HANGMAN display funtion
            hangman_display()

