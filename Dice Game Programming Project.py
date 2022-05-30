import sys
import time
from time import sleep
import os
import random

#Creates the Logins folder if it doesn't exist
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
createFolder('./logins/')
f = open('winners.txt', "a")
f.close()
f = open('leaderboard.txt', "a")
f.close()

def scrollTxt(text):
   for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.015)
   print()

def yuhTxt(text):
   for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.025)

def check(fname, txt):
    with open(fname) as dataf:
        return any(txt in line for line in dataf)


file = open("leaderboard.txt", "r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()


scrollTxt("WELCOME TO THE ULTİMATE DİCE GAME!")
useless= input("Press ENTER to continue.")
loopy = True
while loopy == True:
    scrollTxt("What would you like to do?")
    print("[1] = Start a New Two-Player Dice Game Match")
    print("[2] = View Past Winners")
    print("[3] = View Current Highscores")
    choice = input("")
    if choice == "1":
        print("")
        break
    elif choice == "2":
        print("")
        print("PAST WINNERS:")
        f = open('winners.txt', "r")
        allwinners = f.read()
        print(allwinners)
        f.close()
    elif choice == "3":
        print("")
        leaders = list()
        filename = 'leaderboard.txt'
        with open(filename) as fin:
            for line in fin:
                leaders.append(line.split())
        y = sorted(leaders, key = lambda x: float(x[0]), reverse=True)
        page = 5
        pageno = 1
        scrollTxt("CURRENT LEADERBOARD STANDINGS:")
        for eachline in y[:page]: #after this and the next line it prints just the file contents
            print(" ".join(eachline))
        boardsloop = True
        while boardsloop == True:
            print("")
            print("Write 'Next' to go to next page.")
            print("Write 'Back' to go to the previous page.")
            print("Write 'Menu' to go back to the Main Menu.")
            nextpage = input("")
            if nextpage.lower() == "next":
                page = page + 5
                print("")
                if page - 4 > line_count: #makes sure that you dont see blank pages
                    print("⚠ This is the last page. ⚠")
                else:
                    pageno = pageno + 1
                    print("CURRENT LEADERBOARD STANDINGS (Page "+str(pageno)+"):")
                    for eachline in y[page-5:page]: #after this and the next line it prints just the file contents
                                print(" ".join(eachline))
            elif nextpage.lower() == "back":
                if page == 5:
                    print("⚠ This is the first page. ⚠")
                else:
                    print("")
                    for eachline in y[page-10:page-5]: #after this and the next line it prints just the file contents
                                print(" ".join(eachline))
            elif nextpage.lower() == "menu":
                scrollTxt("Going back to Main Menu...")
                break
            else:
                scrollTxt("Invalid input. Going back to Main Menu.")
                break

    else:
        scrollTxt("Please enter 1, 2 or 3.")
        print("")
        

#Player 1 Login
login = True
while login == True: #loops the username login if the username is too long.
    name1 =  input("Player 1, Please enter a username: ")
    if len(name1) > 12: #checks if there are more than 12 characters
        print("This username is too long, Please enter a different one.")
    elif ' ' in name1:
        print("Please include no spaces.")
    else:
        break #continues the program
PATH = './logins/'+name1.lower()+'.txt'
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
   #ACCOUNT EXISTS
   print("Account Found!")

   for retry in range(3):
      pass1 = input(name1.title()+", Please enter the password for your account: ")
      scrollTxt("AUTHENTICATING...")
      if check('./logins/'+name1.lower()+'.txt', pass1):
         #Correct Password
         scrollTxt("Log In Successful!")
         break
      #Incorrect Password
      scrollTxt("Incorrect Password.")
   else:
      #Password Incorrect 3 Times
      scrollTxt("You have incorrectly entered the password too many times.")
      scrollTxt("⚠ TERMINATING LOGIN. ⚠")
      sys.exit()

else:
   #ACCOUNT DOES NOT EXIST
   print("Account Not Found.")
   scrollTxt("Creating New Account...")
   pass1 = input(name1.title()+", Please create a password for your account: ")
   scrollTxt("Your login details are being saved...")
   f = open('./logins/'+name1.lower()+'.txt', "a")
   f.write(pass1)
   f.close()
   scrollTxt("SAVED!")

scrollTxt("Player 1 ("+name1.title()+") is Ready to Play!")

print("")
#Player 2 Login
while login == True: #loops the username login if the username is too long.
    name2 =  input("Player 2, Please enter a username: ")
    if len(name2) > 12: #checks if there are more than 12 characters
        print("This username is too long, Please enter a different one.")
    else:
        break #continues the program
PATH = './logins/'+name2.lower()+'.txt'
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
   #ACCOUNT EXISTS
   print("Account Found!")

   for retry in range(3):
      pass2 = input(name2.title()+", Please enter the password for your account: ")
      scrollTxt("AUTHENTICATING...")
      if check('./logins/'+name2.lower()+'.txt', pass2):
         #Correct Password
         scrollTxt("Log In Successful!")
         break
      #Incorrect Password
      scrollTxt("Incorrect Password.")
   else:
      #Password Incorrect 3 Times
      scrollTxt("You have incorrectly entered the password too many times.")
      scrollTxt("⚠ TERMINATING LOGIN. ⚠")
      sys.exit()

else:
   #ACCOUNT DOES NOT EXIST
   print("Account Not Found.")
   scrollTxt("Creating New Account...")
   pass2 = input(name2.title()+", Please create a password for your account: ")
   scrollTxt("Your login details are being saved...")
   f = open('./logins/'+name2.lower()+'.txt', "a")
   f.write(pass2)
   f.close()
   print("SAVED!")

print("Player 2 ("+name2.title()+") is Ready to Play!")
print("")

scrollTxt("Both users are Ready!")
time.sleep(1)
yuhTxt("LOADING DİCE GAME")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".")
time.sleep(0.5)

