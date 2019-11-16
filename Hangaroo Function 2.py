def getGuessedWord (secretWord, lettersGuessed):
    gtword = ""
#use "_" for function
     for _ in secretWord:
         if _ in lettersGuessed:
             gtword += _
        else:
            gtword =+ "_ "
    return gtword 