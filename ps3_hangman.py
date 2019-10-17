# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(x, lg):
    count=len(x)
    for i in x:
        if i in lg:
            count-=1
    return count==0

def getGuessedWord(x, lg):
    sw=''
    for i in x:
        if i in lg:
            sw+=i
        else:
            sw=sw+"_ "
    return sw

def getAvailableLetters(lg):
    x="abcdefghijklmnopqrstuvwxyz"
    string=''
    for i in x:
        if i not in lg:
            string+=i
    return string        
secretWord=chooseWord(wordlist)
def hangman(secretWord):
    lifes = 8
    print ("ahln fl3bt alwad amshno2(hangman)\nana bfkar fee klma mn", len(secretWord),"angz ya shab7\n-----------------")
    LG=[]
    while lifes != 0:
        print("anta 3ndak ",lifes,"foras")
        print("al7orf al mtb2ia :",getAvailableLetters(LG))
        kmn=input("khmn rakm ynkm:")
        kmn=kmn.lower()
        if kmn not in getAvailableLetters(LG):
            kmn=input("anta kmnt 2bl kda dah")
        if kmn in secretWord:
            LG.append(kmn)
            print("3ash ywa7sh:",getGuessedWord(secretWord, LG),"\n---------------")
        else:
            LG.append(kmn)
            lifes-=1
            print("msh kda ym msh hn2olak al klma:",getGuessedWord(secretWord, LG),"\n---------------")
        if isWordGuessed(secretWord, LG):
            print ("anta kamd boftika")
            break
    if lifes == 0:
        print("anta t3ban alklma kant:",secretWord)
                
            
           
            
         
        
        
        
        
        
    
    
    
    