scrollTxt("DİCE GAME IS READY!")
#Game Begins
#Makes 5 rounds
p1score=0
p2score=0
for round in range(1,6):
    print("")
    print("---------------------------------------------")
    print("")
    scrollTxt("Time for round "+str(round)+"!!")
    #Player 1's Turn
    scrollTxt(name1.title()+", it is your turn to roll the dice.")
    diceroll=input("Please press ENTER to roll. ")
    if diceroll == "skip":    #SKIPS THE WHOLE GAME CUZ I CANT BE ASKED TO RUN THIS WHOLE THING AGAIN TO TEST IT
        break
    roll1 = random.randint(1,6)
    scrollTxt(name1.title()+" rolled a "+str(roll1)+"!")
    diceroll=input("Please press ENTER to roll again. ")
    roll2 = random.randint(1,6)
    scrollTxt(name1.title()+" rolled a "+str(roll2)+"!")
    p1score= roll1+ roll2 +p1score
    if roll1 == roll2:
        scrollTxt("For rolling a double, you get to roll again!")
        diceroll=input("Press ENTER to roll again! ")
        roll3 = random.randint(1,6)
        scrollTxt(name1.title()+" rolled a "+str(roll3)+"!")
        p1score= p1score+roll3
    else:
        pass
    scrollTxt(name1+"'s overall score is now "+str(p1score)+"!")
    #Calculating whether score is even or odd
    if (p1score % 2) == 0:
        #Score is even
        scrollTxt("Because your overall score was even, you get 10 bonus points!!")
        p1score= p1score + 10
        scrollTxt("Your score is now "+str(p1score)+"!!")
    else:
        #Score is odd
        scrollTxt("Because your overall score was odd, you lose 5 points.")
        if p1score < 5:
            #To prevent score from going under 0
            print("Since your score is less than 5, it will just get set to 0.")
            p1score = 0
            scrollTxt("Your score is now "+str(p1score)+".")
        else:
            p1score = p1score - 5
            scrollTxt("Your score is now "+str(p1score)+".")

    time.sleep(1)
    print("---------------------------------------------")
    
    #Player 2's Turn
    scrollTxt(name2.title()+", it is your turn to roll the dice.")
    diceroll=input("Please press ENTER to roll. ")
    roll1 = random.randint(1,6)
    scrollTxt(name2.title()+" rolled a "+str(roll1)+"!")
    diceroll=input("Please press ENTER to roll again. ")
    roll2 = random.randint(1,6)
    scrollTxt(name2.title()+" rolled a "+str(roll2)+"!")
    p2score= roll1+ roll2 +p2score
    if roll1 == roll2:
        scrollTxt("For rolling a double, you get to roll again!")
        diceroll=input("Press ENTER to roll again! ")
        roll3 = random.randint(1,6)
        scrollTxt(name2.title()+" rolled a "+str(roll3)+"!")
        p2score= p2score+roll3
    else:
        pass
    scrollTxt(name2+"'s overall score is now "+str(p2score)+"!")
    #Calculating whether score is even or odd
    if (p2score % 2) == 0:
        #Score is even
        scrollTxt("Because your overall score was even, you get 10 bonus points!!")
        p2score= p2score + 10
        scrollTxt("Your score is now "+str(p2score)+"!!")
    else:
        #Score is odd
        scrollTxt("Because your overall score was odd, you lose 5 points.")
        if p2score < 5:
            #To prevent score from going under 0
            print("Since your score is less than 5, it will just get set to 0.")
            p2score = 0
            scrollTxt("Your score is now "+str(p2score)+".")
        else:
            p2score = p2score - 5
            scrollTxt("Your score is now "+str(p2score)+".")

    #Round Recap
    scrollTxt("At the end of Round "+str(round)+", "+name1.title()+" has "+str(p1score)+" points, and "+name2.title()+" has "+str(p2score)+" points.")
    remain = 5 - round
    if round < 5:
        scrollTxt("There's still "+str(remain)+" rounds remaining, anyone could still win!")
    elif round == 4:
        scrollTxt("There's only "+str(remain)+" round left. It's the final stretch!")
    else:
        pass

