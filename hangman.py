'''
Created on Nov 23, 2019

@author: ITAUser
'''
#import the random library

#def a function called pickRandomWord():
    #open and read word dictionary/list(word.txt)
    
    #variable called index = selects random word from words.txt
    #variable called word = strip the randomly selected word
    #return the variable called 'word'
    
#def a function called askForNextLetter():
    #variable called letter = input function that asks user to select a letter
    #return the letter selected
    
#def a function called generateWordString(word, lettersGuessed):
    #variable called output = empty list
    #make for loop goes through each letter in the variable 'word': 
        #if statement checks if letter is in lettersGuessed:
            #append letter to output
        #else:
            #append ("_")
        #return output as a string
        
#create a main module:
    #variable called WORD = pickRandomWord()
    
    #variable called lettersToGuess = set of WORD
    #variable called correctLettersGuessed = empty set
    #variable called incorrectLettersGuessed = empty set
    #variable called numberOfGuesses = number of guesses you want the user to have
   
    #print statement that welcomes user to hangman
    
#while loop that runs until (numberOfGuesses is < 1) or (lettersToGuess > 0)
    #variable called guess = askForNextLetter() and turn it into lower case

#if statement that checks if guess is in correctLettersGuessed or guess is in incorrectLettersGuessed:
    #print("you have already guessed that letter")

#if statement checks if guess is in lettersToGuess
    #remove guess from lettersToGuess
    #add guess to correctLettersGuessed 
#else:
    #add guess to incorrectLettersGuessed
    #numberOfGuesses goes down by 1
    
#variable called wordString = generateWord(WORD, correctLettersGuessed)
    #print statement that prints wordString
    #print statement that prints amount of guesses
#if statement to check if number of guesses are less than 1
    #print("Congrats! You've guessed the word correctly")
#else:
    #print("You Lost. the word was" + WORD)
    
    



