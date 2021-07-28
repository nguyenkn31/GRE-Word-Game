#Author: Kai Nguyen
#Created on May 15, 2021
#GREWordQuizBot_Mark1
import pandas as pd
import random
from termcolor import colored
import emoji

def load_word():
    wordList = pd.ExcelFile('BarronWordList.xlsx')
    data = wordList.parse(wordList.sheet_names[0])
    return data

def getRand(length):
  return random.randint(0, length-1)

def match_em_up(times):
    data = load_word()
    df = pd.DataFrame(data=data)
    correct = 0
    wrong = 0
    correct = []
    for i in range(times):
          length = len(df['Type'])
          row = getRand(length)
          Word = df['Word'][row]
          Type = df['Type'][row]
          Meanings = []
          rows = []
          correctMeaning = df['Meaning'][row]
          Meanings.append( df['Meaning'][row])
          rows.append(row)
          for loopOf3 in range(3):
            randomRow = getRand(length)
            while randomRow in rows:
              randomRow = getRand(length)
              rows.append(randomRow)
            Meanings.append( df['Meaning'][randomRow])
          
          random.shuffle(Meanings)
          #print('=====================================')
          if df['Star'][row] == 'Y':
            print("Difficulty level: Hard" )
          else:
            print("Difficulty level: Easy" )
          print("\nWord: " + colored(Word, 'green'))
          print("\nType: ",Type)
          print("\nMeanings: ") 
          for eachMeaning in range(len(Meanings)):
            print(eachMeaning+1, "  ", Meanings[eachMeaning])
          userInputAnswer = input("ANSWER: ")
          if userInputAnswer == 'hint':
            print('\nExample: ', df['Example'][row] )
            userInputAnswer = input("ANSWER: ")
          
          try:
            if userInputAnswer=='quit':
              break
            elif Meanings[int(userInputAnswer)-1] == correctMeaning:
              print('\n==========================')
              print(emoji.emojize('| You are correct! :face_with_tears_of_joy: :clapping_hands: |'))
              print('==========================')
              correct.append(1)
            else:
              print('\n==========================')
              print(emoji.emojize('Oops...that is incorrect. :< :face_screaming_in_fear: :face_with_head-bandage: '))
              print('The correct answer is: ' + colored(correctMeaning, 'green'))
              correct.append(0)
              print('==========================')
          except:
              print("Wrong input!")
              correct.append(0)
    
    print('\n=====================================')
    print('You did ' + str(len(correct)) + ' questions in total.')
    print('Your score is ' + colored(str(sum(correct)/len(correct) * 100) + '%', 'green') + ', which means you got ' + str(sum(correct)) + ' questions correctly.')
    print('=====================================')
    
def print_hangman(wrong):
    if wrong == 1:
        print ("_________")
        print ("|	 |")
        print ("|	 O")
        print ("|")
        print ("|")
        print ("|")
        print ("|________")
    elif wrong == 2:   
        print ("_________")
        print ("|	 |")
        print ("|	 O")
        print ("|	\|/")
        print ("|	 |")
        print ("|")
        print ("|________")
        
    elif wrong == 3:
        print ("_________")
        print ("|	 |")
        print ("|	 O")
        print ("|	\|/")
        print ("|	 |")
        print ("|	/ \ ")
        print ("|________")
        print ("\n\nThe End. ")
        return True
    return False

def hangman():
    data = load_word()
    df = pd.DataFrame(data=data)
    correct = 0
    wrong = 0
    correct = []
    for i in range(1):
        length = len(df['Type'])
        row =random.randint(0, length-1)
        Word = df['Meaning'][row]
        Type = df['Type'][row]
        Words = []
        rows = []
        correctMeaning = df['Word'][row]
        Words.append( df['Word'][row])
        rows.append(row)
        random.shuffle(Words)
        if df['Star'][row] == 'Y':
            print("Difficulty level: Hard" )
        else:
            print("Difficulty level: Easy" )
        print("\nMeaning: ",Word)
        print("\nType: ",Type)
        
        correctly_guessed = []
        for eachDash in range(len(correctMeaning)):
            correctly_guessed.append("_")
        print(" ".join(correctly_guessed))
        
        guessed = []
        wrong = 0
        won = False
        quit = False
        for eachDash in range(len(correctly_guessed)+3):
            print("\n\n")
            userInputAnswer = input("ANSWER: ")
            if userInputAnswer=='quit':
                quit=True
                break
            if userInputAnswer in correctly_guessed:
                print("Already filled!")
                continue
            found=False
            for eachLetter in range(len(correctMeaning)):
                if correctMeaning[eachLetter]==userInputAnswer:
                    correctly_guessed[eachLetter]=userInputAnswer
                    found=True
            if not found:
                wrong+=1
                ended = print_hangman(wrong)
                if ended:
                    break
            
            print(" ".join(correctly_guessed))
            
            if "_" not in correctly_guessed:
                print("You won!")
                won = True
                break
        if quit:
            print("Quit!")
        if not won and not quit:
            print("You lose! The word is " + correctMeaning)  
    return

def wordGame():
    choice = input('Welcome! What game would like to play today? \n1. Match \'Em Up!\n2. Hang-Man\n')
    play_num_times = input('Alright. How many times would you like to play?\n')
    if int(choice) == 1:
        print('Alright. Let\'s play!')
        match_em_up(int(play_num_times))
    elif int(choice) == 2:
        print('Alright. Let\'s play!')
        playagain = True
        while playagain:
            hangman()
            play = input('Wanna play again?\n1. Yes\n2. No\n')
            if play != "1":
                playagain=False
wordGame()