#The Game is Over

if p1score > p2score:
    #Player 1 Wins
    yuhTxt("The winner is")
    time.sleep(0.25)
    print(".", end="")
    time.sleep(0.25)
    print(".", end="")
    time.sleep(0.25)
    print(". ", end="")
    time.sleep(0.25)
    scrollTxt(name1.upper()+" with a final score of "+str(p1score)+"!! Congratulations!")
    winner = name1
    winscore = p1score

elif p2score > p1score:
    #Player 2 Wins
    yuhTxt("The winner is")
    time.sleep(0.25)
    print(".", end="")
    time.sleep(0.25)
    print(".", end="")
    time.sleep(0.25)
    print(".", end="")
    time.sleep(0.25)
    scrollTxt(" "+name2.upper()+" with a final score of "+str(p2score)+"!! Congratulations!")
    winner = name2
    winscore = p2score

elif p1score == p2score:
    #Results Tied
    scrollTxt("Since the final scores were tied, we're going into a TIEBREAKER!!")
    scrollTxt("You both roll a final dice and the highest score wins!")

    tie = True
    while tie == True:
        #Tiebreaker loops until there is ONE winner.
        diceroll=input(name1.title()+", press ENTER to roll. ")
        tie1 = random.randint(1,6)
        scrollTxt(name1.title()+" rolled a "+str(tie1)+".")
        print("---------------------------------------------")
        diceroll=input(name2.title()+", press ENTER to roll. ")
        tie2 = random.randint(1,6)
        scrollTxt(name2.title()+" rolled a "+str(tie2)+".")
        print("---------------------------------------------")
        if tie1 > tie2:
            scrollTxt("After the tiebreaker...")
            scrollTxt("The winner is "+name1.upper()+" with a final score of "+str(p1score)+"!! Congratulations!")
            winner = name1
            winscore = p1score
            break       #Stops the tiebreaker from looping
        elif tie2 > tie1:
            scrollTxt("After the tiebreaker...")
            scrollTxt("The winner is "+name2.upper()+" with a final score of "+str(p2score)+"!! Congratulations!")
            winner = name2
            winscore = p2score
            break       #Stops the tiebreaker from looping
        else:
            scrollTxt("Since you tied again, we'll keep going!")
            print("---------------------------------------------")

scrollTxt("Winner's score being saved...")
f = open('winners.txt', "a")
f.write(winner+" with "+str(winscore)+" points. \n")
f.close()
print("WInner's data has been stored !!")
print("")

scrollTxt("Adding both players' scores to the leaderboard...")
f = open('leaderboard.txt', "a")
f.write(str(p1score)+" : "+name1+'\n')
f.write(str(p2score)+" : "+name2+'\n')
f.close()
print("Leaderboard data saved !!")
print("")
scrollTxt("CURRENT LEADERBOARD STANDINGS:")
print(str(p1score)," : ",name1)
print(str(p2score)," : ",name2)
print("---------------")
leaders = list()
filename = 'leaderboard.txt'
with open(filename) as fin:
    for line in fin:
        leaders.append(line.split())
y = sorted(leaders, key = lambda x: float(x[0]), reverse=True)
for eachline in y[:5]: #after this and the next line it prints just the file contents
    print(" ".join(eachline))

scrollTxt("The Dice Game has now ended.")
scrollTxt("Thanks for Playing !!")
scrollTxt("Now Ending the Program...")
sys.exit()

