def isWordGuessed (secretWord, lettersGuessed):
#use "for" for strings 
    for x in secretWord:
#use "if" for letters
        if x not in lettersGuessed:
            return False
    else:
        return True
    
def getGuessedWord(secretWord, lettersGuessed):
    gtword=""
#use "_" for function
    for _ in secretWord:
         if _ in lettersGuessed:
             gtword+=_
         else:
            gtword+='_ '
    return gtword 

import string 
def getAvailableLetters (lettersGuessed):
    word= ''
#use "string.ascii_lowercase", helps bc it's a compilation of all lower case letters
    EngAlphabet = string.ascii_lowercase
    for l in EngAlphabet:
        if l in lettersGuessed:
            continue
        else:
            word+=l
    return word

def Hangaroo (secretWord):
    print("Hey there! Are you any good when it comes to guessing words? Welcome to Hangaroo")
    lettersGuessed= []
    mistakesMade=0
    while (secretWord!=lettersGuessed):
        if secretWord!= getGuessedWord(secretWord, lettersGuessed):
            print("Available letters: ", getAvailableLetters (lettersGuessed))
            print(getGuessedWord (secretWord, lettersGuessed))
            print("Mistakes made= ",mistakesMade)
            guess = input("Pick a letter: ")
            guessInLowerCase = guess.lower()
            
            if guessInLowerCase not in secretWord and guessInLowerCase not in lettersGuessed:
                mistakesMade+=1
                print("Engk! Make your chance worth it- try better!")
                
            elif guessInLowerCase not in secretWord and guessInLowerCase in lettersGuessed:
                print("You have already picked that letter! You are closing in- pick again")
                
            elif guessInLowerCase in secretWord and guessInLowerCase in lettersGuessed:
                print("You have already picked that letter! You are closing in- pick again!")
                
            else:
                lettersGuessed.append(guessInLowerCase)
                print("Correct deduction.")
                lettersGuessed.append(guessInLowerCase)
                
        else:
                print("Holah, well done! You deducted wisely and got the secret word!!")
                print("Secret word: ", getGuessedWord (secretWord, lettersGuessed))
                print("Mistakes made= ",mistakesMade)
                break
            