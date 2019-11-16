def isWordGuessed (secretWord, lettersGuessed):
#use "for" for strings 
    for x in secretWord:
#use "if" for letters
        if x not in lettersGuessed:
            return False
    else:
        return True