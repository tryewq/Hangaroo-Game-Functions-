import string 
def getAvailableLetters (lettersGuessed):
    word = ''
#use "string.ascii_lowercase", helps bc it's a compilation of all lower case letters
    EngAlphabet = string.ascii_lowercase
    for l in EngAlphabet:
        if l in lettersGuessed:
            continue
        else:
            word+=l
    return word